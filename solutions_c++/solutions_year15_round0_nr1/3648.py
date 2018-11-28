#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <vector>
#include <string>
#include <string.h>
#include <ctime>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <iomanip>
#include <assert.h>
#include <deque>

#ifdef WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif // WIN32

#define INF (1LL << 30)
#define md 1000000007
#define F first
#define S second
#define ll long long
#define mp make_pair
#define pb push_back
#define next(i) (i) + ((i) & (-i))
#define prev(i) (i) - ((i) & (-i))

using namespace std;

int getAns(int smax, string s) {
    int ans = 0;
    int cur = 0;
    for (int i = 0; i < s.size(); i++) {
        if (cur < i) {
            ans += (i - cur);
            cur = i;
        }
        cur += (s[i] - '0');
    }
    return ans;
}


int main() {
    #ifndef ONLINE_JUDGE
            freopen("input.txt", "r", stdin);
            freopen("output.txt", "w", stdout);
    #else
            //freopen("input.txt", "r", stdin);
            //freopen("output.txt", "w", stdout);
    #endif //ONLINE_JUDGE
    int t;
    scanf("%d", &t);
    for (int i = 1;  i <= t; i++) {
        int n;
        string s;
        cin >> n >> s;
        cout << "Case #" << i << ": " << getAns(n, s) << endl;
    }

    return 0;
}
