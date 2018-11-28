#include <bits/stdc++.h>
#define ll long long int
#define ull unsigned long long int
#define s(a) scanf("%lld",&a)
#define pb push_back
#define mp make_pair
#define f first
#define sc second
#define inf 10e16

using namespace std;

int a[100000001];
int ans[1000001];

int getMask(int n)
{
    int w = 0;
    while(n>0) {
        int ww = n%10;
        w = w|(1<<ww);
        n/=10;
    }
    return w;
}

int main()
{
    freopen("inp1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,tt,n,i,j,k,l,w,ww,x,y,z,gotcha;
    gotcha=pow(2,10)-1;
    for(i=1;i<=100000000;i++) {
        a[i]=getMask(i);
    }
    for(i=1000000;i>=1;i--) {
        ww = 0;
        for(j=1;j<=100;j++) {
            w = j*i;
            ww = ww|a[w];
            if(ww == gotcha) {
                break;
            }
        }
        ans[i]=w;
    }
    s(t);
    for(tt=1;tt<=t;tt++) {
        s(n);
        if(n==0) cout<<"Case #"<<tt<<": INSOMNIA\n";
        else cout<<"Case #"<<tt<<": "<<ans[n]<<endl;
    }
    return 0;
}
