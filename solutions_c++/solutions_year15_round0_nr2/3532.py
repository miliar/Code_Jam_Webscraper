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

int getAns(int n, vector<int> a) {
    int bestans = md;
    for (int k = 1; k < 1500; k++) {
        vector<int> temp = a;
        int cur_ans = k;
        for (int i = 0; i < temp.size(); i++) {
            if (temp[i] > k) {
                temp.push_back(temp[i] - k);
                cur_ans++;
            }
        }
        if (cur_ans < bestans) {
            bestans = cur_ans;
        }
    }
    return bestans;
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
    for (int i = 1; i <= t; i++) {
        int d;
        scanf("%d", &d);
        vector<int> a;
        for (int i = 0; i < d; i++) {
            int x;
            scanf("%d", &x);
            a.push_back(x);
        }
        cout << "Case #" << i << ": " << getAns(d, a) << endl;
    }
    return 0;
}
