/*
    Look at me!
    Look at me!
    Look at how large the monster inside me has become!
*/
#include<fstream>
#include<iostream>
#include<cstdio>
#include<map>
#include<typeinfo>
#include<set>
#define FIT(a,b) for(vector<int >::iterator a=b.begin();a!=b.end();a++)
#define FITP(a,b) for(vector<pair<int,int> >::iterator a=b.begin();a!=b.end();a++)
#define RIT(a,b) for(vector<int>::reverse_iterator a=b.end();a!=b.begin();++a)
#include<stack>
#define ROF(a,b,c) for(int a=b;a>=c;--a)
#include<vector>
#include<algorithm>
#define FOR(a,b,c) for(int a=b;a<=c;++a)
#define REP(a,b) for(register int a=0;a<b;++a)
#include<cstring>
#include<bitset>
#include<cmath>
#include<iomanip>
#define f cin
#define g cout
#include<queue>
#define INF 0x3f3f3f3f
#define debug cerr<<"OK";
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ld long double
#define ll long long
#define ull unsigned long long
#define eps 1.e-7
#define BUFMAX 10100100
#define N 101000
#define mod 1000000007
using namespace std;
/*
int dx[]={-1,-1,-1,0,1,1,1,0};
int dy[]={-1,0,1,1,1,0,-1,-1};
*/
int a[305][305];
int n,x,r,K,cur,oi[N],oj[N],ok[N],T;
char s[N];
int main ()
{

    #ifndef ONLINE_JUDGE
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    #endif

    FOR(i,1,300)
    a['1'][i]=a[i]['1']=i;

    a['i']['i']=-'1';
    a['j']['j']=-'1';
    a['k']['k']=-'1';
    a['i']['j']='k';
    a['i']['k']=-'j';
    a['j']['i']=-'k';
    a['j']['k']='i';
    a['k']['i']='j';
    a['k']['j']=-'i';

    f>>T;
    FOR(t,1,T)
    {
        f>>n>>x;
        f>>(s+1);
        r=0;
        if(x>8)
        {
            x%=8;
            x+=8;
        }
        FOR(i,1,x)
        FOR(j,1,n)
        s[++r]=s[j];
        K=0;
        cur='1';
        memset(ok,0,sizeof(ok));
        memset(oi,0,sizeof(oi));
        memset(oj,0,sizeof(oj));
        FOR(i,1,r)
        {
            if(cur<0)
            cur=-a[-cur][s[i]];
            else
            cur=a[cur][s[i]];
            oi[i]=oi[i-1];
            oj[i]=oj[i-1];
            if(cur=='i')
                oi[i]=1;
            if(oi[i]&&cur=='k')
                oj[i]=1;
            if(oj[i]&&cur==-'1')
                ok[i]=1;
            if(ok[i]==1&&cur==-'1'&&i==r)
                K=1;
        }
        g<<"Case #"<<t<<": ";
        if(K)
            g<<"YES\n";
        else
            g<<"NO\n";
    }




    return 0;
}
