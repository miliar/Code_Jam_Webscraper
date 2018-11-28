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
    int casenum = 1;
    int r, c, x;
    while(n--) {
        printf("Case #%d: ", casenum++);
        scanf("%d %d %d", &x, &r, &c);
        switch(x) {
            case 1 :
                printf("GABRIEL\n");
                break;
            case 2 :
                if ((r * c) % 2 == 0) printf("GABRIEL\n");
                else printf("RICHARD\n");
                break;
            case 3 :
                if ((r * c) % 6 == 0 || (r*c) == 9) printf("GABRIEL\n");
                else printf("RICHARD\n");
                break;
            case 4 :
                if (r * c >= 12) printf("GABRIEL\n");
                else printf("RICHARD\n");
                break;
        }
    }//end while
    return 0;
} //end main
