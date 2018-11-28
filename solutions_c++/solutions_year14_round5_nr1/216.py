#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;

const int M = 2000000 + 10;

ll n,p,q,r,s;
ll a[M],tot[M];

int main()
{
    int T; cin >> T;
    for (int C=1;C<=T;C++){
        cin >> n >> p >> q >> r >> s;
        for (int i=1;i<=n; i++)
            a[i]=((i-1)*p+q)%r+s;
        
        tot[0]=0;
        for (int i=1;i<=n;i++)
            tot[i]=tot[i-1]+a[i];
            
        int j = 1;
        ll ans = 0;
        for (int i=0;i<n;i++){
            while(tot[j]-tot[i]<=tot[n]-tot[j])
                j++;
            
            ll tot1,tot2,tot3;
            
            tot1 = tot[i];
            tot2 = tot[j]-tot[i];
            tot3 = tot[n]-tot[j];
            ll s1=tot1+tot2+tot3-max(max(tot1,tot2),tot3);
            
            tot1 = tot[i];
            tot2 = tot[j-1]-tot[i];
            tot3 = tot[n]-tot[j-1];
            ll s2=tot1+tot2+tot3-max(max(tot1,tot2),tot3);
            
            ll s=max(s1,s2);
            ans=max(ans,s);
        }
        double out=(double)ans/(double)tot[n];
        printf("Case #%d: %.10f\n",C,out);
    }
    return 0;
}
