#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <functional>
#include <iterator>
#include <map>
#include <numeric>
#include <cstring>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <cctype>
#include <math.h>
#include <cstdlib>

using namespace std;

#define I64 long long int
#define INF 0x7f7f7f7f
#define SIZE 1000
#define MAX 1000010
#define EPS 1e-9
#define PI 2*acos(0.0)

#define PII pair <int, int>
#define PLL pair <I64, I64>
#define PDD pair <double, double>
#define PSI pair <string, int>
#define PIS pair <int, string>
#define PSS pair <string string>

#define MII map <int, int>
#define MLL map <I64, I64>
#define MDD map <double, double>
#define MSI map <string, int>
#define MIS map <int, string>
#define MSS map <string string>

#define VI vector <int>
#define VS vector <string>
#define QI queue <int>
#define QS queue <string>
#define SI stack <int>
#define SS stack <string>

#define pb push_back
#define pob pop_back
#define mp make_pair

#define IT iterator
#define ff first
#define ss second

#define SET(a, b) memset( a, b, sizeof (a) )
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define IAMHERE cout << "YES\n";
#define DEBUG(a, b) cout << a << ": " << b << "\n";

bool flag[11];
int ans[MAX];
int cnt = 0;

void digit (int n)
{
    while (n > 0) {
        int d = n % 10;
        n = n / 10;
        if (!flag[d]) {
            flag[d] = true;
            cnt++;
        }
    }
    return;
}

void preCalculate ()
{
    ans[0] = -1;

    for (int N = 1; N <= 1000000; N++) {
        int n = N;
        SET(flag, false);
        cnt = 0;
        for (int i = 1; ; i++) {
            n = N * i; //DEBUG(N, n);
            digit(n);
            if (cnt == 10) {
                break;
            }
        }
        ans[N] = n;
    }
    return;
}

int main()
{
    READ("A-large.in");
    WRITE("out.txt");
    int Case=1;
    int n;
    char dump[2];

    preCalculate();
    //for (int i = 0; i < 1000001; i++) DEBUG(i, ans[i]);
    int tc; scanf("%d", &tc);

    while (tc--) {
        scanf("%d", &n);
        if (n == 0) printf("Case #%d: INSOMNIA\n", Case++);
        else printf("Case #%d: %d\n", Case++, ans[n]);
    }
    return 0;
}
