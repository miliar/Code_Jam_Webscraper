#include <iostream>
#include <string>
#include <cassert>

enum class Quaternion
{
    ONE       = 0,
    MINUS_ONE = 1,
    I         = 2,
    MINUS_I   = 3,
    J         = 4,
    MINUS_J   = 5,
    K         = 6,
    MINUS_K   = 7
};

using Q = Quaternion;

static constexpr Quaternion MinusTable[] = { Q::MINUS_ONE, Q::ONE, Q::MINUS_I, Q::I, Q::MINUS_J, Q::J, Q::MINUS_K, Q::K };

constexpr Quaternion operator -(Quaternion q)
{
    return MinusTable[(int)q];
}

static constexpr Quaternion MultTable[8][8] = {
    {  Q::ONE,  -Q::ONE,   Q::I,    -Q::I,     Q::J,    -Q::J,     Q::K,    -Q::K    },
    { -Q::ONE,   Q::ONE,  -Q::I,     Q::I,    -Q::J,     Q::J,    -Q::K,     Q::K    },
    {  Q::I,    -Q::I,    -Q::ONE,   Q::ONE,   Q::K,    -Q::K,    -Q::J,     Q::J    },
    { -Q::I,     Q::I,     Q::ONE,  -Q::ONE,  -Q::K,     Q::K,     Q::J,    -Q::J    },
    {  Q::J,    -Q::J,    -Q::K,     Q::K,    -Q::ONE,   Q::ONE,   Q::I,    -Q::I    },
    { -Q::J,     Q::J,     Q::K,    -Q::K,     Q::ONE,  -Q::ONE,  -Q::I,     Q::I    },
    {  Q::K,    -Q::K,     Q::J,    -Q::J,    -Q::I,     Q::I,    -Q::ONE,   Q::ONE  },
    { -Q::K,     Q::K,    -Q::J,     Q::J,     Q::I,    -Q::I,     Q::ONE,  -Q::ONE  }
};

Quaternion operator *(Quaternion q1, Quaternion q2)
{
    return MultTable[(int)q1][(int)q2];
}

Quaternion pow(Quaternion q, int p)
{
    Quaternion r = Q::ONE;
    for (int i = 1; i <= p; ++i)
        r = r * q;
    return r;
}

Quaternion from_char(char c)
{
    switch (c)
    {
    case 'i':
        return Q::I;
    case 'j':
        return Q::J;
    case 'k':
        return Q::K;
    }
    assert(false);
    return Q::ONE;
}

Quaternion get_next(Quaternion q)
{
    switch (q)
    {
    case Q::I:
        return Q::J;
    case Q::J:
        return Q::K;
    }
    assert(false);
    return Q::ONE;
}

template <class Iter>
Iter next_iter(Iter global_begin, Iter global_end, Iter i)
{
    ++i;
    if (i == global_end)
        return global_begin;
    return i;
}

template <class Iter>
int update_if_next_iter(Iter global_end, Iter i, int x)
{
    ++i;
    if (i == global_end)
        return x - 1;
    return x;
}

template <class Iter>
Quaternion calculate(Iter begin, Iter end)
{
    auto res = Q::ONE;
    for (Iter i = begin; i != end; ++i)
        res = res * from_char(*i);
    return res;
}

template <class Iter>
bool helper_splittable(Iter global_begin, Iter begin, Iter end, Quaternion part_value, int pow_reminder, Quaternion to_find, Quaternion pre_value = Q::ONE)
{
    if (pow_reminder == 0)
        return false;

    bool find_more = part_value != Q::ONE && begin == global_begin && pow_reminder > 0;
    Quaternion res = Q::ONE;

    for (Iter i = begin; i != end; ++i)
    {
        res = res * from_char(*i);

        if (pre_value * res == to_find)
        {
            if (to_find == Q::K)
            {
                if (i + 1 == end && (part_value == Q::ONE || (pow_reminder - 1) % 4 == 0))
                    return true;
            }
            else if (helper_splittable(global_begin, next_iter(global_begin, end, i), end, part_value, update_if_next_iter(end, i, pow_reminder), get_next(to_find)))
            {
                return true;
            }
        }
        else if (find_more)
        {
            for (int c_pow = 1; c_pow < 4 && pow_reminder > c_pow; ++c_pow)
            {
                Quaternion v = pow(part_value, c_pow);
                if (pre_value * v * res == to_find)
                {
                    if (to_find == Q::K)
                    {
                        if (i + 1 == end && ((pow_reminder - 1) % 4 == c_pow))
                            return true;
                    }
                    else if (helper_splittable(global_begin, next_iter(global_begin, end, i), end, part_value, update_if_next_iter(end, i, pow_reminder) - c_pow, get_next(to_find)))
                    {
                        return true;
                    }
                }
            }
        }
    }
    if (begin == global_begin)
        return false;
    return helper_splittable(global_begin, global_begin, end, part_value, pow_reminder - 1, to_find, res);
}

template <class Iter>
bool Solve(int length, Iter begin, Iter end, int repeat_times)
{
    return helper_splittable(begin, begin, end, calculate(begin, end), repeat_times, Q::I);
}

int main()
{
    int t = 0;
    std::cin >> t;

    for(int i = 0; i < t; ++i)
    {
        int l, x;
        std::string str;
        std::cin >> l >> x >> str;

        bool res = Solve(l, str.cbegin(), str.cend(), x);
        std::cout << "Case #" << i + 1 << ": " << (res ? "YES" : "NO") << "\n";
    }
    return 0;
}
