#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <deque>
#include <cmath>
#include <set>
#include <iomanip>
#include <ctime>
#include <sstream>
#include <map>
using namespace std;

#define forn(i,n) for(int i = 0; i < (int)n; ++i)
#define _mp(a,b) make_pair(a,b)
#define _pb(x) push_back(x)
#define mins(a,b) a = min(a,b)
#define maxs(a,b) a = max(a,b)

int main() {
//    srand(263515);
   ios_base::sync_with_stdio(false);
//    cout << fixed;
//    cout << setprecision(9);
   freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
    int T = 0;
    cin >> T;
    forn(test, T)
    {
        int n,x;
        cin >> n >> x;
        vector<int> mask(x+1,0);
        forn(i,n)
        {
            int cur = 0;
            cin >> cur;
            ++mask[cur];
        }
        int ans = 0;
        int index = x;
        while (index >= 0)
        {
            if (mask[index] == 0)
            {
                --index;
            }
            else
            {
                ++ans;
                --mask[index];
                for(int i = x - index; i >= 0; --i)
                {
                    if (mask[i] > 0)
                    {
                        --mask[i];
                        break;
                    }
                }
            }
        }
        cout << "Case #" << test+1 << ": " << ans << "\n";
    }



    return 0;
}
