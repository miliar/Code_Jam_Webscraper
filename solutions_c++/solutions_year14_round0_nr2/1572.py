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

int T,ca,n,i,j,k,l,p;
ld C,F,X,s,v,t,tt,tott,ans;

int main()
{
    //freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
    read(T);
    rep(ca,1,T)
    {
        printf("Case #%d: ",ca);
        cin>>C>>F>>X;
        v=2;s=0;
        ans=ld(1e50);tott=0;
        while(1)
        {
            if(s>X)break;
            if(tott>=ans)break;
            upmin(ans,tott+(X-s)/v);
            t=(C-s)/v;tott+=t;v+=F;s=0;
        }
        cout<<fixed<<setprecision(7)<<ans<<endl;
    }
    	
    scanf("\n");
    return 0;
}
