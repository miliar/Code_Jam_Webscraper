#include<map>
#include<set>
#include<list>
#include<cmath>
#include<ctime>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<cctype>
#include<cstdio>
#include<string>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>

using namespace std;

// Template Begin(By yayamao)
#ifndef ONLINE_JUDGE
	#define READ freopen("C-small-attempt0.in", "r", stdin)
	#define WRITE freopen("C-small-attempt0.out", "w", stdout)
#else
	#define READ
	#define WRITE
#endif

#ifdef _MSC_VER
	#define int64 __int64
	#define uint64 unsigned __int64
#else
	#define int64 long long
	#define uint64 unsigned long long
#endif

#define S(x) ((int)x.size())
#define L(x) ((int)x.length())

#define X first
#define Y second
#define MII map<int, int>
#define MSI map<string, int>
#define MIS map<int, string>
#define PII pair<int, int>
#define PSI pair<string, int>
#define PIS pair<int, string>
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)

#define TWO(x)			(1 << (x))
#define TWOL(x)			(1LL << (x))
#define LOWER_BIT(x)	((x) & (-(x)))
#define CONTAIN(s,x)	(((s) & TWO(x)) != 0)
#define CONTAINL(s,x)	(((s) & TWOL(x)) != 0)

template<class T>inline void checkMax(T &a,const T &b){if(a < b) a = b;}
template<class T>inline void checkMin(T &a,const T &b){if(b < a) a = b;}
template<class T>inline string toString(const T &n){ostringstream out; out << n; out.flush(); return out.str();}
template<class T>inline T toValue(const string &s){T x; istringstream in(s); in >> x; return x;}
bool hasNext(){char c;if(scanf(" %c",&c)==EOF) return false; ungetc(c, stdin); return true;}

const double EPS  = 1E-8;
const double D_INF = 1E99;
const int I_INF = 0x7FFFFFFF;
const int64 L_INF = 0x7FFFFFFFFFFFFFFFLL;

int dx[]={ 0, 0,-1, 1,-1, 1,-1, 1};
int dy[]={-1, 1, 0, 0,-1,-1, 1, 1};
string dir[]={"L", "R", "U", "D", "LU", "LD", "RU", "RD"};

int tenPower[10]={0x1,0xA,0x64,0x3E8,0x2710,0x186A0,0xF4240,0x989680,0x5F5E100,0x3B9ACA00};

// [l, r]
#define range(i, l, r) for(int i = (l); i <= (int)(r); ++i)
#define rangeD(i, r, l) for(int i = (r); i >= (int)(l); --i)

// [0, n)
#define rep(i, n) for(int i = 0; i < (int)(n); ++i)
#define repD(i, n) for(int i = (int)(n) - 1; i >= 0; --i)

// [begin, end)
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

#define setv(a, v) memset(a, v, sizeof(a))
#define all(c) (c).begin(), (c).end()
// Template Ended(By yayamao)

void preProcess() {
}

const int N = 55;
int64 palindromicSquares[N] = {
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
	1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001LL,
    10221412201LL,
    12102420121LL,
    12345654321LL,
    40000800004LL,
    1000002000001LL,
    1002003002001LL,
    1004006004001LL,
    1020304030201LL,
    1022325232201LL,
    1024348434201LL,
    1210024200121LL,
    1212225222121LL,
    1214428244121LL,
    1230127210321LL,
    1232346432321LL,
    1234567654321LL,
    4000008000004LL,
    4004009004004LL,
};

void run(const int &caseID) {
    int64 lower, higher;
    cin >> lower >> higher;

    int count = 0;
    rep (i, N) {
        if (lower <= palindromicSquares[i] && palindromicSquares[i] <= higher) {
            ++count;
        }
    }

    cout << "Case #" << caseID << ": " << count << endl;
}

void runWithCaseT() {
    int caseT;
    scanf("%d", &caseT);
    getchar();
    for(int caseID = 1; caseID <= caseT; ++caseID) {
        run(caseID);
    }
}

void runWithoutCaseT() {
    int caseID = 0;
    while(hasNext()) {
        run(++caseID);
    }
}

int main(int argc, char *argv[]) {
    srand(time(NULL));

    READ;
    WRITE;

    preProcess();

    runWithCaseT();
    //runWithoutCaseT();

    return (EXIT_SUCCESS);
}

