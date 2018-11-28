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
//	freopen("2input.txt", "r", stdin);
//	freopen("2output.txt", "w", stdout);

    int t;
    cin >> t;

    for (int cas = 1; cas <=t; cas++) {
        int n;
        sd(n);
        int arr[n];
        for (int i=0; i<n; i++)
            sd(arr[i]);

        int ans = 0;
        int sum = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i] < arr[i-1])
                ans += arr[i-1] - arr[i];
        }

        printf("Case #%d: %d ", cas, ans);

        ans = 0;

        int low = 1;
        int high = 10000;

        bool zero = true;

        for (int i = 1; i < n; i++) {
            if (arr[i]<arr[i-1]) {
                zero = false;
                break;
            }
        }

        if (zero) {
            puts("0");
            continue;
        }

        for (int i = 0; i < n-1; i++)
            sum += arr[i];

        while (low < high) {
            int mid = low + (high - low)/2;
            ans = 0;
            for (int i = 0; i < n-1; i++) {
                if (arr[i] > mid) {
                    if (arr[i+1] < arr[i] - mid) {
                        low = mid + 1;
                        goto DONE;
                    } else {
                        ans += mid;
                    }
                } else {
                    ans += arr[i];
                }
            }
            high = mid;
            sum = ans;
            DONE:;
        }

        cout << sum << endl;
    }


	return 0;
}
