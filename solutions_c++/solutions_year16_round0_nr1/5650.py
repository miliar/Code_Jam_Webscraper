#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long ll;

#define pb push_back
#define mp make_pair
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define file freopen("1.txt","r",stdin)
#define llel y1
#define x MAXN


ll n,a[12],k,q,ans;
bool f,g;

main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.txt","w",stdout);

    cin >> q;

    for(int jj = 1; jj <= q; ++jj){
        cin >> n;

        for(int i = 0; i <= 9; ++i){
            a[i] = 0;
        }

        ans = 0;
        g = false;

        for(int i = 1; i <= 1000; ++i){
            k = i * n;

            while(k > 0){
                a[k % 10] = 1;
                k/=10;
            }

            f = true;
            for(int j = 0; j <= 9; ++j){
                if (!a[j]){
                    f = false;
                    break;
                }
            }
            if (f){
                g = true;
                ans = i * n;
                break;
            }
        }

        if (g) cout << "Case #" << jj << ": " << ans << "\n";
        else cout << "Case #" << jj << ": " << "INSOMNIA\n";
    }
}
