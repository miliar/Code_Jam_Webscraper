#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <bitset>

using namespace std;

#define MP make_pair
#define PB push_back
#define PL printf("\n")
#define CENDL "\n"
#define CDOT "."
#define CSP " "
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?-(x):(x))
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) for(int i=0;i<(n);i++)
#define CLEAR(a,b) memset(a,b,sizeof(a))
#define bug(x) printf("Bug tester #%d\n", x)
#define cbug(x) { cout << "Bug tester #" << x << CENDL; }
#define PI(x) printf("%d\n", x)


typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

// ios_base::sync_with_stdio(false);
// int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
// int __builtin_popcount (unsigned int x);

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt", "w", stdout);
    int n; scanf("%d", &n);
    int s;
    int casenum = 1;
    char str[1005];
//    string str;
    while(n--) {
        scanf("%d %s", &s, str);
        //cin >> s >> str;

        //REP(i, 100) cout << i << "." <<  (int) str[i] << CENDL;

        int sum = 0;
        int ans = 0;
        int size = strlen(str);
        REP(i, size) {
           // printf("%d %lld %lld %d\n", i, sum, ans, s);
            if (sum >= s) {
               // printf("going to break\n");
                break;
            }
            if (str[i] == '0') {
             //   printf("going to continue\n");
                continue;
            }
            if (sum < i) {
                ans += i - sum;
                sum = i;

            }
            sum += str[i] - '0';
            //printf("%d %d %d\n", i, sum, ans);
        }
        printf("Case #%d: %d\n", casenum++, ans);
    }//end while
    return 0;
} //end main
