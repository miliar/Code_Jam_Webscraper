/*Programmed by Ayush Jaggi*/

#include<bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define F first
#define S second
#define sz size()
#define clr clear()
#define mem(a,b) memset(a,b,sizeof(a))
#define in(type,a) scanf("%" #type,&a)
#define ins(a) scanf("%s",a)
#define out(type,a) printf("%" #type,a)
#define pn printf("\n")
#define ps printf(" ")
#define rep(i,a,b) for(int i=a;i<(int)b;i++)
#define all(a) a.begin(),a.end()
#define repv(i,a) rep(i,all(a))
#define sortv(a) sort(all(a))
#define len length()

#define tc int t;\
in(d,t);\
while(t--)
//#define test int t; in(d,t); while(t--)

#define scn int n;\
in(d,n);
//#define scn int n; in(d,n);

#define scnm int n,m;\
in(d,n);\
in(d,m);
//#define scnm int n; in(d,n); in(d,m)

//iterator example
//for(map<ii,int>::const_iterator it=graph.begin(); it!=graph.end(); it++)
//it->F, it->S operations

//__typeof(a) -> hardware call equivalent to typeof(a)

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<string> vs;

ll MOD=1000000007;

template<class T> inline T gcd(T a, T b)
{
    return b ? gcd(b, a % b) : a;
}

//__gcd(a,b) hardware call

inline ll expo(ll base, int nent)
{
    if(nent==1)
        return base;
    else if(nent&1)
    {
        ll temp=expo(base,nent/2);
        temp=(temp*temp)%MOD*base;
        if(temp>=MOD)
            temp%=MOD;
        return temp;
    }
    else
    {
        ll temp=expo(base,nent/2);
        temp*=temp;
        if(temp>=MOD)
            temp%=MOD;
        return temp;
    }
}

/*
inline void prime()
{
    int s, d, count=0;
    lb=sqrt(n);
    for(s=2; s<=lb; s++)
        if(!pr[s])
        {
            sieve[count++]=s;
            for(d=s*s; d<=n; d+=s)
                pr[d]=1;
        }
}
*/

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out4.txt","w",stdout);
    int x, r, c, n=1, ans[5][5][5];
    rep(i,1,5)
    rep(j,1,5)
    ans[1][i][j]=1;

    ans[2][1][1]=0;
    ans[2][1][3]=0;
    ans[2][3][1]=0;
    ans[2][3][3]=0;
    ans[2][2][1]=1;
    ans[2][1][2]=1;
    ans[2][2][2]=1;
    ans[2][2][3]=1;
    ans[2][3][2]=1;
    ans[2][2][4]=1;
    ans[2][4][2]=1;
    ans[2][1][4]=1;
    ans[2][4][1]=1;
    ans[2][3][4]=1;
    ans[2][4][3]=1;
    ans[2][4][4]=1;

    ans[3][1][1]=0;
    ans[3][1][3]=0;
    ans[3][3][1]=0;
    ans[3][3][3]=1;
    ans[3][2][1]=0;
    ans[3][1][2]=0;
    ans[3][2][2]=0;
    ans[3][2][3]=1;
    ans[3][3][2]=1;
    ans[3][2][4]=0;
    ans[3][4][2]=0;
    ans[3][1][4]=0;
    ans[3][4][1]=0;
    ans[3][3][4]=1;
    ans[3][4][3]=1;
    ans[3][4][4]=0;

    ans[4][1][1]=0;
    ans[4][1][3]=0;
    ans[4][3][1]=0;
    ans[4][3][3]=0;
    ans[4][2][1]=0;
    ans[4][1][2]=0;
    ans[4][2][2]=0;
    ans[4][2][3]=0;
    ans[4][3][2]=0;
    ans[4][2][4]=0;
    ans[4][4][2]=0;
    ans[4][1][4]=0;
    ans[4][4][1]=0;
    ans[4][3][4]=1;
    ans[4][4][3]=1;
    ans[4][4][4]=1;

    tc
    {
        in(d,x);
        in(d,r);
        in(d,c);
        if(ans[x][r][c])
            printf("Case #%d: GABRIEL\n",n++);
        else
            printf("Case #%d: RICHARD\n",n++);
    }
    return 0;
}
