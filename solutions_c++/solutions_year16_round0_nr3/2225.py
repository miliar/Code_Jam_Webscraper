

#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;
template<class T> inline bool amax (T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool amin (T &a, const T &b) { if (a > b) { a = b; return 1; } return 0; }
template<class T> ostream& operator << (ostream &os, const vector<T> &v) { os << "["; for (typename vector<T>::const_iterator it = v.begin(); it != v.end(); it++) { os << (it != v.begin() ? ", " : "") << *it; } os << "]"; return os; }
template<class T> ostream& operator << (ostream &os, const set<T> &s) { os << "["; for (typename set<T>::const_iterator it = s.begin(); it != s.end(); it++) { os << (it != s.begin() ? ", " : "") << *it; } os << "]"; return os; }
template<class Key, class Val> ostream& operator << (ostream &os, const map<Key, Val> &m) { os << "{"; for (typename map<Key, Val>::const_iterator it = m.begin(); it != m.end(); it++) { os << (it != m.begin() ? ", " : "") << it->first << ":" << it->second; } os << "}"; return os; }
template<class T, class S> ostream& operator << (ostream &os, const pair<T, S> &p) { os << "(" << p.first << ", " << p.second << ")"; return os; }
template <class T> istream& operator >> (istream &is, vector<T> &v) { for (size_t i = 0; i < v.size(); i++) is >> v[i]; return is; }
template <class Target, class Source> inline Target lexical_cast (const Source &s) { Target t; stringstream ss; ss << s; ss >> t; return t; }

//> v < ^ (clock wise)
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};
const int INFI = 1<<28;
const long long int INFL = 1LL<<60;
const double INFD = 1e+300;
const float INFF = 1e+100;
const double EPS = 1e-8;
const long long int MOD = 1000000007;

int solve ();
int main () {
    cout.setf(ios::fixed); cout.precision(10);
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}


class bigint {
private:
    static const int BASE = 100000000, LEN = 8;
    bool negative;
    std::vector<int> a;
    bigint& normalize();
public:
    bigint(int x = 0);
    bigint(const std::string& s);
    bigint& operator = (const bigint& x);
    bigint& operator = (int x);
    bigint& operator = (const std::string& s);
    const bool operator < (const bigint& x) const;
    const bool operator > (const bigint& x) const;
    const bool operator <= (const bigint& x) const;
    const bool operator >= (const bigint& x) const;
    const bool operator != (const bigint& x) const;
    const bool operator == (const bigint& x) const;
    bigint operator -() const;
    bigint& operator += (const bigint& x);
    bigint& operator -= (const bigint& x);
    bigint& operator *= (const bigint& x);
    bigint& operator /= (const bigint& x);
    bigint& operator %= (const bigint& x);
    const bigint operator + (const bigint& x) const;
    const bigint operator - (const bigint& x) const;
    const bigint operator * (const bigint& x) const;
    const bigint operator / (const bigint& x) const;
    const bigint operator % (const bigint& x) const;
    friend std::pair<bigint,bigint> divmod(const bigint& lhs, const bigint& rhs);
    friend std::istream& operator >> (std::ostream& is, bigint& x); //適当実装
    friend std::ostream& operator << (std::ostream& os, const bigint& x);
    friend const bigint abs(bigint x);
};
bigint& bigint::normalize() {
    int i = a.size()-1;
    while (i >= 0 && a[i] == 0) --i;
    a.resize(i+1);
    if (a.size() == 0) negative = false;
    return *this;
}
bigint::bigint(int x) : negative(x<0) {
    x = abs(x);
    for (; x > 0; x /= BASE) a.push_back(x % BASE);
}
bigint::bigint(const std::string& s): negative(false) {
    int p = 0;
    if (s[p] == '-') { ++p; negative = true; }
    else if (s[p] == '+') { ++p; }
    for (int i = s.size()-1, v = BASE; i >= p; --i, v*=10) {
    int x = s[i]-'0';
    if (x < 0 || 9 < x) {
      std::cerr<<"error: parse error:"<<s<<std::endl;
      exit(1);
    } 
    if (v == BASE) {
      v = 1;
      a.push_back(x);
    } else a.back() += (x)*v;
    }
    normalize();
}
bigint& bigint::operator = (const bigint& x) {
    negative = x.negative;
    a = x.a;
    return *this;
}
bigint& bigint::operator = (int x) { return *this = bigint(x); }
bigint& bigint::operator = (const std::string& s) { return *this = bigint(s); }
const bool bigint::operator < (const bigint& x) const {
    if (negative != x.negative) return negative < x.negative;
    if (a.size() != x.a.size()) return (a.size() < x.a.size())^negative;
    for(int i = a.size()-1; i >= 0; --i)
    if (a[i] != x.a[i]) return (a[i] < x.a[i])^negative;
    return false;
}
const bool bigint::operator > (const bigint& x) const { return x<(*this); }
const bool bigint::operator <= (const bigint& x) const { return !(x<(*this)); }
const bool bigint::operator >= (const bigint& x) const { return !((*this)<x); }
const bool bigint::operator != (const bigint& x) const { return (*this)<x || x<(*this); }
const bool bigint::operator == (const bigint& x) const { return !((*this)<x || x<(*this)); }
bigint bigint::operator -() const {
    bigint ret(*this);
    if (a.size()) ret.negative = !ret.negative;
    return ret;
}
bigint& bigint::operator += (const bigint& x) {
    if (negative != x.negative) return *this -= -x;
    if (a.size() < x.a.size()) a.resize(x.a.size());
    int tmp = 0;
    for (int i = 0; i < a.size(); ++i) {
    a[i] += (i<x.a.size()?x.a[i]:0) + tmp;
    tmp = a[i] / BASE;
    a[i] %= BASE;
    }
    if (tmp) a.push_back(1);
    return *this;
}
bigint& bigint::operator -= (const bigint& x) {
    if (negative != x.negative) return *this += -x;
    std::vector<int> b(x.a);
    if ((*this < x) ^ negative) {
    a.swap(b);
    negative = !negative;
    }
    for (int i = 0, tmp = 0; i < a.size(); ++i) {
    a[i] += BASE - (i<b.size()?b[i]:0) + tmp;
    tmp = a[i] / BASE - 1;
    a[i] %= BASE;
    }
    return this->normalize();
}
bigint& bigint::operator *= (const bigint& x) {
    negative ^= x.negative;
    std::vector<int> c(a.size()*x.a.size()+1);
    for (int i = 0; i < a.size(); ++i) {
    long long tmp = 0;
    for (int j = 0; j < x.a.size(); ++j) {
      long long v = (long long)a[i] * x.a[j] + c[i+j] + tmp;
      tmp = v / BASE;
      c[i+j] = (int)(v % BASE);
    }
    if (tmp) c[i+x.a.size()] += (int)tmp;
    }
    a.swap(c);
    return this->normalize();
}
bigint& bigint::operator /= (const bigint& x) {
    return *this = divmod(*this,x).first;
}
bigint& bigint::operator %= (const bigint& x) {
    return *this = divmod(*this,x).second;
}
const bigint bigint::operator + (const bigint& x) const {
    bigint res(*this); return res += x;
}
const bigint bigint::operator - (const bigint& x) const {
    bigint res(*this); return res -= x;
}
const bigint bigint::operator * (const bigint& x) const {
    bigint res(*this); return res *= x;
}
const bigint bigint::operator / (const bigint& x) const {
    bigint res(*this); return res /= x;
}
const bigint bigint::operator % (const bigint& x) const {
    bigint res(*this); return res %= x;
}
std::pair<bigint,bigint> divmod(const bigint& lhs, const bigint& rhs) {
    if (!rhs.a.size()) {
    std::cerr<<"error: division by zero"<<std::endl;
    exit(1);
    }
    bigint x(abs(rhs)), q, r;
    for (int i = lhs.a.size()-1; i >= 0; --i) {
    r = r * bigint::BASE + lhs.a[i];
    int head = 0, tail = bigint::BASE;
    if (r >= x) {
      while (head + 1 < tail) {
        int mid = (head + tail) / 2;
        if (x * bigint(mid) > r) tail = mid;
        else head = mid;
      }
      r -= x * head;
    }
    q.a.push_back(head);
    }
    reverse(q.a.begin(), q.a.end());
    bool neg = lhs.negative ^ lhs.negative;
    q.negative = neg; r.negative = neg;
    return std::make_pair(q.normalize(), r.normalize());
}
std::istream& operator >> (std::istream& is, bigint& x) {
    std::string tmp; is >> tmp;
    x = bigint(tmp);
    return is;
}
std::ostream& operator << (std::ostream& os, const bigint& x) {
    if (x.negative) os << '-';
    if (!x.a.size()) os << 0;
    else os << x.a.back();
    for (int i = x.a.size()-2; i >= 0; --i) {
    os.width(bigint::LEN);
    os.fill('0');
    os << x.a[i];
    }
    return os;
}
const bigint abs(bigint x) {
    x.negative = false;
    return x;
}

/* end of the library */

void Eratosthenes (int n, vector<int> &primes) {
    primes = vector<int>(n);
    primes[0] = primes[1] = 0;
    for (int i = 2; i < n; i++) primes[i] = i;
    for (int i = 2; i < n; i++)
        if (primes[i]) 
            for (int j = i<<1; j < n; j += i) 
                primes[j] = 0;
    //素数リスト用
    vector<int>::iterator it = remove(primes.begin(), primes.end(), 0);
    primes.erase(it, primes.end());
}


int solve () {
    int T;
    cin >> T;
    int caseNum = 1;
    int P = 1000;
    vector<int> primes;
    Eratosthenes(P, primes);
    while (T--) {
        cout << "Case #" << caseNum++ << ":" << endl;
        int ans = 0;
        int cnt = 0;
        while (1) {
            string s = "10000000000000000000000000000001";
            for (int i = 1; i < 31; i++) {
                s[i] = (rand()%2)?'1':'0';
            }
            vector<int> divisor(11, -1);
            bool ok = true;
            for (int b = 2; b <= 10; b++) {
                bigint n = 0;
                bigint mul = 1;
                for (int i = s.size()-1; i >= 0; i--) {
                    if (s[i] == '1') n += mul;
                    mul *= b;
                }
                for (int i = 0; i < primes.size(); i++) {
                    if (n % primes[i] == 0) {
                        divisor[b] = primes[i];
                    }
                }
                if (divisor[b] == -1) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                cnt++;
                cout << s;
                for (int b = 2; b <= 10; b++) {
                    cout << " " << divisor[b];
                }
                cout << endl;
                if (cnt == 500) return 0;
            }
        }
    }
    return 0;
}
