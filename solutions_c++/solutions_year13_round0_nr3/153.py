#define ENABLE_MAIN 1
#if ENABLE_MAIN


#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <functional>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <list>
#include <queue>
#include <numeric>
#include <iomanip>
#include <fstream>


using namespace std;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;
typedef pair<int, int> PII;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef pair<ll, ll> PLL;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;

const ll oo = 1LL << 60;
const int kNumMoves = 4;
const int kMoves[kNumMoves][2] = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

#define FOR(i, n) for (int i = 0; i < int(n); ++i)
#define FORI(i, s, n) for (int i = s; i < int(n); ++i)
#define FORD(i, n) for (int i = n - 1; i >= 0; --i)
#define VALID(i, mx) (i >= 0 && i < mx)

string PrintCase(int i)
{     
    ostringstream os;
    os << "Case #" << (i + 1) << ": ";
    return os.str();
}

char buf[100];

struct BigNumber
{
    BigNumber(ll v = 0);
    BigNumber(const string& s);
    int Digits() const { return digits.size(); }
    BigNumber& operator+=(const BigNumber& a);
    string AsString() const;
    vl digits;    
    static const ll kBase = 100000000LL;
};

BigNumber::BigNumber(const string& s)
{
    int n = s.size();
    int idx = n - 1;
    ll v = 0;
    ll power = 1;
    while (idx >= 0)
    {
        v = v + power * (s[idx--] - '0');
        power *= 10;        
        if (power < kBase) continue;
        digits.push_back(v % kBase);
        v /= kBase;
        power = 1;
    }

    if (v)
        digits.push_back(v);
}

BigNumber::BigNumber(ll v)
{
    int pos = 0;
    digits.push_back(0);
    while (v)
    {
        if (digits.size() == pos) digits.push_back(0);
        digits[pos] = v;
        v = digits[pos] / BigNumber::kBase;
        digits[pos] %= BigNumber::kBase;
        ++pos;
    }
}

ostream& operator<<(ostream& os, const BigNumber& a)
{
    int len = a.digits.size();
    FORD(i, len)
    {
        if (i != len - 1)
        {
            ll power = 10;
            while ((power < BigNumber:: kBase) && (a.digits[i] * power) < BigNumber::kBase)
            {
                power *= 10;
                os << 0;
            }
        }
        os << a.digits[i];
    }

    return os;
}
bool operator<(const BigNumber& a, const BigNumber& b)
{
    int as = a.Digits();
    int bs = b.Digits();
    if (as != bs) return as < bs;
    
    FORD(i, as)
    {
        if (a.digits[i] != b.digits[i])
            return a.digits[i] < b.digits[i];
    }

    return false;
}

string BigNumber::AsString() const
{
    string s;

    ostringstream os;
    os << *this;

    return os.str();
}

BigNumber& BigNumber::operator+=(const BigNumber& a)
{
    int l = a.digits.size();
    ll carry = 0;
    while (int(digits.size()) < l) digits.push_back(0);
    FOR(i, l)
    {
        ll sum = digits[i] + a.digits[i] + carry;
        carry = sum / BigNumber::kBase;
        digits[i] = sum % kBase;
    }

    FORI(i, l, digits.size())
    {
        ll sum = digits[i] + carry;
        carry = sum / BigNumber::kBase;
        digits[i] = sum % kBase;
    }

    if (carry)
        digits.push_back(carry);

    return *this;
}

BigNumber Add(const BigNumber& a, const BigNumber& b)
{
    int as = a.Digits();
    int bs = b.Digits();
    int l = min(as, bs);
    int lMax = max(as, bs);

    BigNumber res;

    ll carry = 0;
    FOR(i, l)
    {        
        ll sum = a.digits[i] + b.digits[i] + carry;
        carry = sum / BigNumber::kBase;
        res.digits.push_back(sum % BigNumber::kBase);
    }

    if (as != bs)
    {
        const BigNumber& c = (as < bs) ? b : a;

        FORI(i, l + 1, lMax)
        {
            ll sum = carry + c.digits[i];
            carry = sum / BigNumber::kBase;
            res.digits.push_back(sum % BigNumber::kBase);
        }
    }

    if (carry)
        res.digits.push_back(carry);

    return res;
}

void Mult_Add(const BigNumber&a, ll dig, int offset, BigNumber& res)
{
    int as = a.Digits();
    ll carry = 0;
    FOR(i, as)
    {
        while (int(res.digits.size()) <= (i + offset)) res.digits.push_back(0);

        ll prod = res.digits[i + offset] + a.digits[i] * dig + carry;
        carry = prod / BigNumber::kBase;
        res.digits[i + offset] = prod % BigNumber::kBase;
    }
    int pos = as + offset;
    while (carry)
    {
        while (int(res.digits.size()) <= pos) res.digits.push_back(0);
        res.digits[pos] += carry;
        carry = res.digits[pos] / BigNumber::kBase;
        res.digits[pos] %= BigNumber::kBase;
        ++pos;
    }
}

BigNumber Mult(const BigNumber& a, const BigNumber& b)
{    
    int bs = b.Digits();

    BigNumber res;

    FOR(i, bs)
        Mult_Add(a, b.digits[i], i, res);

    return res;
}

bool HasSqPalindrome(ll v)
{    
    if (v > 3)
    {
        int d;
        ll c = v;
        while (c)
        {
            d = c % 10;
            if (d > 2) return false;
            c /= 10;
        }
    }
    stringstream ss;
    ss << v;
    string s = ss.str();

    int d = s.size();
    FOR(i, d / 2) { if (s[i] != s[d - 1 - i]) return false; }
    ll vsq = v * v;
    stringstream sss;
    sss << vsq;
    s = sss.str();
    d = s.size();
    FOR(i, d / 2) { if (s[i] != s[d - 1 - i]) return false; }
    
    return true;
}

vector<BigNumber> cands;
vector<BigNumber> bn;

void AddCandidate(const string& s)
{
    BigNumber a(s);
    BigNumber sq = Mult(a, a);
    string res = sq.AsString();

    int d = res.size();
    FOR(i, d / 2) { if (res[i] != res[d - 1 - i]) return; }
    cands.push_back(a);
    bn.push_back(sq);
}


void AddPalindromeCandidate(int n, int offset, int prefix, int remaining, int oneCount, int twoCount, string& s)
{
    if (!remaining)
    {        
        AddCandidate(s);
        return;
    }
    if (remaining == 1)
    {
        s[offset] = '0';
        AddCandidate(s);
        if (oneCount < 9)
        {
            s[offset] = '1';
            AddCandidate(s);
        }
        if (!twoCount && oneCount < 5)
        {
            s[offset] = '2';
            AddCandidate(s);
        }
        return;
    }

    s[offset] =  s[n - 1 - offset] = '0';
    AddPalindromeCandidate(n, offset + 1, prefix, remaining - 2, oneCount, twoCount, s);

    if (prefix < 2 && oneCount < 7)
    {
        s[offset] =  s[n - 1 - offset] = '1';
        AddPalindromeCandidate(n, offset + 1, prefix, remaining - 2, oneCount + 2, twoCount, s);
    }
}


void GenerateCandidates()
{
    AddCandidate("1");
    AddCandidate("2");
    AddCandidate("3");
    AddCandidate("11");
    AddCandidate("22");

    FORI(i, 3, 52)
    {
        string s(i, 0);
        FORI(j, 1, 3)
        {
            s[0]        = j + '0';
            s[i - 1]    = j + '0';
            int oneCount = (j == 1) ? 2 : 0;
            int twoCount = (j == 2) ? 2: 0;
            AddPalindromeCandidate(i, 1, j, i - 2, oneCount, twoCount, s);
        }
    }
    sort(cands.begin(), cands.end());
}

int main()
{
     ofstream cout ("C-large-2.out");
     ifstream cin ("C-large-2.in");

    vector<PLL> sq;
    GenerateCandidates();    
    
    sort(bn.begin(), bn.end());

    int t;
    cin >> t;    
    FOR(c, t)
    {
        string as, bs;

        cin >> as >> bs;

        BigNumber a(as);
        BigNumber b(bs);

        int idxL = lower_bound(bn.begin(), bn.end(), a) - bn.begin();
        int idxU = upper_bound(bn.begin(), bn.end(), b) - bn.begin();

        cout << PrintCase(c) << (idxU - idxL) << endl;
    }

    return 0;
}
#endif