#include <iostream>
#include <cassert>
#include <vector>

/* #define DEBUG(x) do { x; } while (false) */

#ifndef DEBUG
#   define DEBUG(x) do { } while (false)
#endif


template<class digit_type>
class Quaternion
{
    public:
        Quaternion<digit_type>() {}
        Quaternion<digit_type>(digit_type a, digit_type b, digit_type c, digit_type d)
            : a(a), b(b), c(c), d(d) {}

    public:
        // a + b*i + c*j + d*k
        digit_type a = 0;
        digit_type b = 0;
        digit_type c = 0;
        digit_type d = 0;

    public:
        /* inline Quaternion<digit_type>& Quaternion<digit_type>::operator*=(Quaternion<digit_type> rhs) */
        /* { */
        /*     assert(this != &rhs); */
        /*     return *this; */
        /* } */

        Quaternion<digit_type> operator-() const {
            Quaternion<digit_type> result;
            result.a = -a;
            result.b = -b;
            result.c = -c;
            result.d = -d;
            return result;
        }
};

template<class digit_type>
inline Quaternion<digit_type> operator*(const Quaternion<digit_type>& x, const Quaternion<digit_type>& y)
{
    Quaternion<digit_type> result;
    result.a = x.a * y.a - x.b * y.b - x.c * y.c - x.d * y.d;
    result.b = x.a * y.b + x.b * y.a + x.c * y.d - x.d * y.c;
    result.c = x.a * y.c - x.b * y.d + x.c * y.a + x.d * y.b;
    result.d = x.a * y.d + x.b * y.c - x.c * y.b + x.d * y.a;
    return result;
}

template<typename digit_type>
inline bool operator==(const Quaternion<digit_type>& x, const Quaternion<digit_type>& y)
{
    return x.a == y.a && x.b == y.b && x.c == y.c && x.d == y.d;
}

template <typename digit_type>
std::ostream& operator<<(std::ostream& os, const Quaternion<digit_type>& x)
{
    return (os << "q(" << x.a << "," << x.b << "," << x.c << "," << x.d << ")");
}


enum class QuaternionUnit { e = 0, i = 1, j = 2, k = 3 };

class SimpleQuaternionTable
{
    public:
        int unit_result[4][4];
        bool sign_result[4][4];

    public:
        SimpleQuaternionTable()
        {
            unit_result[0][0] = 0; sign_result[0][0] = false;
            unit_result[0][1] = 1; sign_result[0][1] = false;
            unit_result[0][2] = 2; sign_result[0][2] = false;
            unit_result[0][3] = 3; sign_result[0][3] = false;
            unit_result[1][0] = 1; sign_result[1][0] = false;
            unit_result[1][1] = 0; sign_result[1][1] = true;
            unit_result[1][2] = 3; sign_result[1][2] = false;
            unit_result[1][3] = 2; sign_result[1][3] = true;
            unit_result[2][0] = 2; sign_result[2][0] = false;
            unit_result[2][1] = 3; sign_result[2][1] = true;
            unit_result[2][2] = 0; sign_result[2][2] = true;
            unit_result[2][3] = 1; sign_result[2][3] = false;
            unit_result[3][0] = 3; sign_result[3][0] = false;
            unit_result[3][1] = 2; sign_result[3][1] = false;
            unit_result[3][2] = 1; sign_result[3][2] = true;
            unit_result[3][3] = 0; sign_result[3][3] = true;
        }
};

const SimpleQuaternionTable quat_table;


struct SimpleQuaternion {
    private:
        SimpleQuaternion(bool negative, int unit) : negative(negative), unit(unit) {}

    public:
        static SimpleQuaternion e() { return SimpleQuaternion(false, 0); }
        static SimpleQuaternion i() { return SimpleQuaternion(false, 1); }
        static SimpleQuaternion j() { return SimpleQuaternion(false, 2); }
        static SimpleQuaternion k() { return SimpleQuaternion(false, 3); }

        static SimpleQuaternion from_char(char c)
        {
            switch(c) {
                case 'e': return e();
                case 'i': return i();
                case 'j': return j();
                case 'k': return k();
                default: assert(false);
            }
        }

        inline SimpleQuaternion& operator*=(SimpleQuaternion rhs)
        {
            assert(this != &rhs);
            assert(0 <= this->unit && this->unit <= 3);
            assert(0 <= rhs.unit && rhs.unit <= 3);
            this->negative = (this->negative != rhs.negative) != quat_table.sign_result[this->unit][rhs.unit];
            this->unit = quat_table.unit_result[this->unit][rhs.unit];
            return *this;
        }

        inline bool operator==(const SimpleQuaternion& rhs) const
        {
            return this->negative == rhs.negative && this->unit == rhs.unit;
        }

        SimpleQuaternion operator-() const {
            return SimpleQuaternion(!this->negative, this->unit);
        }

        std::ostream& output(std::ostream& os) const
        {
            if (negative) os << '-';
            switch(unit) {
                case 0: os << 'e'; break;
                case 1: os << 'i'; break;
                case 2: os << 'j'; break;
                case 3: os << 'k'; break;
                default: assert(false);
            }
            return os;
        }

    private:
        bool negative;
        int unit; // 1 = 1, 2 = i, 3 = j, 4 = k
};


inline SimpleQuaternion operator*(SimpleQuaternion x, const SimpleQuaternion& y)
{
    x *= y;
    return x;
}

inline SimpleQuaternion pow(SimpleQuaternion x, unsigned long long n)
{
    n %= 4; // pow(q, 4) == e for all q
    if (n == 0) { return SimpleQuaternion::e(); }
    if (n == 1) { return x; }
    if (n == 2) { return x*x; }
    if (n == 3) { return x*x*x; }
    assert(false);
}

std::ostream& operator<<(std::ostream& os, const SimpleQuaternion& x)
{
    return x.output(os);
}


typedef SimpleQuaternion quat;


struct split_idx
{
    long long full; // how many full strings
    long long part; // how many chars from one partial string - 1 (i.e. index of last char *in* the string from the border)
};


int main()
{
    const auto e = quat::e();
    const auto i = quat::i();
    const auto j = quat::j();
    const auto k = quat::k();
    assert(e*e == e);
    assert(e*i == i);
    assert(e*j == j);
    assert(e*k == k);
    assert(i*e == i);
    assert(i*i == -e);
    assert(i*j == k);
    assert(i*k == -j);
    assert(j*e == j);
    assert(j*i == -k);
    assert(j*j == -e);
    assert(j*k == i);
    assert(k*e == k);
    assert(k*i == j);
    assert(k*j == -i);
    assert(k*k == -e);

    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {

        int L;
        long long X;

        DEBUG(std::cerr << std::endl);
        DEBUG(std::cerr << std::endl);
        DEBUG(std::cerr << std::endl);
        DEBUG(std::cerr << std::endl);
        DEBUG(std::cerr << std::endl);
        DEBUG(std::cerr << std::endl);


        std::cin >> L >> X;
        DEBUG(std::cerr << "L=" << L << " X=" << X << " S=");

        std::vector<quat> S; // S = the given quaternion string
        quat s = e; // s = the given quaternion string reduced
        S.reserve(L);
        for (int m = 0; m < L; ++m) {
            char c;
            std::cin >> c;
            DEBUG(std::cerr << c);

            auto q = quat::from_char(c);
            S.push_back(q);
            s *= q;
        }
        DEBUG(std::cerr << " s=" << s << std::endl);
        assert((long long)S.size() == L);


        auto check_split = [&](int lX, int l, quat sl, int rX, int r, quat sr) {
            // we have: pow(s,X) = pow(s,lX)*sl * middle * sr*pow(s,rX)
            //                   = i * middle * k
            // thus middle = (-i) * pow(s,X) * (-k) = i * pow(s, X) * k
            // thus middle  = sl*sl*sl*pow(s,lX)*pow(s,lX)*pow(s,lX)*pow(s,X)*pow(s,rX)*pow(s,rX)*pow(s,rX)*sr*sr*sr
            //              = pow(sl,3) * pow(s, 3*lX + X + 3*rX) * pow(sr,3)
            long long mX = X - lX - rX - 1; // full strings in middle part
            assert(mX >= 0);
            if (mX == 0) {
                assert(l + 1 < r);
            }

            /* quat m = pow(sl, 3) * pow(s, 3*lX + X + 3*rX) * pow(sr, 3); */
            quat m = i * pow(s, X) * k;
            DEBUG(std::cerr << "Testing sl=" << sl << " @(" << lX << "," << l << ")  sr=" << sr << " @(" << rX << "," << r << ")  m=" << m << std::endl);
            /* DEBUG(std::cerr << "pow(s, lX)=" << pow(s, lX) << "    pow(s, lX) * sl = " << pow(s, lX) * sl << std::endl); */
            /* DEBUG(std::cerr << "pow(s, rX)=" << pow(s, rX) << "    sr * pow(s, rX) = " << sr * pow(s, rX) << std::endl); */
            assert(pow(s, lX) * sl == i);
            assert(sr * pow(s, rX) == k);
            return (m == j);
        };


        auto find_right_split = [&](int full_used_left, int l, quat sl) {
            long long remX = X - full_used_left; // remaining full strings for middle and right
            quat sr = e;
            for (int r = L-1; r >= 0; --r) {
                if (remX == 1 && l + 1 >= r) {
                    // no more room for middle string
                    break;
                }

                // find right split
                sr = S[r] * sr;

                // Found a possible right split at location r?
                if (sr == k) {
                    if (check_split(full_used_left, l, sl, 0, r, sr)) return true;
                }
                if (remX >= 2 && sr*s == k) {
                    if (check_split(full_used_left, l, sl, 1, r, sr)) return true;
                }
                if (remX >= 3 && sr*s*s == k) {
                    if (check_split(full_used_left, l, sl, 2, r, sr)) return true;
                }
                if (remX >= 4 && sr*s*s*s == k) {
                    if (check_split(full_used_left, l, sl, 3, r, sr)) return true;
                }
            }
            return false;
        };


        auto find_left_split = [&]() {
            quat sl = e;
            for (int l = 0; l < L; ++l) {
                // l == left index
                // find left split
                sl *= S[l];

                // Found a possible left split at location l?
                if (sl == i) {
                    if (find_right_split(0, l, sl)) return true;
                }
                if (X >= 2 && s*sl == i) {
                    if (find_right_split(1, l, sl)) return true;
                }
                if (X >= 3 && s*s*sl == i) {
                    if (find_right_split(2, l, sl)) return true;
                }
                if (X >= 4 && s*s*s*sl == i) {
                    if (find_right_split(3, l, sl)) return true;
                }
            }
            return false;
        };

        bool result = false;

        if (pow(s, X) == i*j*k) {
            result = find_left_split();
        } else {
            DEBUG(std::cerr << "early disproved" << std::endl);
        }
        std::cout << "Case #" << t << ": " << (result ? "YES" : "NO") << '\n';
    }

    return 0;
}
