#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>

using namespace std;


int main(int argc, char **argv){
    freopen("/Users/Arseniy/All/Int/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/Int/int/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        int d;
        cin >> d;
        vector <int> p;
        p.assign(d, 0);
        int c = 0;
        for (int i=0;i<d;i++){
            cin >> p[i];
            c = max(c, p[i]);
        }
        int ans = 1001;
        for (int mx = 1; mx <= c; mx++){
            int x = 0;
            for (int i=0;i<d;i++){
                x += (p[i]-1)/mx;
            }
            ans = min(ans, x+mx);
        }
        cout << ans << endl;
    }
    
    return 0;
}