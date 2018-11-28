#include <iostream>
#include <string>

enum Ix {E, I, J, K};

Ix mul_table[4][4] =
    { { E, I, J, K }
    , { I, E, K, J }
    , { J, K, E, I }
    , { K, J, I, E }
    };

bool mul_signs[4][4] =
    { { false, false, false, false }
    , { false, true, false, true }
    , { false, true, true, false }
    , { false, false, true, true }
    };

struct Q
{
    Ix val;
    bool sign;

    Q(const Q &r):
        val(r.val),
        sign(r.sign)
    {}

    Q():
        val(E),
        sign(false)
    {}

    Q(char c):
        sign(false)
    {
        switch(c) {
            case '1': val = E; break;
            case 'i': val = I; break;
            case 'j': val = J; break;
            case 'k': val = K; break;
        }
    }

    bool operator==(const Q &r)
    {
        return val == r.val && sign == r.sign;
    }

    bool operator!=(const Q &r)
    {
        return val != r.val || sign != r.sign;
    }

    Q & operator *= (const Q &r)
    {
        sign ^= r.sign ^ mul_signs[val][r.val];
        val = mul_table[val][r.val];
        return *this;        
    }

    Q operator *(const Q &r)
    {
        Q res(*this);
        res *= r;
        return res;
    }

    Q pow(size_t n)
    {
        if (n == 1)
            return *this;
        if (n & 1)
            return (*this) * this->pow(n - 1);
        else {
            Q tmp = this->pow(n >> 1);
            return tmp * tmp;
        }
    }
};

Q qi('i'), qj('j'), qk('k');

std::ostream &operator<<(std::ostream &str, const Q &q)
{
    if (q.sign)
        str << '-';
    switch (q.val) {
        case E: str << '1'; break;
        case I: str << 'i'; break;
        case J: str << 'j'; break;
        case K: str << 'k'; break;
    }
    return str;
}

bool solve(const std::string &str, size_t x)
{
    static const Q ijk = qi * qj * qk;
    Q q, ti;
    size_t ipos = 0;
    for (size_t i = 0; i < str.length(); ++i) {
        q *= Q(str[i]);
        if (q == qi && ti.val == E) {
            ipos = i;
            ti = q;
        }
    }
    if (q.pow(x) != ijk)
        return false;

    if (ti.val == E) {
        ti = q;
        ipos = str.length();
        for (; ipos < str.length() * x; ++ipos)
        {
            ti *= Q(str[ipos % str.length()]);
            if (ti == qi)
                break;
        }
        if (ti != qi)
            return false;
    }

    Q tk;
    size_t jpos = str.length() * x - 1;
    for (; jpos > ipos; --jpos)
    {
        tk = Q(str[jpos % str.length()]) * tk;
        if (tk == qk) {
            return true;
        }
    }
    return false;
}

int main()
{
    size_t test_cases;
    std::cin >> test_cases;
    std::string str;
    for (size_t i = 1; i <= test_cases; ++i)
    {
        size_t l, x;
        std::cin >> l >> x >> str;
        std::cout << "Case #" << i << ": " << (solve(str, x) ? "YES" : "NO") << std::endl;
    }
}