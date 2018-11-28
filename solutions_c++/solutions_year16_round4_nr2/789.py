#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define mp make_pair
#define ll long long
#define pb push_back

int x,r,p,sc;

using namespace std;

double a[20];
double d[20][20];
int main() {
    

    cin.sync_with_stdio(false);
    cin.tie(0);
    
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    cout.setf(ios::fixed);
    cout.precision(10);
           
    
    int t;
    cin >> t;
    for (int i1 = 0; i1 < t; i1++) {
        int n,k;
        cin >> n >> k;
        
        for (int i = 0; i < n; i++)
            cin >> a[i];
        
        double ans = 0;
        
        for (int i = 0; i < (1<<n); i++)  {
            int cnt = 0;
            for (int j = 0; j < n; j++)
                if ((i&(1<<j)) > 0) cnt ++;
            if (cnt == k) {
                
                for (int j = 0; j < n; j++)
                    for (int j1 = 0; j1 < n; j1 ++)
                        d[j][j1] = 0;
                
                d[0][0] = 1.0;
                int cnt = 0;
                for (int j = 0; j < n; j++) 
                    if ((i&(1<<j)) > 0) {
                        for (int k = 0; k <= cnt; k++) {
//                            cout << k << " " << cnt-k << " == " << d[k][cnt-k] << "\n";
                            //k cnt-k
                            d[k+1][cnt-k] += d[k][cnt-k]*a[j];
                            d[k][cnt-k+1] += d[k][cnt-k]*(1-a[j]);
                        }
                        cnt ++;
                    }
                ans = max(ans,d[k/2][k/2]);
//                cout << i << " " << d[k/2][k/2] << "\n";
            }
            
        }
        cout << "Case #" <<i1+1 << ": " << ans << "\n";
    }

    return 0;
}
