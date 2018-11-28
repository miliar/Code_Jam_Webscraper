#include <bits/stdc++.h>

using namespace std;

using namespace std::chrono;

class Timer
{
public:

    high_resolution_clock::time_point start;

    Timer() : start(high_resolution_clock::now()) {
    }

    void reset()
    {
        start = high_resolution_clock::now();
    }

    double getTime() const
    {
        high_resolution_clock::time_point finish = high_resolution_clock::now();
        duration<double> time_span = duration_cast<duration<double>>(finish - start);

        return time_span.count();
    }
};

class BigInteger
{
private:

    static const int base = 1000000000;
    static const int base_digits = 9;

    vector<int> a;
    int sign;

    ///Auxiliary functions
    vector<int> convertBase(const vector<int> &, int, int) const;

    vector<long long> karatsubaMultiplication(const vector<long long> &, const vector<long long> &) const;
    pair<BigInteger, BigInteger> division(const BigInteger &, const BigInteger &) const;

    BigInteger binary_gcd(const BigInteger &, const BigInteger &) const;
    void extented_euclid(BigInteger, BigInteger, BigInteger &, BigInteger &) const;

    bool witness(const BigInteger &, const BigInteger &) const;
    BigInteger pollards_rho(const BigInteger &) const;
    vector<BigInteger> factorization(const BigInteger &, const size_t) const;

    int reverse_bits(const int, const int) const;
    void fft(vector<complex<double>> &, int, int) const;
    vector<complex<double>> convolution(vector<complex<double>> &, vector<complex<double>> &) const;

    BigInteger bruteForceMultiplication(const BigInteger &, const BigInteger &, const int, const int) const;
    BigInteger karatsubaMultiplication(const BigInteger &, const BigInteger &, const int, const int) const;
    BigInteger fftMultiplication(const BigInteger &, const BigInteger &, const int, const int) const;
    BigInteger hybridMultiplication(const BigInteger &, const BigInteger &) const;

public:

    BigInteger();
    BigInteger(long long);
    BigInteger(const BigInteger &);
    BigInteger(const string &);


    BigInteger& operator =  (const BigInteger &);
    BigInteger& operator =  (long long);
    BigInteger& operator =  (const string &);

    BigInteger  operator +  (const BigInteger &) const;
    BigInteger& operator += (const BigInteger &);

    BigInteger  operator -  (const BigInteger &) const;
    BigInteger& operator -= (const BigInteger &);

    BigInteger  operator *  (int) const;
    BigInteger& operator *= (int);

    BigInteger  operator *  (const BigInteger &) const;
    BigInteger& operator *= (const BigInteger &);

    BigInteger  operator /  (int) const;
    BigInteger& operator /= (int);

    BigInteger  operator /  (const BigInteger &) const;
    BigInteger& operator /= (const BigInteger &);

    int         operator %  (int) const;
    BigInteger& operator %= (int);

    BigInteger  operator %  (const BigInteger &) const;
    BigInteger& operator %= (const BigInteger &);

    BigInteger& operator ++ ();
    BigInteger  operator ++ (int);

    BigInteger& operator -- ();
    BigInteger  operator -- (int);

    BigInteger  operator -  () const;


    void trim();
    size_t numberOfDigits() const;


    BigInteger abs() const;

    BigInteger pow(int) const;
    BigInteger pow(const BigInteger &) const;
    BigInteger modPow(int, int) const;
    BigInteger modPow(int, const BigInteger &) const;
    BigInteger modPow(const BigInteger &, const BigInteger &) const;

    BigInteger sqrt(int) const;

    BigInteger gcd(const BigInteger &) const;
    BigInteger lcm(const BigInteger &) const;
    BigInteger modInverse(const BigInteger &) const;
    bool isProbablePrime(const int) const;
    BigInteger nextProbablePrime(const size_t) const;
    BigInteger getProperDivisor() const;
    vector<BigInteger> factorize(const size_t) const;


    bool operator <  (const BigInteger &) const;
    bool operator >  (const BigInteger &) const;
    bool operator <= (const BigInteger &) const;
    bool operator >= (const BigInteger &) const;
    bool operator == (const BigInteger &) const;
    bool operator != (const BigInteger &) const;


    ///Java-like functions
    BigInteger add(const BigInteger &) const;
    BigInteger subtract(const BigInteger &) const;

    int compareTo(const BigInteger &) const;
    bool equals(const BigInteger &) const;

    BigInteger multiply(int) const;
    BigInteger multiply(const BigInteger &) const;

    BigInteger divide(int) const;
    BigInteger divide(const BigInteger &) const;
    pair<BigInteger, BigInteger> divideAndRemainder(const BigInteger &) const;
    int mod(int) const;
    BigInteger mod(const BigInteger &) const;

    bool isZero() const;
    int signum() const;
    unsigned int hashCode() const;

    static BigInteger randomBigInteger(const size_t);
    static BigInteger valueOf(long long);
    static BigInteger ONE();
    static BigInteger TEN();
    static BigInteger ZERO();

    string toString() const;
    long long toLongLong() const;


    ///Input/Output operators ---------------------------------------------------------
    friend istream& operator >> (istream &stream, BigInteger &B)
    {
        string s;
        stream >> s;

        B = BigInteger(s);

        return stream;
    }

    friend ostream& operator << (ostream &stream, const BigInteger &B)
    {
        if (B.sign == -1)
            stream << '-';

        stream << (B.a.empty() ? 0 : B.a.back());

        for (int i = (int)B.a.size() - 2; i >= 0; i--)
            stream << setw(base_digits) << setfill('0') << B.a[i];

        return stream;
    }
    ///----------------------------------------------------------------------------------
};

///Constructors --------------------------------------------------------------------------------

BigInteger::BigInteger() : a(), sign()
{
    this->sign = 1;
    this->a.clear();
}

BigInteger::BigInteger(long long value) : a(), sign()
{
    *this = value;

    this->trim();
}

BigInteger::BigInteger(const BigInteger &BI): a(), sign()
{
    this->sign = BI.sign;
    this->a = BI.a;

    this->trim();
}

BigInteger::BigInteger(const string &s) : a(), sign()
{
    this->sign = 1;
    this->a.clear();

    int cursor = 0;

    while (cursor < (int)s.size() && (s[cursor] == '-' || s[cursor] == '+'))
    {
        if (s[cursor] == '-')
            this->sign = -1;

        cursor++;
    }

    for (int i = (int)s.size() - 1; i >= cursor; i -= base_digits)
    {
        int x = 0;

        for (int j = max(cursor, i - base_digits + 1); j <= i; ++j)
            x = x * 10 + (s[j] - '0');

        this->a.push_back(x);
    }

    this->trim();
}

///Constructors --------------------------------------------------------------------------------

BigInteger& BigInteger::operator = (const BigInteger &BI)
{
    this->sign = BI.sign;
    this->a = BI.a;

    this->trim();

    return *this;
}

BigInteger& BigInteger::operator = (long long value)
{
    this->sign = 1;
    this->a.clear();

    if (value < 0)
    {
        this->sign = -1;
        value = -value;
    }

    do
    {
        this->a.push_back(value % base);
        value /= base;

    } while (value > 0);

    this->trim();

    return *this;
}

BigInteger& BigInteger::operator = (const string &s)
{
    *this = BigInteger(s);

    return *this;
}

BigInteger BigInteger::operator + (const BigInteger &B) const
{
    if (this->sign == B.sign)
    {
        BigInteger solution = B;

        int maximLg = (int)max(this->a.size(), B.a.size());

        for (int i = 0, carry = 0; i < maximLg || carry; ++i)
        {
            if (i == (int)solution.a.size())
                solution.a.push_back(0);

            long long current = solution.a[i];

            current += carry;

            if (i < (int)this->a.size())
                current += this->a[i];

            carry = (current >= base);

            if (carry)
                current -= base;

            solution.a[i] = current;
        }

        return solution;
    }
    else
    {
        return *this - (-B);
    }
}

BigInteger& BigInteger::operator += (const BigInteger &B)
{
    *this = *this + B;

    return *this;
}

BigInteger BigInteger::operator - (const BigInteger &B) const
{
    if (this->sign == B.sign)
    {
        if (this->abs() >= B.abs())
        {
            BigInteger solution = *this;

            for (int i = 0, carry = 0; i < (int)B.a.size() || carry; ++i)
            {
                long long current = solution.a[i];

                current -= carry;

                if (i < (int)B.a.size())
                    current -= B.a[i];

                carry = (current < 0);

                if (carry)
                    current += base;

                solution.a[i] = current;
            }

            solution.trim();

            return solution;
        }
        else
        {
            return -(B - *this);
        }
    }
    else
    {
        return *this + (-B);
    }
}

BigInteger& BigInteger::operator -= (const BigInteger &B)
{
    *this = *this - B;

    return *this;
}

BigInteger BigInteger::operator * (int value) const
{
    BigInteger solution = *this;

    if (value < 0)
    {
        solution.sign = -solution.sign;
        value = -value;
    }

    for (int i = 0, carry = 0; i < (int)solution.a.size() || carry; ++i)
    {
        if (i == (int)solution.a.size())
            solution.a.push_back(0);

        long long current = (1LL * solution.a[i] * value) + 1LL * carry;
        carry = current / base;
        solution.a[i] = current % base;
    }

    solution.trim();

    return solution;
}

BigInteger& BigInteger::operator *= (int value)
{
    *this = *this * value;

    return *this;
}

BigInteger BigInteger::operator * (const BigInteger &B) const
{
    return hybridMultiplication(*this, B);
}

BigInteger& BigInteger::operator *= (const BigInteger &B)
{
    *this = *this * B;

    return *this;
}

BigInteger BigInteger::operator / (int value) const
{
    BigInteger solution = *this;

    if (value < 0)
    {
        solution.sign = -solution.sign;
        value = -value;
    }

    for (int i = (int)solution.a.size() - 1, rem = 0; i >= 0; i--)
    {
        long long current = 1LL * rem * base + 1LL * solution.a[i];
        solution.a[i] = (current / value);
        rem = (current % value);
    }

    solution.trim();

    return solution;
}

BigInteger& BigInteger::operator /= (int value)
{
    *this = *this / value;

    return *this;
}

BigInteger BigInteger::operator / (const BigInteger &B) const
{
    return division(*this, B).first;
}

BigInteger& BigInteger::operator /= (const BigInteger &B)
{
    *this = *this / B;

    return *this;
}

int BigInteger::operator % (int value) const
{
    if (value < 0)
        value = -value;

    int rem = 0;

    for (int i = (int)this->a.size() - 1; i >= 0; i--)
        rem = (1LL * rem * base + 1LL * this->a[i]) % value;

    return rem * this->sign;
}

BigInteger& BigInteger::operator %= (int value)
{
    *this = *this % value;

    return *this;
}

BigInteger BigInteger::operator % (const BigInteger &B) const
{
    return division(*this, B).second;
}

BigInteger& BigInteger::operator %= (const BigInteger &B)
{
    *this = *this % B;

    return *this;
}

BigInteger& BigInteger::operator ++ () ///prefix
{
    *this = *this + 1;

    return *this;
}

BigInteger BigInteger::operator ++ (int) ///postfix
{
    BigInteger solution = *this;
    ++(*this);

    return solution;
}

BigInteger& BigInteger::operator -- () ///prefix
{
    *this = *this - 1;

    return *this;
}

BigInteger BigInteger::operator -- (int) ///postfix
{
    BigInteger solution = *this;
    --(*this);

    return solution;
}

BigInteger BigInteger::operator - () const
{
    BigInteger solution = *this;
    solution.sign = -solution.sign;

    return solution;
}

void BigInteger::trim()
{
    while (this->a.size() && this->a.back() == 0)
        this->a.pop_back();
}

size_t BigInteger::numberOfDigits() const
{
    if (this->a.empty() == true)
        return 1; ///*this = 0

    size_t number = base_digits * (this->a.size() - 1);

    int tmp = this->a.back();

    while (tmp)
    {
        number++;
        tmp /= 10;
    }

    return number;
}

BigInteger BigInteger::abs() const
{
    BigInteger solution = *this;
    solution.sign = 1;

    return solution;
}

BigInteger BigInteger::pow(int exponent) const
{
    BigInteger solution = 1;
    BigInteger A = *this;

    while (exponent > 0)
    {
        if (exponent & 1)
            solution *= A;

        A *= A;
        exponent >>= 1;
    }

    return solution;
}

BigInteger BigInteger::pow(const BigInteger &exponent) const
{
    BigInteger solution = 1;
    BigInteger A = *this;
    BigInteger p = exponent;

    while (p.isZero() == false)
    {
        if (p % 2 == 1)
            solution *= A;

        A *= A;
        p /= 2;
    }

    return solution;
}

BigInteger BigInteger::modPow(int exponent, int MOD) const
{
    BigInteger solution = 1;
    BigInteger A = *this;

    while (exponent > 0)
    {
        if (exponent & 1)
            solution = (solution * A) % MOD;

        A = (A * A) % MOD;
        exponent >>= 1;
    }

    return solution;
}

BigInteger BigInteger::modPow(int exponent, const BigInteger &MOD) const
{
    BigInteger solution = 1;
    BigInteger A = *this;

    while (exponent > 0)
    {
        if (exponent & 1)
            solution = (solution * A) % MOD;

        A = (A * A) % MOD;
        exponent >>= 1;
    }

    return solution;
}

BigInteger BigInteger::modPow(const BigInteger &exponent, const BigInteger &MOD) const
{
    BigInteger solution = 1;
    BigInteger A = *this;
    BigInteger p = exponent;

    while (p.isZero() == false)
    {
        if (p % 2 == 1)
            solution = (solution * A) % MOD;

        A = (A * A) % MOD;
        p /= 2;
    }

    return solution;
}

BigInteger BigInteger::sqrt(int order) const
{
    assert(order >= 1);

    BigInteger T = 10;
    BigInteger l = T.pow(max(0, (int)this->numberOfDigits() / order - 1));
    BigInteger r = T.pow((int)this->numberOfDigits() / order + 1);
    BigInteger m, tmp, solution;

    while (l <= r)
    {
        m = (l + r) / 2;
        tmp = m.pow(order);

        if (tmp <= *this)
        {
            solution = m;
            l = m + 1;
        }
        else
        {
            r = m - 1;
        }
    }

    return solution;
}

BigInteger BigInteger::gcd(const BigInteger &_B) const
{
    BigInteger A = *this;
    BigInteger B = _B;

    return binary_gcd(A, B);
}

BigInteger BigInteger::lcm(const BigInteger &B) const
{
    return *this * B / this->gcd(B);
}

BigInteger BigInteger::modInverse(const BigInteger &N) const
{
    assert(this->gcd(N) == BigInteger(1));

    BigInteger x, y;
    extented_euclid(*this, N, x, y);

    if (x <= BigInteger(0))
    {
        x = N - (x.abs() % N);
    }

    return x;
}

bool BigInteger::isProbablePrime(const int numberOfBases) const
{
    int primes[] = { 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,
                     61,67,71,73,79,83,89,97,101,103,107,109,113,127,
                     131,137,139,149,151,157,163,167,173,179,181,191,
                     193,197,199,211,223,227,229,233,239,241,251,257,
                     263,269,271
                    }; ///58 prime numbers

    if (*this == 1)
        return false;

    if (*this != 2 && *this % 2 == 0)
        return false;

    for (int i = 0; i < min(58, numberOfBases); ++i)
    {
        if (*this == primes[i])
            return true;
    }

    for (int i = 0; i < min(58, numberOfBases); ++i)
    {
        if (witness(primes[i], *this))
            return false;
    }

    return true;
}

BigInteger BigInteger::nextProbablePrime(const size_t numberOfBases) const
{
    BigInteger solution = *this + 1;

    while (solution.isProbablePrime(numberOfBases) == false)
        solution++;

    return solution;
}

Timer timer;

BigInteger BigInteger::getProperDivisor() const
{
    if (timer.getTime() > 1.0)
        return 0;

    BigInteger divisor;

    do
    {
        divisor = pollards_rho(*this);

    } while (divisor == *this);

    return divisor;
}

vector<BigInteger> BigInteger::factorize(const size_t numberOfBases) const
{
    vector<BigInteger> V = factorization(*this, numberOfBases);
    std::sort(V.begin(), V.end());

    return V;
}

///Auxilary functions--------------------------------------------------

vector<int> BigInteger::convertBase(const vector<int> &A, int oldBase, int newBase) const ///conversion from 10^oldBase to 10^newBase
{
    vector<long long> powers(max(oldBase, newBase) + 1, 0);

    powers[0] = 1;

    for (int i = 1; i < (int)powers.size(); ++i)
        powers[i] = powers[i - 1] * 10LL;

    vector<int> solution;

    long long current = 0;
    int current_size = 0;

    for (int i = 0; i < (int)A.size(); ++i)
    {
        current += A[i] * powers[current_size];
        current_size += oldBase;

        while (current_size >= newBase)
        {
            solution.push_back((int)(current % powers[newBase]));
            current /= powers[newBase];
            current_size -= newBase;
        }
    }

    solution.push_back((int)current);

    while (solution.empty() == false && solution.back() == 0)
        solution.pop_back();

    return solution;
}

vector<long long> BigInteger::karatsubaMultiplication(const vector<long long> &A, const vector<long long> &B) const
{
    const size_t N = A.size();
    vector<long long> solution(2 * N, 0);

    if (N <= 32)
    {
        for (size_t i = 0; i < N; ++i)
            for (size_t j = 0; j < N; ++j)
                solution[i + j] += A[i] * B[j];

        return solution;
    }

    size_t p = N / 2;

    vector<long long> a1(A.begin(), A.begin() + p);
    vector<long long> a2(A.begin() + p, A.end());
    vector<long long> b1(B.begin(), B.begin() + p);
    vector<long long> b2(B.begin() + p, B.end());

    vector<long long> a1b1 = karatsubaMultiplication(a1, b1);
    vector<long long> a2b2 = karatsubaMultiplication(a2, b2);

    for (size_t i = 0; i < p; ++i)
    {
        a2[i] += a1[i];
        b2[i] += b1[i];
    }

    vector<long long> tmp = karatsubaMultiplication(a2, b2);

    for (size_t i = 0; i < N; ++i)
    {
        tmp[i] -= a1b1[i];
        tmp[i] -= a2b2[i];

        solution[i + p] += tmp[i];
        solution[i] += a1b1[i];
        solution[i + N] += a2b2[i];
    }

    return solution;
}

pair<BigInteger, BigInteger> BigInteger::division(const BigInteger &X, const BigInteger &Y) const
{
    if (X < Y)
    {
        return make_pair(0, X);
    }

    if (X == Y)
    {
        return make_pair(1, 0);
    }

    int norm = base / (Y.a.back() + 1);

    BigInteger A = X.abs() * norm;
    BigInteger B = Y.abs() * norm;

    BigInteger q, r;
    q.a.resize(A.a.size());

    for (int i = (int)A.a.size() - 1; i >= 0; i--)
    {
        r = r * base + A.a[i];

        int s1, s2;

        if (r.a.size() <= B.a.size())
            s1 = 0;
        else
            s1 = r.a[B.a.size()];

        if (r.a.size() <= B.a.size() - 1)
            s2 = 0;
        else
            s2 = r.a[B.a.size() - 1];

        int digit = (1LL * base * s1 + 1LL * s2) / B.a.back();

        r -= B * digit;

        while (r < 0)
        {
            r += B;
            digit--;
        }

        q.a[i] = digit;
    }

    q.sign = X.sign * Y.sign;
    r.sign = X.sign;

    q.trim();
    r.trim();

    return make_pair(q, r / norm);
}

BigInteger BigInteger::binary_gcd(const BigInteger &A, const BigInteger &B) const
{
    if (A.isZero())
        return B;

    if (B.isZero())
        return A;

    if (A == B)
        return A;

    if (A % 2 == 0)
    {
        if (B % 2 == 1)
        {
            return binary_gcd(A / 2, B);
        }
        else
        {
            return binary_gcd(A / 2, B / 2) * 2;
        }
    }
    else
    {
        if (B % 2 == 0)
        {
            return binary_gcd(A, B / 2);
        }
    }

    if (A > B)
    {
        return binary_gcd((A - B) / 2, B);
    }
    else
    {
        return binary_gcd((B - A) / 2, A);
    }
}

void BigInteger::extented_euclid(BigInteger A, BigInteger B, BigInteger &x, BigInteger &y) const
{
    if (B.isZero())
    {
        x = 1;
        y = 0;
    }
    else
    {
        BigInteger x0, y0;

        extented_euclid(B, A % B, x0, y0);

        x = y0;
        y = x0 - (A / B) * y0;
    }
}

bool BigInteger::witness(const BigInteger &primeBase, const BigInteger &N) const
{
    BigInteger tmp = N - 1;
    int t = 0;

    while (tmp % 2 == 0)
    {
        t++;
        tmp /= 2;
    }

    BigInteger x = primeBase.modPow(tmp, N);

    if (x == 1 || x == N - 1)
        return false;

    t--;

    while (t > 0)
    {
        x = (x * x) % N;

        if (x == N - 1)
            return false;

        t--;
    }

    return true;
}

BigInteger BigInteger::pollards_rho(const BigInteger &N) const ///returns a proper divisor of N or N (if it fails!)
{
    if (N % 2 == 0)
        return 2;

    BigInteger A = 1 + rand() % 1000000000000000000LL;
    BigInteger C = 1 + rand() % 1000000000000000000LL;

    BigInteger X = A;
    BigInteger Y = A;
    BigInteger divisor;

    do
    {
        X = (X * X + C) % N;

        Y = (Y * Y + C) % N;
        Y = (Y * Y + C) % N;

        divisor = X.subtract(Y).abs().gcd(N); /// gcd(abs(x - y), n);

    } while (divisor == 1);

    return divisor;
}

vector<BigInteger> BigInteger::factorization(const BigInteger &N, const size_t numberOfBases) const
{
    if (N == 1)
        return vector<BigInteger>();

    if (N.isProbablePrime(numberOfBases))
    {
        vector<BigInteger> V = {N};
        return V;
    }

    BigInteger divisor = N.getProperDivisor();

    vector<BigInteger> A = factorization(divisor, numberOfBases);
    vector<BigInteger> B = factorization(N / divisor, numberOfBases);

    for (size_t i = 0; i < B.size(); ++i)
        A.push_back(B[i]);

    return A;
}

int BigInteger::reverse_bits(const int x, const int EXP) const
{
    int rev_x = 0;

    for (int i = 0; i < EXP; ++i)
    {
        bool bit = x & (1 << i);

        rev_x <<= 1;
        rev_x |= bit;
    }

    return rev_x;
}

void BigInteger::fft(vector<complex<double>> &A, int EXP, int inverse) const
{
    const int N = A.size();

    for (int i = 0; i < N; ++i)
    {
        int j = reverse_bits(i, EXP);

        if (i < j)
            swap(A[i], A[j]);
    }

    for (int length = 2; length <= N; length *= 2)
    {
        complex<double> root = polar(1.0, inverse * 2.0 * M_PI / length);

        for (int start = 0; start < N; start += length)
        {
            complex<double> wk = 1.0;

            for (int i = 0; i < length / 2; ++i)
            {
                complex<double> u = A[start + i];
                complex<double> v = A[start + i + length / 2] * wk;

                A[start + i] = u + v;
                A[start + i + length / 2] = u - v;

                wk *= root;
            }
        }
    }

    if (inverse == -1)
    {
        for (int i = 0; i < N; ++i)
            A[i] /= N;
    }
}

vector<complex<double>> BigInteger::convolution(vector<complex<double>> &A, vector<complex<double>> &B) const
{
    int N = A.size();
    int M = B.size();

    int EXP = 0;

    while ((1 << EXP) < 2 * max(N, M))
        EXP++;

    int length = 1 << EXP;

    ///padding
    for (int i = N; i < length; ++i)
        A.push_back(0);

    for (int i = M; i < length; ++i)
        B.push_back(0);

    fft(A, EXP, 1);
    fft(B, EXP, 1);

    vector<complex<double>> C(length);

    for (int i = 0; i < length; ++i)
        C[i] = A[i] * B[i];

    fft(C, EXP, -1);

    return C;
}

BigInteger BigInteger::bruteForceMultiplication(const BigInteger &A, const BigInteger &B, const int newBase, const int newBaseDigits) const
{
    vector<int> a5 = convertBase(A.a, base_digits, newBaseDigits);
    vector<int> b5 = convertBase(B.a, base_digits, newBaseDigits);

    vector<unsigned long long> x(a5.begin(), a5.end());
    vector<unsigned long long> y(b5.begin(), b5.end());

    vector<unsigned long long> c(x.size() + y.size(), 0);

    for (size_t i = 0; i < x.size(); ++i)
        for (size_t j = 0; j < y.size(); ++j)
            c[i + j] += x[i] * y[j];

    BigInteger solution;
    solution.a.clear();
    solution.sign = A.sign * B.sign;

    unsigned long long carry = 0;

    for (int i = 0; i < (int)c.size(); ++i)
    {
        unsigned long long current = c[i] + carry;
        solution.a.push_back(current % newBase);
        carry = (current / newBase);
    }

    solution.a = convertBase(solution.a, newBaseDigits, base_digits);
    solution.trim();

    return solution;
}

BigInteger BigInteger::karatsubaMultiplication(const BigInteger &A, const BigInteger &B, const int newBase, const int newBaseDigits) const
{
    vector<int> a5 = convertBase(A.a, base_digits, newBaseDigits);
    vector<int> b5 = convertBase(B.a, base_digits, newBaseDigits);

    vector<long long> x(a5.begin(), a5.end());
    vector<long long> y(b5.begin(), b5.end());

    while (x.size() < y.size()) x.push_back(0);
    while (y.size() < x.size()) y.push_back(0);

    while (x.size() & (x.size() - 1))
    {
        x.push_back(0);
        y.push_back(0);
    }

    vector<long long> c = karatsubaMultiplication(x, y);

    BigInteger solution;
    solution.a.clear();
    solution.sign = A.sign * B.sign;

    for (int i = 0, carry = 0; i < (int)c.size(); ++i)
    {
        long long current = c[i] + carry;
        solution.a.push_back(current % newBase);
        carry = (current / newBase);
    }

    solution.a = convertBase(solution.a, newBaseDigits, base_digits);
    solution.trim();

    return solution;
}

BigInteger BigInteger::fftMultiplication(const BigInteger &X, const BigInteger &Y, const int newBase, const int newBaseDigits) const
{
    vector<int> Xtr = convertBase(X.a, base_digits, newBaseDigits);
    vector<int> Ytr = convertBase(Y.a, base_digits, newBaseDigits);

    int N = Xtr.size();
    int M = Ytr.size();

    vector<complex<double>> A(N);
    vector<complex<double>> B(M);

    for (int i = 0; i < N; ++i)
        A[i] = Xtr[i];

    for (int i = 0; i < M; ++i)
        B[i] = Ytr[i];

    vector<complex<double>> C = convolution(A, B);
    vector<int> result;

    int carry = 0;

    for (size_t i = 0; i < C.size(); ++i)
    {
        int c = (int)(C[i].real() + 0.5);

        c += carry;
        carry = c / newBase;
        c %= newBase;

        result.push_back(c);
    }

    BigInteger solution;
    solution.sign = X.sign * Y.sign;
    solution.a = convertBase(result, newBaseDigits, base_digits);

    return solution;
}

BigInteger BigInteger::hybridMultiplication(const BigInteger &A, const BigInteger &B) const
{
    const int CUT_OFF_KARATSUBA = 19000 * 19000;
    const int CUT_OFF_FFT       = 81900;
    ///----------------------------------------------------------------------

    int nrA = this->numberOfDigits();
    int nrB = B.numberOfDigits();

    if (1LL * nrA * nrB <= 1LL * CUT_OFF_KARATSUBA)
        return bruteForceMultiplication(A, B, 100000000, 8);

    if (max(nrA, nrB) <= CUT_OFF_FFT)
    {
        if (max(nrA, nrB) <= 48000)
            return karatsubaMultiplication(A, B, 1000000, 6);
        else
            return karatsubaMultiplication(A, B, 100000, 5);
    }
    else
    {
        if (max(nrA, nrB) <= 1700000)
            return fftMultiplication(A, B, 100, 2);
        else
            return fftMultiplication(A, B, 10, 1);
    }
}

///Comparision operators --------------------------------------------------------------------------

bool BigInteger::operator < (const BigInteger &B) const
{
    if (this->sign != B.sign)
        return this->sign < B.sign;

    if (this->a.size() != B.a.size())
        return this->a.size() * this->sign < B.a.size() * B.sign;

    for (int i = (int)this->a.size() - 1; i >= 0; i--)
        if (this->a[i] != B.a[i])
            return this->a[i] * this->sign < B.a[i] * B.sign;

    return false;
}

bool BigInteger::operator > (const BigInteger &B) const
{
    return B < *this;
}

bool BigInteger::operator <= (const BigInteger &B) const
{
    return !(B < *this);
}

bool BigInteger::operator >= (const BigInteger &B) const
{
    return !(*this < B);
}

bool BigInteger::operator == (const BigInteger &B) const
{
    return !(*this < B) && !(B < *this);
}

bool BigInteger::operator != (const BigInteger &B) const
{
    return (*this < B) || (B < *this);
}

///Comparision operators --------------------------------------------------------------------------

///Java-like functions--------------------------------------------------------------------------------------

/// 1 ----------------------------------------------------------------------------------
BigInteger BigInteger::add(const BigInteger &B) const
{
    return *this + B;
}

BigInteger BigInteger::subtract(const BigInteger &B) const
{
    return *this - B;
}
///------------------------------------------------------------------------------------

/// 2 ---------------------------------------------------------------------------------
int BigInteger::compareTo(const BigInteger &B) const
{
    if (*this < B)
        return -1;

    if (*this > B)
        return +1;

    return 0;
}

bool BigInteger::equals(const BigInteger &B) const
{
    return *this == B;
}
///------------------------------------------------------------------------------------

/// 3 ---------------------------------------------------------------------------------
BigInteger BigInteger::multiply(int value) const
{
    return *this * value;
}

BigInteger BigInteger::multiply(const BigInteger &B) const
{
    return *this * B;
}
///------------------------------------------------------------------------------------

/// 4 ---------------------------------------------------------------------------------
BigInteger BigInteger::divide(int value) const
{
    return *this / value;
}

BigInteger BigInteger::divide(const BigInteger &B) const
{
    return *this / B;
}

pair<BigInteger, BigInteger> BigInteger::divideAndRemainder(const BigInteger &B) const
{
    return division(*this, B);
}

int BigInteger::mod(int value) const
{
    return *this % value;
}

BigInteger BigInteger::mod(const BigInteger &B) const
{
    return *this % B;
}
/// -----------------------------------------------------------------------------------

/// 5 ---------------------------------------------------------------------------------
bool BigInteger::isZero() const
{
    if (this->a.empty() == true)
        return true;

    if ((int)this->a.size() == 1 && this->a.back() == 0)
        return true;
    else
        return false;
}

int BigInteger::signum() const
{
    if (*this < 0)
        return -1;

    if (*this > 0)
        return +1;

    return 0;
}

unsigned int BigInteger::hashCode() const
{
    unsigned int hashC = 5381;

    for (int i = (int)this->a.size() - 1; i >= 0; --i)
    {
        hashC = ((hashC << 5) + hashC) + this->a[i];
    }

    if (this->sign == -1)
        hashC *= 2654435761U;

    return hashC;
}

BigInteger BigInteger::randomBigInteger(const size_t numDigits)
{
    string s;
    s.push_back(char('1' + rand() % 9));

    for (size_t i = 1; i < numDigits; ++i)
        s.push_back(char('0' + rand() % 10));

    return BigInteger(s);
}

BigInteger BigInteger::valueOf(long long value)
{
    return BigInteger(value);
}

BigInteger ONE()
{
    return BigInteger(1);
}

BigInteger TEN()
{
    return BigInteger(10);
}

BigInteger ZERO()
{
    return BigInteger(0);
}

///------------------------------------------------------------------------------------

/// 6 ---------------------------------------------------------------------------------
string BigInteger::toString() const
{
    string solution;

    if (this->sign == -1)
        solution.push_back('-');

    if (this->a.empty() == true)
    {
        solution.push_back('0');
    }
    else
    {
        string res;
        int tmp = this->a.back();

        while (tmp)
        {
            res.push_back(char('0' + tmp % 10));
            tmp /= 10;
        }

        reverse(res.begin(), res.end());
        solution += res;

        for (int i = (int)this->a.size() - 2; i >= 0; i--)
        {
            res.clear();
            tmp = this->a[i];

            while (tmp)
            {
                res.push_back(char('0' + tmp % 10));
                tmp /= 10;
            }

            reverse(res.begin(), res.end());

            for (int j = 0; j < base_digits - (int)res.size(); j++)
                solution.push_back('0');

            solution += res;
        }
    }

    return solution;
}

long long BigInteger::toLongLong() const
{
    long long solution = 0;

    for (int i = (int)this->a.size() - 1; i >= 0; i--)
        solution = solution * base + this->a[i];

    return solution * this->sign;
}
///------------------------------------------------------------------------------------

///Java-like functions--------------------------------------------------------------------------------------


BigInteger getNumber(long long mask, int numbOfBits, int base)
{
    BigInteger solution = 0;

    for (int i = numbOfBits - 1; i >= 0; --i)
    {
        solution = solution * base;

        if ((mask >> i) & 1)
        {
            solution++;
        }
    }

    return solution;
}

string nrToBinString(BigInteger nr)
{
    string bin_rep;

    do
    {
        bin_rep.push_back(char('0' + nr % 2));
        nr /= 2;

    } while (nr > 0);

    reverse(bin_rep.begin(), bin_rep.end());

    return bin_rep;
}

void checkFile()
{
    ifstream in("data.out");

    string s;
    set<string> Set;

    while (in >> s)
    {
        Set.insert(s);
    }

    cout << Set.size() << endl;
}

BigInteger getFactor(istream &stream)
{
    string s;
    stream >> s;

    BigInteger d;
    stream >> d;

    return d;
}

#include <cstring>

int main()
{
    /*
    const int MAX_N = 32;
    unordered_set<long long int> goodNumbers;

    long long stateLeft = 0;
    long long stateRight = (1LL << 30);

    int c = 0;

    while (stateLeft <= stateRight)
    {
        bool valid = true;

        c ^= 1;

        long long int mask = 1 | (1LL << 31);

        if (c)
        {
            mask |= (stateLeft << 1);
            stateLeft++;
        }
        else
        {
            mask |= (stateRight << 1);
            stateRight--;
        }

        if ((mask & 1) == 0 || ((mask >> (31)) & 1) == 0)
        {
            cerr << "ERRR" << endl;
            return 0;
        }

        cout << "DA " << stateLeft << " " << stateRight << " " << mask << endl;

        for (int b = 2; b <= 10 && valid; ++b)
        {
            BigInteger nr = getNumber(mask, MAX_N, b);

            if (nr == -1 || nr == 1 || nr.isProbablePrime(20))
                valid = false;
        }

        cout << "NU" << endl;

        if (valid && goodNumbers.count(mask) == 0)
        {
            goodNumbers.insert(mask);

            ofstream out("data.out", ios::app);
            out << mask << '\n';
        }

        if (goodNumbers.size() >= 500)
            break;

      //  cout << stateLeft << " " << stateRight << " " << goodNumbers.size() << endl;
    }
    */
/*
    ifstream ok("data.out");
    ofstream out("solution.out");

    const int MAX_J = 500;

    ///out << "Case #1:\n";

    srand(time(nullptr));

    for (int i = 0; i < MAX_J; ++i)
    {
        long long vect;
        ok >> vect;

        string s = nrToBinString(BigInteger(vect));

        out << s << " ";

        for (int base = 2; base <= 10; ++base)
        {
            BigInteger number = getNumber(vect, 32, base);
            assert(number.isProbablePrime(10) == false);

            out << number;

            if (base < 10)
                out << " ";
        }

        out << "\n";

        cerr << i << endl;
    }

    ok.close();
    out.close();
    */

    /*
    ofstream out("solution.out");

    ifstream numbs("numbers.out");

    for (int i = 0; i < 500; ++i)
    {
        string s;
        numbs >> s;

        out << s << " ";

        for (int j = 2; j <= 10; ++j)
        {
            BigInteger number;
            numbs >> number;

            string str = number.toString();

            char sir[1000];

            strcpy(sir, "factor ");
            int n = 7;

            for (char c : str)
                sir[ n++ ] = c;

            sir[n] = '\0';

            strcat(sir, " >> fact.in");

            system(sir);

            ifstream get("fact.in");

            out << getFactor(get);

            get.close();
            system("rm fact.in");

            if (j < 10)
                out << " ";
        }

        out << endl;
    }
    */

    ifstream in("solution.out");

    string test;
    assert(getline(in, test));

    for (int i = 0; i < 500; ++i)
    {
        string s;
        assert(in >> s);

        assert(s[0] == '1');
        assert(s[s.size() - 1] == '1');

        for (int base = 2; base <= 10; ++base)
        {
            BigInteger number = 0;

            for (char c : s)
            {
                number = number * base;

                if (c == '1')
                    number++;
            }

            assert(number.isProbablePrime(30) == false);

            BigInteger d;
            assert(in >> d);

            assert(number % d == 0);
        }
    }

    return 0;
}
