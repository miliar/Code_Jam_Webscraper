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
    int r, c, w;

    REP(casenum, n) {
        scanf("%d %d %d", &r, &c, &w);
        int sum = 0;

        if (r > c) {
            int temp = r;
            r = c;
            c = temp;
        }
        // now r <= c;

        if (w == 1) sum = r * c;
        else if (r == 1) {
            sum += c/w;
            if (c%w) sum++;
            sum += (w-1);
        }
        else if (r == 2) {
            sum = 0;
        }
        else if (r > 2) {
            sum += ((r-2)/w) * ((c - 2)/w);
            if (r % 2) sum += (c-1)/w;
            PI(sum);

            sum += c/w;
            if (r % 2) sum += c/w;
            PI(sum);

            sum += r/w;
            if (c % 2) sum += r/w;
            PI(sum);

            if (w > 1) sum += w;
            PI(sum);
        }
        printf("Case #%d: %d\n", casenum+1, sum);
    }//end while
    return 0;
} //end main
