/* [themighty] deathsurgeon (Rupesh Maity)
 * 2nd year, B.Tech in IT
 * IIIT - Allahabad
 */

#include <iostream>
#include <cstdio>
#include <math.h>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <stack>
#include <queue>
#include <vector>
#include <map>

using namespace std;

typedef long long LL;
typedef unsigned uint;
typedef pair<int, int> pii;

#define MOD 1000000007
#define MAX 1000000
#define pb push_back
#define yes puts("YES")
#define no puts("NO")
#define sd(x) scanf("%d", &x)
#define PI 3.14159265

int main() {
	freopen("2input.txt", "r", stdin);
    freopen("2output.txt", "w", stdout);

    int t;
    cin >> t;

    for (int cas = 1; cas <= t; cas++) {
        int ans = 0;
        int sum = 0;
        int mx;
        string str;
        cin >> mx >> str;

        for (int i=0; i<=mx; i++) {
            if (sum<i) {
                ans += i-sum;
                sum = i;
            }
            sum += str[i] - '0';
        }

        printf("Case #%d: %d\n", cas, ans);
    }

	return 0;
}
