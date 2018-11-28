#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<ctime>
#include<complex>
#define ft first
#define sd second
#define pb push_back
#define mkp make_pair
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)<(b)?(b):(a))
using namespace std;
typedef long long LL;
typedef pair<int,int> Pair;
const int inf=0x3f3f3f3f;
const double eps=1e-6;
const int mod=1e9+7;
const int maxn=110;
int n,j;
int ans[15];
int bin[15];
void getbin(int a)
{
    int p=n;
    while(a)
    {
        bin[p--]=a%2;
        a/=2;
    }
}
LL get(int b)
{
    LL rt=bin[1];
    for(int i=2;i<=n;i++)
        rt=rt*b+bin[i];
    //cout<<rt<<endl;
    return rt;
}
bool ok(int a)
{
    for(int i=2;i<=10;i++)
    {
        LL t=get(i);
        LL tt=min(t-1,(LL)sqrt(t)+2);
        bool ok=0;
        for(int j=2;j<=tt;j++)
        {
            if(t%j==0)
            {
                ans[i]=j;
                ok=1;
                break;
            }
        }
        if(ok==0) return 0;
    }
    return 1;
}
void print(int a)
{
    for(int i=1;i<=n;i++)
        printf("%d",bin[i]);
    printf(" ");
}
int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%d%d",&n,&j);
        printf("Case #%d:\n",kase);
        int a=(1<<(n-1))+1,b=(1<<n)-1;
        for(int i=a;i<=b;i++)
        {
            if((i&1)==0) continue;
            getbin(i);
            if(ok(i))
            {
                print(i);
                for(int i=2;i<=9;i++)
                    printf("%d ",ans[i]);
                printf("%d\n",ans[10]);
                j--;
                if(!j) break;
            }
        }
    }
}
