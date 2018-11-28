#include <string>
#include <iostream>
#include <vector>
#include <utility>
#include <cstdio>
#include <sstream>
using namespace std;

class BigInteger
{
public:
    static const int L = 300 / 8;
    static const int CPS = 100000000;
    
	bool operator < (const BigInteger & other) const { return cmp(other) < 0; }
    bool operator > (const BigInteger & other) const { return cmp(other) > 0; }
    bool operator <= (const BigInteger & other) const { return cmp(other) <= 0; }
    bool operator >= (const BigInteger & other) const { return cmp(other) >= 0; }
    bool operator == (const BigInteger & other) const { return cmp(other) == 0; }
    bool operator != (const BigInteger & other) const { return cmp(other) != 0; }
    
    int len, d[L];
    void fix() {
        while (len > 0 && d[len] == 0) len--;
    }
    
    BigInteger(int x = 0) {
        for (d[len = 0] = 0; x; x /= CPS) d[++len] = x % CPS;
    }
    BigInteger(const char *s) {
        d[len = 0] = 0;
        for (int i = strlen(s) - 1, e = CPS; i >= 0; i--)
            if (e == CPS) d[++len] = s[i] - '0', e = 10;
            else d[len] += (s[i] - '0') * e, e *= 10;
        fix();
    }
    BigInteger(const BigInteger &rhs) {
        len = rhs.len;
        memcpy(d, rhs.d, sizeof d[0] * (len + 1));
    }
    
    int cmp(const BigInteger &b) const {
        if (len != b.len) return len - b.len;
        int i = len; while (i > 1 && d[i] == b.d[i]) i--;
        return d[i] - b.d[i];
    }
    
    string print() const {
        string ret = "";
        char temp[20];
        sprintf(temp, "%d", d[len]);
        ret += string(temp);
        for (int i = len - 1; i > 0; i--)
        {
            sprintf(temp, "%08d", d[i]);
            ret += string(temp);
        }
        return ret;
    }
    
	friend ostream & operator << (ostream & out, BigInteger & a)
	{
		out << a.print();
		return out;
	}
    
    BigInteger& operator += (const BigInteger &b) {
        for (int i = 1, t = 0; i <= b.len || t; t = (d[i] += t) / CPS, d[i++] %= CPS) {
            if (i > len) d[++len] = 0;
            if (i <= b.len) t += b.d[i];
        }
        return *this;
    }
    
    BigInteger operator + (const BigInteger &b) const {
        return BigInteger(*this) += b;
    }
    
    BigInteger operator - (const BigInteger &b) const {
        BigInteger c(*this);
        for (int i = 1, j = 0; i <= len; i++) {
            c.d[i] -= j;
            if (i <= b.len) c.d[i] -= b.d[i];
            if (c.d[i] < 0) j = 1, c.d[i] += CPS;
            else j = 0;
        }
        c.fix();
        return c;
    }
    
    BigInteger& operator *= (const int &b) {
        if (b == 0) len = 0;
        long long t = 0;
        for (int i = 1; i <= len; i++)
            d[i] = (t += d[i] * (long long) b) % CPS, t /= CPS;
        while (t) d[++len] = t % CPS, t /= CPS;
        return *this;
    }
    
    BigInteger operator * (const BigInteger &b) const {
        if (len == 0 || b.len == 0) return 0;
        long long sum, t = 0;
        BigInteger c; c.len = len + b.len - 1;
        for (int i = 1; i <= c.len; i++) {
            sum = t;
            int b1 = len < i ? len : i;
            int b2 = i - b.len > 0 ? i - b.len : 0;
            for (int j = b2; j < b1 && j < i; j++) {
                if (i - j > b.len) j = i - b.len - 1;
                else sum += (long long) d[j + 1] * b.d[i - j] ;
            }
            if (sum >= CPS) t = sum / CPS, c.d[i] = sum % CPS;
            else t = 0, c.d[i] = sum;
        }
        if (t) c.d[++c.len] = t;
        return c;
    }
    
    BigInteger operator / (const int &b) const {
        BigInteger c;
        long long t = 0;
        for (int i = len; i > 0; i--)
            t = t * CPS + d[i], c.d[i] = t / b, t %= b;
        c.len = len;
        c.fix();
        return c;
    }
    
    BigInteger operator / (const BigInteger &b) const {
        BigInteger c, f;
        for (int i=len; i>0; i--) {
            !f.len ? (f=d[i]) : (f=f*CPS, f.d[1]=d[i]);
            if (f.cmp(b)<0) {c.d[i]=0; continue;}
            int lf=1, rt=CPS-1;
            while (lf<=rt) {
                int mid=lf+rt>>1;
                (f.cmp(b*mid)<0) ? (rt=mid-1) : (lf=mid+1);
            }
            f=f-b*rt; c.d[i]=rt; if (i>c.len) c.len=i;
        }
        return c;
    }
    
    int operator % (const int &b) const {
        long long t = 0;
        for (int i = len; i > 0; i--) t = (t * CPS + d[i]) % b;
        return t;
    }
    
    BigInteger operator % (const BigInteger &b) const {
        BigInteger f;
        for (int i=len; i>0; i--) {
            !f.len ? (f=d[i]) : (f=f*CPS, f.d[1]=d[i]);
            if (f.cmp(b)<0) continue;
            int lf=1, rt=CPS-1;
            while (lf<=rt) {
                int mid=lf+rt>>1;
                (f.cmp(b*mid)<0) ? (rt=mid-1) : (lf=mid+1);
            }
            f=f-b*rt;
        }
        return f;
    }
    
    void shiftRight() {
        for (int i = len, t = 0; i > 0; i--)
            t = t * CPS + d[i], d[i] = t >> 1, t &= 1;
        fix();
    }
    
    BigInteger sqrt() {
        if (len == 0) return 0;
        BigInteger x, y(*this);
        y.d[y.len = y.len / 2 + 1] = CPS - 1;
        do x = y, y = (*this) / x + x, y.shiftRight(); while (x.cmp(y) > 0);
        return x;
    }
    
};

BigInteger A, B;
vector<BigInteger> anss;

bool isPalidome(BigInteger x)
{
    ostringstream ostr;
    ostr << x;
    string s = ostr.str();
    
    for (int i = 0, j = (int)s.length() - 1; i < j; i++, j--)
        if (s[i] != s[j]) return false;
    return true;
}

/**
 1
 2
 3
 11
 22
 101
 111
 121
 202
 212
 1001
 1111
 2002
 10001
 10101
 10201
 11011
 11111
 11211
 20002
 20102
 100001
 101101
 110011
 111111
 200002
 1000001
 1001001
 1002001
 1010101
 1011101
 1012101
 1100011
 1101011
 1102011
 1110111
 1111111
 2000002
 2001002
*/
void init()
{
    vector<BigInteger> cur;
    cur.push_back(BigInteger("1"));
    cur.push_back(BigInteger("2"));
    cur.push_back(BigInteger("3"));
    
    for (int l = 1; l <= 55; ++l)
    {
        vector<BigInteger> newcur;
        for (int i = 0; i < cur.size(); ++i)
        {
            anss.push_back(cur[i]);
            
            ostringstream ostr;
            ostr << cur[i];
            string s = ostr.str();
            
            if (s.length() % 2 == 0)
            {
                for (char c = '0'; c <= '2'; ++c)
                {
                    string news = s.substr(0, s.length() / 2) + string(1, c) + s.substr(s.length() / 2);
                    BigInteger x(news.data());
                    BigInteger sqrx = x * x;
                    if (isPalidome(sqrx)) newcur.push_back(x);
                }
            }
            else
            {
                string news = s.substr(0, s.length() / 2) + string(1, s[s.length() / 2]) + s.substr(s.length() / 2);
                BigInteger x(news.data());
                BigInteger sqrx = x * x;
                if (isPalidome(sqrx)) newcur.push_back(x);
            }
        }
        cur = newcur;
    }
    
    for (int i = 0; i < anss.size(); ++i) anss[i] = anss[i] * anss[i];
    cerr << "Total = " << anss.size() << endl;
}

void read()
{
    string a, b;
    cin >> a >> b;
    A = BigInteger(a.data());
    B = BigInteger(b.data());
}

string deal()
{
    int cnt = 0;
    for (int i = 0; i < anss.size(); ++i)
        if (anss[i] >= A && anss[i] <= B) cnt++;
    ostringstream ostr;
    ostr << cnt;
    return ostr.str();
}

int main()
{
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/QUAL/c.in", "r", stdin);
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/QUAL/c.out", "w", stdout);
    
    init();
    
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test)
    {
        read();
        cerr << "Running " << test << endl;
        cout << "Case #" << test << ": " << deal() << endl;
    }
    return 0;
}