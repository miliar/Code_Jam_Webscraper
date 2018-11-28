#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<bitset>
#include<iomanip>
#include<iostream>
#include<cmath>
using namespace std;
#define rep(i,x,y) for(i=x;i<=y;i++)
#define _rep(i,x,y) for(i=x;i>=y;i--)
#define REP(i,x,y) for(int i=(x);i<=(y);i++)
#define _REP(i,x,y) for(int i=(x);i>=(y);i--)
#define CL(S,x) memset(S,x,sizeof(S))
#define CP(S1,S2) memcpy(S1,S2,sizeof(S2))
#define ALL(x,S) for(x=S.begin();x!=S.end();x++)
#define pb push_back
#define IN insert
#define ER erase
#define BE begin()
#define ED end() 
#define LB lower_bound
#define UB upper_bound
#define mp make_pair
#define fi first
#define se second
#define upmin(x,y) x=min(x,y)
#define upmax(x,y) x=max(x,y)
#define COUT(S,x) cout<<fixed<<setprecision(x)<<S<<endl
template<class T> inline void read(T&x){bool fu=0;char c;for(c=getchar();c<=32;c=getchar());if(c=='-')fu=1,c=getchar();for(x=0;c>32;c=getchar())x=x*10+c-'0';if(fu)x=-x;};
template<class T> inline void read(T&x,T&y){read(x);read(y);}
template<class T> inline void read(T&x,T&y,T&z){read(x);read(y);read(z);}
inline char getc(){char c;for(c=getchar();c<=32;c=getchar());return c;}

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

int T,ca,n,i,j,k,l,p;
int s[1010],a[1010],o[1010];
int A(int i,int t){for(;i<=n;i+=i&-i)s[i]+=t;}
int S(int i){int ans=0;for(;i;i-=i&-i)ans+=s[i];return ans;}

int main()
{
    freopen("1.in","r",stdin);freopen("1.out","w",stdout);
	for(read(T);T;T--)
	{
        printf("Case #%d: ",++ca);
        read(n);
        rep(i,1,n)read(a[i]),o[i]=a[i];
        
        sort(o+1,o+1+n);j=1;rep(i,2,n)if(o[i]!=o[i-1])o[++j]=o[i];o[0]=j;
        rep(i,1,n)a[i]=LB(o+1,o+1+o[0],a[i])-o;
        //rep(i,1,n)printf("%d ",a[i]);printf("\n");
        /*
        int best=int(1e9);
        int tt=0;
        rep(i,0,n)
        {
            int ans=0;
            CL(s,0);_rep(j,i,1)ans+=S(a[j]),A(a[j],1);
            CL(s,0);rep(j,i+1,n)ans+=S(a[j]),A(a[j],1);
            //REP(k1,0,i)REP(k2,k1,i)ans+=(a[k1]>a[k2]);
            //REP(k1,i+1,n)REP(k2,k1,n)ans+=(a[k1]<a[k2]);
            
            if(ans<best)tt=i;
            upmin(best,ans);
        }
        */
        
        int best=0;
        rep(i,1,n)
        {
            int tot1=0,tot2=0;
            rep(j,1,i-1)if(a[j]>a[i])tot1++;
            rep(j,i+1,n)if(a[j]>a[i])tot2++;
            best+=min(tot1,tot2);
        }
        //printf("%d\n",tt);
        printf("%d\n",best);
    }
	
    return 0;
}
