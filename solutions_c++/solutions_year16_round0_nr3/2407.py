#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#define ll long long

using namespace std;

template <class T>
bool even(const T & n) {
    return (n & 1) == 0;
}

template <class T>
void bisect(T & n) {
    n >>= 1;
}

template <class T>
void redouble (T & n) {
    n <<= 1;
}

template <class T>
bool perfect_square (const T & n) {
    T sq = (T) ceil (sqrt((double) n));
    return sq * sq == n;
}

template <class T>
unsigned bits_in_number (T n) {
    if (n == 0)
        return 1;
    unsigned result = 0;
    while (n) {
        bisect(n);
        ++result;
    }
    return result;
}

template <class T>
bool test_bit (const T & n, unsigned k) {
    return (n & (T(1) << k)) != 0;
}

template <class T>
void mul_mod(T & a, T b, const T & n) {
    a *= b;
    a %= n;
}

template <>
void mul_mod(int & a, int b, const int & n) {
    a = int ((((long long) a) * b) % n);
}

template <>
void mul_mod(unsigned & a, unsigned b, const unsigned & n) {
    a = unsigned ((((unsigned long long) a) * b) % n);
}

template <>
void mul_mod(unsigned long long & a, unsigned long long b, const unsigned long long & n) {
    if (a >= n)
        a %= n;
    if (b >= n)
        b %= n;
    unsigned long long res = 0;
    while (b)
        if (!even(b)) {
            res += a;
            while (res >= n)
                res -= n;
            --b;
        }
        else {
            redouble (a);
            while (a >= n)
                a -= n;
            bisect (b);
        }
    a = res;
}

template <>
void mul_mod(long long & a, long long b, const long long & n) {
    bool neg = false;
    if (a < 0) {
        neg = !neg;
        a = -a;
    }
    if (b < 0) {
        neg = !neg;
        b = -b;
    }
    unsigned long long aa = a;
    mul_mod<unsigned long long> (aa, (unsigned long long) b, (unsigned long long) n);
    a = (long long) aa * (neg ? -1 : 1);
}

template <class T, class T2>
T pow_mod(T a, T2 k, const T & n) {
    T res = 1;
    while (k)
        if (!even(k)) {
            mul_mod(res, a, n);
            --k;
        }
        else {
            mul_mod(a, a, n);
            bisect(k);
        }
    return res;
}

template <class T>
void transform_num (T n, T & p, T & q) {
    T p_res = 0;
    while (even (n)) {
        ++p_res;
        bisect (n);
    }
    p = p_res;
    q = n;
}

template <class T, class T2>
T gcd_1 (const T & a, const T2 & b) {
    return (a == 0) ? b : gcd_1 (b % a, a);
}

template <class T>
T jacobi (T a, T b) {
    if (a == 0)
        return 0;
    if (a == 1)
        return 1;

    if (a < 0)
    if ((b & 2) == 0)
        return jacobi (-a, b);
    else
        return - jacobi (-a, b);

    T e, a1;
    transform_num (a, e, a1);

    T s;
    if (even (e) || (b & 7) == 1 || (b & 7) == 7)
        s = 1;
    else
        s = -1;
    if ((b & 3) == 3 && (a1 & 3) == 3)
        s = -s;
    if (a1 == 1)
        return s;
    return s * jacobi (b % a1, a1);
}

template <class T, class T2>
const vector<T> & get_primes (const T & b, T2 & pi) {
    static vector<T> primes;
    static T counted_b;

    if (counted_b >= b)
        pi = T2 (upper_bound(primes.begin(), primes.end(), b) - primes.begin());
    else {
        if (counted_b == 0) {
            primes.push_back (2);
            counted_b = 2;
        }

        T first = counted_b == 2 ? 3 : primes.back() + 2;
        for (T cur = first; cur <= b; ++++cur) {
            bool cur_is_prime = true;
            for (T div : primes) {
                if (div * div > cur)
                    break;
                if (cur % div == 0) {
                    cur_is_prime = false;
                    break;
                }
            }
            if (cur_is_prime)
                primes.push_back (cur);
        }

        counted_b = b;
        pi = (T2) primes.size();

    }

    return primes;

}

template <class T, class T2>
T2 prime_div_trivial (const T & n, T2 m) {
    if (n == 2 || n == 3)
        return 1;
    if (n < 2)
        return 0;
    if (even(n))
        return 2;

    T2 pi;
    const vector<T2> & primes = get_primes (m, pi);

    for (T2 div : primes) {
        if (div * div > n)
            break;
        if (n % div == 0)
            return div;
    }

    if (n < m * m)
        return 1;
    return 0;

}

template <class T, class T2>
bool miller_rabin (T n, T2 b) {
    if (n == 2)
        return true;
    if (n < 2 || even (n))
        return false;

    if (b < 2)
        b = 2;
    for (T g; (g = gcd_1 (n, b)) != 1; ++b)
        if (n > g)
            return false;

    T n_1 = n;
    --n_1;
    T p, q;
    transform_num (n_1, p, q);

    T rem = pow_mod(T(b), q, n);
    if (rem == 1 || rem == n_1)
        return true;

    for (T i = 1; i < p; i++) {
        mul_mod(rem, rem, n);
        if (rem == n_1)
            return true;
    }

    return false;

}

template <class T, class T2>
bool lucas_selfridge(const T & n, T2 unused) {
    if (n == 2)
        return true;
    if (n < 2 || even (n))
        return false;

    if (perfect_square (n))
        return false;

    T2 dd;
    for (T2 d_abs = 5, d_sign = 1; ; d_sign = -d_sign, ++++d_abs) {
        dd = d_abs * d_sign;
        T g = gcd_1(n, d_abs);
        if (1 < g && g < n)
            return false;
        if (jacobi(T(dd), n) == -1)
            break;
    }

    T2
            p = 1,
            q = (p*p - dd) / 4;

    T n_1 = n;
    ++n_1;
    T s, d;
    transform_num (n_1, s, d);

    T
            u = 1,
            v = p,
            u2m = 1,
            v2m = p,
            qm = q,
            qm2 = q*2,
            qkd = q;
    for (unsigned bit = 1, bits = bits_in_number(d); bit < bits; bit++) {
        mul_mod(u2m, v2m, n);
        mul_mod(v2m, v2m, n);
        while (v2m < qm2)
            v2m += n;
        v2m -= qm2;
        mul_mod(qm, qm, n);
        qm2 = qm;
        redouble (qm2);
        if (test_bit (d, bit)) {
            T t1, t2;
            t1 = u2m;
            mul_mod(t1, v, n);
            t2 = v2m;
            mul_mod(t2, u, n);

            T t3, t4;
            t3 = v2m;
            mul_mod(t3, v, n);
            t4 = u2m;
            mul_mod(t4, u, n);
            mul_mod(t4, (T)dd, n);

            u = t1 + t2;
            if (!even (u))
                u += n;
            bisect (u);
            u %= n;

            v = t3 + t4;
            if (!even (v))
                v += n;
            bisect (v);
            v %= n;
            mul_mod(qkd, qm, n);
        }
    }

    if (u == 0 || v == 0)
        return true;

    T qkd2 = qkd;
    redouble (qkd2);
    for (T2 r = 1; r < s; ++r)
    {
        mul_mod(v, v, n);
        v -= qkd2;
        if (v < 0) v += n;
        if (v < 0) v += n;
        if (v >= n) v -= n;
        if (v >= n) v -= n;
        if (v == 0)
            return true;
        if (r < s-1)
        {
            mul_mod(qkd, qkd, n);
            qkd2 = qkd;
            redouble(qkd2);
        }
    }

    return false;

}

template <class T>
bool baillie_pomerance_selfridge_wagstaff(T n) {
    int div = prime_div_trivial (n, 1000);
    if (div == 1)
        return true;
    if (div > 1)
        return false;

    if (!miller_rabin (n, 2))
        return false;

    return lucas_selfridge (n, 0);
}

template <class T>
bool is_prime(T n) {
    return baillie_pomerance_selfridge_wagstaff(n);
}

long long to_base(unsigned int mask, int base) {
    long long res = 0;
    long long mul = 1;
    while (mask != 0) {
        res = res + (mask & 1) * mul;
        mask = mask >> 1;
        mul = mul * base;
    }
    return res;
}

bool ok(unsigned int mask) {
    for (int i = 2; i <= 10; i++) {
        if (is_prime(to_base(mask, i))) return false;
    }
    return true;
}

void print(unsigned int mask) {
    if (mask == 0) return;
    else {
        print(mask >> 1);
        cout << (mask & 1);
    }
}

long long get_divisor(long long x) {
    if (x % 2 == 0) return 2;
    for (int i = 3; i < x; i = i + 2) {
        if (x % i == 0) return i;
    }
}

int main() {
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;;
    for (int i = 1; i <= t; i++) {
        int n, j;
        cin >> n >> j;
        cout << "Case #" << i << ":\n";
        for (unsigned int mask = 0; mask < (1 << (n - 2)); mask++) {
            unsigned int actual = (mask << 1) + 1 + (1 << (n - 1));
            if (ok(actual)) {
                print(actual);
                cout << " ";
                for (int b = 2; b <= 10; b++) {
                    cout << get_divisor(to_base(actual, b)) << " ";
                }
                cout << "\n";
                j--;
            }
            if (j == 0) break;
        }
    }
    return 0;
}

