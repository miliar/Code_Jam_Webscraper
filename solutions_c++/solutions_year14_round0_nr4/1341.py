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
#define CL(S,x) memset(S,x,sizeof(S))
#define CP(S1,S2) memcpy(S1,S2,sizeof(S2))
#define ALL(x,S) for(x=S.begin();x!=S.end();x++)
#define sqr(x) ((x)*(x))
#define mp make_pair
#define fi first
#define se second
#define upmin(x,y) x=min(x,y)
#define upmax(x,y) x=max(x,y)
#define pb push_back
#define COUT(S,x) cout<<fixed<<setprecision(x)<<S<<endl

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

template<class T> inline void read(T&x){bool fu=0;char c;for(c=getchar();c<=32;c=getchar());if(c=='-')fu=1,c=getchar();for(x=0;c>32;c=getchar())x=x*10+c-'0';if(fu)x=-x;};
template<class T> inline void read(T&x,T&y){read(x);read(y);}
template<class T> inline void read(T&x,T&y,T&z){read(x);read(y);read(z);}
inline char getc(){char c;for(c=getchar();c<=32;c=getchar());return c;}

int T,ca,n,i,j,k,l,r,p,ans1,ans2;
ld a[1010],b[1010];

set<ld> S2;
set<ld>::iterator it;

int main()
{
    //freopen("1.in","r",stdin);freopen("1.out","w",stdout);
    read(T);
    rep(ca,1,T)
    {
        read(n);rep(i,1,n)cin>>a[i];rep(i,1,n)cin>>b[i];
        sort(a+1,a+1+n);
        ans1=ans2=0;
        
        S2.clear();rep(i,1,n)S2.insert(b[i]);
        rep(i,1,n)
        {
            it=S2.upper_bound(a[i]);
            if(it==S2.end())ans2++;
            else S2.erase(it);
        }
        
        S2.clear();rep(i,1,n)S2.insert(b[i]);
        
        l=1;r=n;
        while(l<=r)
        {
            if(a[l]>*S2.begin())l++,ans1++,S2.erase(*S2.begin());
            else S2.erase(*S2.rbegin()),l++;
        }
        printf("Case #%d: ",ca);
        printf("%d %d\n",ans1,ans2);
    }
    	
    scanf("\n");
    return 0;
}
