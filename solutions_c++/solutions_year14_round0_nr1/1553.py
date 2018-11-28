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

int T,n,i,j,k,l,p,r1,r2;
int s1[10],s2[10];

int main()
{
    //freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
    read(T);
    rep(p,1,T)
    {
        read(r1);
        int x;
        rep(i,1,4)
        rep(j,1,4)
        {
            read(x);
            if(i==r1)s1[j]=x;
        }
        read(r2);
        rep(i,1,4)
        rep(j,1,4)
        {
            read(x);
            if(i==r2)s2[j]=x;
        }
        int z=0,cnt=0;
        rep(i,1,4)
        rep(j,1,4)
        if(s1[i]==s2[j])
        {
            ++cnt;
            z=s1[i];
        }
        printf("Case #%d: ",p);
        if(cnt==0)printf("Volunteer cheated!\n");
        else if(cnt>1)printf("Bad magician!\n");
        else printf("%d\n",z);
    }	
    scanf("\n");
    return 0;
}
