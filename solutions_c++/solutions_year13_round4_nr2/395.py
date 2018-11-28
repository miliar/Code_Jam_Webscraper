#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>
using namespace std;

#define rep(i, n)       rep2 (i, 0, n)
#define rep2(i, m, n)   for  (int i = (int)(m); i < (int)(n); ++i)

typedef long long ll;

class bigint {
private:
    static const int BASE = 100000000, LEN = 8;
    std::vector<int> a;
    bigint& normalize();
public:
    bigint(int x = 0);
    bigint(const std::string& s);
    bigint& operator = (const bigint& x);
    bigint& operator = (int x);
    bigint& operator = (const std::string& s);
    bool operator < (const bigint& x) const;
    bool operator > (const bigint& x) const;
    bool operator <= (const bigint& x) const;
    bool operator >= (const bigint& x) const;
    bool operator != (const bigint& x) const;
    bool operator == (const bigint& x) const;
    bigint& operator += (const bigint& x);
    bigint& operator -= (const bigint& x);
    bigint& operator *= (const bigint& x);
    bigint operator + (const bigint& x) const;
    bigint operator - (const bigint& x) const;
    bigint operator * (const bigint& x) const;
    friend std::istream& operator >> (std::ostream& is, bigint& x);
    friend std::ostream& operator << (std::ostream& os, const bigint& x);
};
bigint& bigint::normalize() {
    int i = a.size() - 1;
    while (i >= 0 && a[i] == 0) --i;
    a.resize(i + 1);
    return *this;
}
bigint::bigint(int x) {
    for (; x > 0; x /= BASE) a.push_back(x % BASE);
}
bigint::bigint(const std::string& s) {
    int p = 0;
    for (int i = s.size() - 1, v = BASE; i >= p; --i, v *= 10) {
        int x = s[i] - '0';
        if (x < 0 || 9 < x) {
            std::cerr<<"error: parse error:"<<s<<std::endl;
            exit(1);
        } 
        if (v == BASE) {
            v = 1;
            a.push_back(x);
        } else a.back() += (x) * v;
    }
    normalize();
}
bigint& bigint::operator = (const bigint& x) {
    a = x.a;
    return *this;
}
bigint& bigint::operator = (int x) { return *this = bigint(x); }
bigint& bigint::operator = (const std::string& s) { return *this = bigint(s); }
bool bigint::operator < (const bigint& x) const {
    if (a.size() != x.a.size()) return (a.size() < x.a.size());
    for (int i = a.size() - 1; i >= 0; --i)
        if (a[i] != x.a[i]) return (a[i] < x.a[i]);
    return false;
}
bool bigint::operator > (const bigint& x) const { return x < (*this); }
bool bigint::operator <= (const bigint& x) const { return !(x < (*this)); }
bool bigint::operator >= (const bigint& x) const { return !((*this) < x); }
bool bigint::operator != (const bigint& x) const { return (*this) < x || x < (*this); }
bool bigint::operator == (const bigint& x) const { return !((*this) < x || x < (*this)); }
bigint& bigint::operator += (const bigint& x) {
    if (a.size() < x.a.size()) a.resize(x.a.size());
    int tmp = 0;
    for (int i = 0; i < (int)a.size(); ++i) {
        a[i] += (i<(int)x.a.size()?x.a[i]:0) + tmp;
        tmp = a[i] / BASE;
        a[i] %= BASE;
    }
    if (tmp) a.push_back(1);
    return *this;
}
bigint& bigint::operator -= (const bigint& x) {
    std::vector<int> b(x.a);
    for (int i = 0, tmp = 0; i < (int)a.size(); ++i) {
        a[i] += BASE - (i<(int)b.size()?b[i]:0) + tmp;
        tmp = a[i] / BASE - 1;
        a[i] %= BASE;
    }
  return this->normalize();
}
bigint& bigint::operator *= (const bigint& x) {
    std::vector<int> c(a.size()*x.a.size()+1);
    for (int i = 0; i < (int)a.size(); ++i) {
        long long tmp = 0;
        for (int j = 0; j < (int)x.a.size(); ++j) {
            long long v = (long long)a[i] * x.a[j] + c[i+j] + tmp;
            tmp = v / BASE;
            c[i+j] = (int)(v % BASE);
        }
        if (tmp) c[i+x.a.size()] += (int)tmp;
    }
    a.swap(c);
    return this->normalize();
}
bigint bigint::operator + (const bigint& x) const {
    bigint res(*this); return res += x;
}
bigint bigint::operator - (const bigint& x) const {
    bigint res(*this); return res -= x;
}
bigint bigint::operator * (const bigint& x) const {
    bigint res(*this); return res *= x;
}
std::istream& operator >> (std::istream& is, bigint& x) {
    std::string tmp; is >> tmp;
    x = bigint(tmp);
    return is;
}
std::ostream& operator << (std::ostream& os, const bigint& x) {
    if (!x.a.size()) os << 0;
    else os << x.a.back();
    for (int i = x.a.size()-2; i >= 0; --i) {
        os.width(bigint::LEN);
        os.fill('0');
        os << x.a[i];
    }
    return os;
}
bigint pow2(int n) {
    bigint res(1);
    rep (i, n) res *= 2;
    return res;
}

int main()
{
    int t, n;
    bigint all, p, ans, tmp;
    cin >> t;
    rep (caseno, t) {
        cin >> n >> p;
        all = pow2(n);
        ans = tmp = 0;
        rep (i, n) {
            tmp += pow2(n - i - 1);
            if (p <= tmp) break;
            ans += pow2(i + 1);
        }
        if (p == all) ans = all - 1;
        cout << "Case #" << caseno + 1 << ": " << ans;
        ans = all - 1;
        rep (i, n) {
            if (p >= pow2(n - i)) break;
            ans -= pow2(i);
        }
        cout << " " << ans << endl;
    }
}
