#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cstdlib>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdio>

using namespace std;

#define mp make_pair
typedef long long llong;
typedef unsigned long long ullong;
typedef pair<int, int> PI;
typedef pair<PI, int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
llong INF = (1LL<<62);
const int inf = (1LL<<30);
const int maxn = (int) 1e9 + 5;

int used[10010];

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    int t = 1;
    while(tc--){
        int n;
        cin >> n;
        int cap;
        cin >> cap;
        VI V(n);
        for(int i = 0; i < n; ++i) cin >> V[i];
        sort(V.begin(), V.end());
        int res = 0;
        memset(used, 0, sizeof(used));
        while(1){
            int f = 0;
            int didit = 0;
            for(int i = 0; i < n && !didit; ++i){
                if(used[i]) continue;
                ++f;
                int got = V[i];
                int left = cap - got;
                for(int j = n - 1; j >= 0; --j){
                    if(used[j]) continue;
                    if(V[j] <= left){
                        used[i] = 1;
                        used[j] = 1;
                        ++res;
                        didit = 1;
                        break;
                    }
                }
                if(!didit){
                    used[i] = 1;
                    ++res;
                    didit = 1;
                }
            }
            if(!didit) break;
        }

        cout << "Case #" << t++ << ": " << res << endl;
    }
    return 0;
}