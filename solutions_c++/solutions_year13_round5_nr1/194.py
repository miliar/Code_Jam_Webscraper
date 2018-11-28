#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

long long b;
vector< long long > ost;
map< long long, long long > kol;
int n;

void solve() {
    cout.setf(ios::fixed);
    cout.precision(10);
    cin >> b >> n;
    kol.clear();
    
    ost.resize(n);
    for (int i = 0; i < n; i++)
    {
        cin >> ost[i];
        kol[ost[i]]++;
    }
    
    kol[0] = 37 - n;
    long double ans = 0.0;
    for (long long curbet = 1; true; curbet++) 
        for (long long cut = 0; cut < 37; cut++)
        {
            long long curcut = cut;
            long long need = 0;
            long long curprof = 0;
            long long possiblecells = 0;
            bool ok = false;
            for (map< long long, long long >::reverse_iterator it = kol.rbegin(); it != kol.rend() && need <= b; it++)
            {
                if (it->first <= curbet)
                {
                    long long willcut = min(it->second, curcut);
                    
                    need += (curbet - it->first) * it->second + willcut;
                    curprof += (curbet - it->first) * 36 * (it->second - willcut);
                    possiblecells += it->second - willcut;
                    
                    if (willcut != it->second)
                        ok = true;
                    curcut -= willcut;
                }
            }
            if (!ok)
                break;
            if (curcut)
                break;
            if (cut == 0 && need > b) {
                cout << ans << endl;
                return;
            }
            if (need > b)
                break;
           
            
            long double curans = ((long double)(1.0) * (curprof)) / (possiblecells) - need;
            ans = max(ans, curans);
        }
        
    cout << ans << endl;
}

int main() {
    #ifdef OFFLINE
    freopen("A_input.txt","r", stdin);
    freopen("A_output.txt","w", stdout);
    #endif
    int t;
    scanf("%d\n", &t);
    for (int testnum = 0; testnum < t; testnum++) {
        printf("Case #%d: ", testnum + 1);
        solve();
    }
}
