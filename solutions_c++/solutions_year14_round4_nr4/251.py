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

int T,ca,n,m,i,j,k,l,p;
int a[111];
string s[11];
set<string> S[11];

int main()
{
    freopen("2.in","r",stdin);
    //freopen("2.out","w",stdout);
	for(read(T);T;T--)
	{
        printf("Case #%d: ",++ca);
        int best=-1,num=0;
        read(n,m);
        rep(i,1,n)cin>>s[i];
        int u=1;rep(i,1,n)u=u*m;u--;
        REP(pos,0,u)
        {
            int x0=pos;rep(i,1,n)a[i]=x0%m,x0/=m;
            
            rep(i,0,m)S[i].clear();
            rep(i,1,n)
            {
                for(j=0;j<=s[i].length();j++)
                S[a[i]].insert(s[i].substr(0,j));
            }
            int tot=0;rep(i,0,m-1)tot+=S[i].size();
            if(tot>best)best=tot,num=1;
            else if(tot==best)num++;
        }
        printf("%d %d\n",best,num);
    }
	scanf("\n");
    return 0;
}
