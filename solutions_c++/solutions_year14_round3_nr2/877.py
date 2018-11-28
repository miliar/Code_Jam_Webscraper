#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <cassert>
#include <queue>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline _T ABS(const _T& x) { return (x<0)?-x:x;}
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }
template <class _T> inline _T gcd(const _T &a, const _T &b) {
    _T t;

    while (!(b == 0)) {
        t = a % b;
        a = b;
        b = t;
    }

    return a;
}

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef unsigned uns;
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef pair < int, int > PII;
typedef map < string, int > MSI;
typedef map < string, void * > MSV;

// DEBUG
//#define DEBUG
#ifdef DEBUG
static bool const _debug_ = true;
#else
static bool const _debug_ = false;
#endif
#define DOUT(MSG) (_debug_ && cerr << (MSG))
#define DLOUT(MSG) (_debug_ && cerr << (MSG) << endl)


// ########## UTILITIES ##########//
inline uns getUnsigned() {
    uns curr;
    scanf("%u", &curr);
    return curr;
}

inline void getUnsigned(uns &one, uns &two) {
    scanf("%u%u", &one, &two);
}

inline void getUnsigned(uns &one, uns &two, uns &three) {
    scanf("%u%u%u", &one, &two, &three);
}

inline int getInt() {
    int curr;
    scanf("%d", &curr);
    return curr;
}

inline void getInt(int &one, int &two) {
    scanf("%d%d", &one, &two);
}

inline void getInt(int &one, int &two, int &three) {
    scanf("%d%d%d", &one, &two, &three);
}

inline double getDouble() {
    double curr;
    scanf("%lf", &curr);
    return curr;
}

inline void getDouble(double &one, double &two) {
    scanf("%lf%lf", &one, &two);
}

inline void getDouble(double &one, double &two, double &three) {
    scanf("%lf%lf%lf", &one, &two, &three);
}

inline void FLUSH() {
    string dummy;
    getline(cin, dummy);
}

inline string getString() {
    string curr;
    cin >> curr;
    return curr;
}

inline string getLine() {
    string curr;
    getline(cin, curr);
    return curr;
}

inline void split(string const &in, VS &out, char delim = ' ') {
    size_t start = 0; size_t len = 0;
    size_t end = in.sz -1;
    size_t foundAt = in.find_first_of(delim, start);
    while (foundAt != string::npos) {
        len = (foundAt - start);
        out.pb(in.substr(start, len));
        start = foundAt+1;
        foundAt = in.find_first_of(delim, start);
    }
    if (foundAt != end) {
        out.pb(in.substr(start));
    }
}

// ########## UTILITIES ##########//
#define MODULO (1000000007)

// 0. VARIABLES
u64 factArr[1001];
void preprocess() {
    factArr[0] = 1;
    for (int ff=1; ff<1001; ++ff) {
        factArr[ff] = (factArr[ff-1]*ff)%MODULO;
    }
}

inline void foreachTest(uns testNum) {
    // 1. READ inputs
    int N;
    cin >> N;
    getLine();

    int nn;
    /*string sets[N];
    for (nn=0; nn<N; ++nn){
        cin >> sets[nn];
    }*/
    string line = getLine();
    VS sets;
    split(line, sets);
    int csz, ss;
    char lch;
    for (nn=0; nn<N; ++nn) {
        lch = '-';
        string newstr;
        string const &curr = sets[nn];
        csz = curr.size();
        for (ss=0; ss<csz; ++ss) {
            if (lch != curr[ss]) {
                newstr += curr[ss];
                lch = curr[ss];
            }
        }
        sets[nn] = newstr;
    }
    /*cerr << "STRINGS:" << endl;
    for (nn=0; nn<N; ++nn) {
        cerr << sets[nn] << endl;
    }*/

    // 2. SOLVE test
    map<char, unsigned> singleChars;
    vector<int> toErase;
    for (nn=0; nn<N; ++nn) {
        if (sets[nn].size() == 1) {
            int cnt = ++singleChars[sets[nn][0]];
            if (cnt > 1) {
                toErase.push_back(nn);
            }
        }
    }
    int erased = 0;
    for (nn=0; nn<toErase.size(); ++nn) {
        sets.erase(sets.begin()+toErase[nn]-erased);
        ++erased;
    }
    N = sets.size();
    //cerr << " new N = " << N << endl;

    vector<int> perm;
    for (nn=0; nn<N; ++nn) {
        perm.push_back(nn);
        //cerr << " " << sets[nn] << endl;
    }

    u64 res = 0;
    do {
        vector<int>::iterator pei = perm.begin(), pee = perm.end();
        set<char> encountered;
        bool validPerm=true;
        char lch = '-';
        for (; (pei != pee) && validPerm; ++pei) {
            string const &curr = sets[*pei];
            csz = curr.size();
            for (ss=0; ss<csz; ++ss) {
                if (lch != curr[ss]) {
                    if (encountered.find(curr[ss]) != encountered.end()) {
                        validPerm = false;
                        break;
                    } else {
                        lch = curr[ss];
                        encountered.insert(lch);
                    }
                }
            }
        }
        if (validPerm) {
            ++res;
        }
    } while (next_permutation(perm.begin(), perm.end()));

    //cerr << " curr res = " << res << endl;

    map<char, unsigned>::iterator  sci = singleChars.begin(), sce = singleChars.end();
    for (; sci != sce; ++sci) {
        if (sci->second > 1) {
            res = (factArr[sci->second] * res) % MODULO;
        }
    }
    
    // 3.  WRITE outputs
    cout << "Case #" << testNum << ": ";
    cout << res % MODULO;

    // 4. CLEANUP for next test
    cout << endl;
}

int main() {
    //freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
    //freopen("log.txt", "wt", stderr);
    cout << setiosflags(ios::fixed) << setprecision(10);

    preprocess();
    uns T = getUnsigned();
    for (uns tt=1U; tt<=T; ++tt) {
        //DOUT("At test: "); DLOUT(tt);
        foreachTest(tt);
    }
    return 0;
}

