#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stack>

#define msn(x) (memset((x),0,sizeof((x))))
#define msx(x) (memset((x),0x7f,sizeof((x))))
#define fuck(x) cerr << #x << " <- " << x << endl
#define acer cout<<"sb"<<endl
typedef long long ll;
using namespace std;
#define inf 0x3f3f3f3f
#define eps 1e-8
#define pi acos(-1.0)
string s;
ll n,x;

int mp[5][5]=
{
    0,0,0,0,0,
    0,1,2,3,4,
    0,2,-1,4,-3,
    0,3,-4,-1,2,
    0,4,3,-2,-1
};
int val[500];
int by(int a,int b)
{
   // printf("%d %d\n",a,b);
    if(a<0&&b<0)
    {
        return mp[-a][-b];
    }
    if(a<0&&b>0)return -mp[-a][b];
    if(a>0&&b<0)return -mp[a][-b];
    return mp[a][b];
}
int quick(int a,int b)
{
    int c=b;
    int i=0;
    int re=1;
   /* while((1<<i)<=a)
    {
        if((1<<i)&a)re=by(re,c);
        c=by(c,c);
        i++;
    }*/
    for(i=0;i<a;i++)re=by(re,b);
    return re;
}
bool solve()
{
    int cmp=1;
    for(int i=0;i<n;i++)
    {
        cmp=by(cmp,val[s[i]]);
    }
    cmp=quick(x,cmp);
    if(cmp!=-1)return 0;

    int cmp1=1;
    for(ll i=0;i<n*x;i++)
    {
        int cmp2=1;
        cmp1=by(cmp1,val[s[i%n]]);
        for(ll j=x*n-1;j>i+1;j--)
        {
            cmp2=by(val[s[j%n]],cmp2);
            if(cmp1==2&&cmp2==4)
            {
                return 1;
            }
        }
    }
    return 0;
}
int main()
{
    int T;
    val['i']=2;
    val['j']=3;
    val['k']=4;
    freopen("C-small-attempt5.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&n,&x);
        cin>>s;
        printf("Case #%d: ",cas);
        if(solve())printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
