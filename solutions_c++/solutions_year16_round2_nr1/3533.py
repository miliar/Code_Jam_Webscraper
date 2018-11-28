#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define VAR(a,b)        __typeof(b) a=(b)
#define REP(i,n)        for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b)      for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b)     for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c)   for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c)          (c).begin(),(c).end()
#define TRACE(x)        cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x)        cerr << #x << " = " << x << endl;
#define eprintf(...)    fprintf(stderr, __VA_ARGS__)

typedef long long               ll;
typedef long double             ld;
typedef unsigned long           ulong;
typedef unsigned long long      ull;
typedef vector<int>             VI;
typedef vector<char>            VC;

char a[256];

int nums[10];

void run(char c, const string& str, int num) {
    int diff = a[c-'A'];
    nums[num] += diff;
    REP(i, str.size()) {
        //cerr << "sub " << str[i] << endl;
        a[str[i]-'A'] -= diff;
    }
}

int main() {
    //freopen("input",  "r", stdin);
    //freopen("output", "w", stdout);
    int TN;
    cin >> TN;
    FOR(TI,1,TN) {
        memset(a, 0, sizeof(a));
        memset(nums, 0, sizeof(nums));
        string S;
        cin >> S;
        REP(i,S.size())
            ++a[S[i]-'A'];
        printf("Case #%d: ", TI);
        run('Z', "ZERO", 0);
        run('X', "SIX", 6);
        run('G', "EIGHT", 8); 
        run('H', "THREE", 3);
        run('W', "TWO", 2);       

        run('R', "FOUR", 4);
        run('F', "FIVE", 5);
        run('I', "NINE", 9);
        run('V', "SEVEN", 7);
        run('O', "ONE", 1);
        REP(i, 10)
            REP(j, nums[i])
                printf("%d", i);
        printf("\n");
        REP(i,256)
            if (a[i] != 0)
                cout << "ERROR: " << i+'A' << endl;
    } // next test
    return 0;
}
