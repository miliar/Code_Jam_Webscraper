#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        int n,m,k;
        cin >> n >> m >> k;
        if (n > m){
            swap(n, m);
        }
        if ((k <= 4) || (n <= 2)){
            cout << k << endl;
            continue;
        }
        int ans = n*m;
        for (int q = 3;q<=n;q++){
            for (int w = 3; w <= m; w++){
                if (q*w < k) continue;
        for (int i=1;i<q;i++){
            for (int j=1;j+i<=q;j++){
                for (int a=1;a<w;a++){
                    for (int b=1;b+a<=w;b++){
                        int c = q*w - (i*(i+1))/2 - (j*(j+1))/2 -(a*(a+1))/2-(b*(b+1))/2;
                        int t = 2*(q+w)-(i+j+a+b+4);
                        int e = k-c;
                        if (e > 0)
                            t+=e;
                        ans = min(ans, t);
                    }
                }
            }
        }
            }
        }
        cout << ans << endl;
    }
    return 0;
}
