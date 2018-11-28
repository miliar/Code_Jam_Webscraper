#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long ll;
const ll MAXN=1005;
struct RE{
       ll x,y;
       }p[MAXN];
ll n,i,l,c[MAXN];
inline bool cmp(RE A,RE B){return ((A.y<B.y)||(A.y==B.y&&A.x<B.x));}
inline bool check(ll i,ll j,ll k){
       ll tmp=(p[j].x-p[i].x)*(p[k].y-p[j].y)-(p[k].x-p[j].x)*(p[j].y-p[i].y);
       if (tmp<0) return 0; else return 1;
}
void graham_scan(){
     sort(p+1,p+n+1,cmp);
     l=2;
     c[1]=1; c[2]=2;
     for (i=3;i<=n;i++){
         l++;
         c[l]=i;
         while (!check(c[l-2],c[l-1],c[l])&&l>2){
               l--;
               c[l]=c[l+1];
         }
     }

     for (i=n-1;i>=1;i--)
     {
         l++;
         c[l]=i;
         while (!check(c[l-2],c[l-1],c[l])&&l>2){
               l--;
               c[l]=c[l+1];
         }
     }
}
ll nn,now;
ll xx[20],yy[20],ans[20];
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    ll T,ca=0;
    scanf("%lld",&T);
    while (T--) {
        scanf("%lld",&nn);
        for (ll i = 0; i<nn; i++)
            scanf("%lld%lld",&xx[i],&yy[i]),ans[i]=nn;

        for (ll k = 0; k<(1<<nn); k++) {
            now=k;
            n=0;
            ll cnt=0;
            while (now) {
                if (now&1) {
                    n++;
                    p[n].x=xx[cnt];
                    p[n].y=yy[cnt];
                }
                cnt++;
                now>>=1;
            }
            graham_scan();
            for (ll i = 0; i<nn; i++)
                for (ll j = 1; j<=l; j++)
                if (xx[i]==p[c[j]].x && yy[i]==p[c[j]].y) {
                    ans[i]=min(ans[i],nn-n);
                    //if (i==nn-1 && ans[i]==2) cout<<k<<endl;
                }
        }

        printf("Case #%lld:\n",++ca);
        for (ll i = 0; i<nn; i++)
            printf("%lld\n",ans[i]);
    }
}
