//Google CodeJam Qualification A
//write by Lone Wolf in 2016.04.09
#pragma comment(linker, "/STACK:102400000,102400000")
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#define PI (acos(-1.0))
#define lowbit(x) (x&(-x))
#define sspeed ios_base::sync_with_stdio(0);cin.tie(0)
typedef long long LL;
using namespace std;
const int MOD=1000000007;
const int INF=0x3f3f3f3f;
const int N=1000010;
const int M=10000010;
const int Mat=110;
typedef double Matrix[Mat][Mat];
const double eps=1e-10;
inline int readint()
{
    char c=getchar();
    while (c<'0'||c>'9') c=getchar();
    int x=0;
    while ('0'<=c&&c<='9')
    {
        x=x*10+c-'0';
        c=getchar();
    }
    return x;
}
int buf[10];
inline void writeint(int i)
{
    int p=0;
    if (i==0) p++;
    else while (i)
    {
        buf[p++]=i%10;
        i/=10;
    }
    for (int j=p-1;j>=0;j--) putchar('0'+buf[j]);
}
int n,m,l;
LL Prime[N];
LL ans[11];
int EulerPrimeScreen()///Å·À­É¸·¨
{
    bitset<M>F;
    LL i,j;
    F.set();
    for (i=2;i<M;i++)
    {
        if (F[i]) Prime[n++]=i;
        for (j=0;j<n;j++)
        {
            if (i*Prime[j]>M) break;
            F[i*Prime[j]]=false;
            if (i%Prime[j]==0) break;
        }
    }
    return 0;
}
void init()
{
    n=0;
    EulerPrimeScreen();
    l=n;
}
LL IsPrime(LL x)
{
    if (x<=1) return 0;
    int i;
    for (i=0;i<l;i++)
    {
        if (x==Prime[i]) return 0;
        if (x%Prime[i]==0) return Prime[i];
    }
    return 0;
}
int flag[20];
bool check(int x)
{
    int i,j,s;
    s=0;
    while (x>0)
    {
        flag[s]=x&1;
        x=x>>1;
        s++;
    }
    memset(ans,0,sizeof(ans));
    for (i=s-1;i>=0;i--)
    {
        for (j=2;j<=10;j++)
        {
            ans[j]=ans[j]*j;
            ans[j]=ans[j]+flag[i];
        }
    }

    for (i=2;i<11;i++)
    {
        ans[i]=IsPrime(ans[i]);
        if (ans[i]==0) return false;
    }
    return true;
}
void solve()
{
    int i,j,k;
    scanf("%d%d",&n,&m);
    k=1<<(n);
    i=1<<(n-1);
    i++;
    j=0;
    while (i<k)
    {
        if (check(i))
        {
            for (int a=n-1;a>=0;a--) cout<<flag[a];
            for (int a=2;a<=10;a++) cout<<" "<<ans[a];
            cout<<endl;
            j++;
            if (j==m) return;
        }
        i+=2;
    }
    return;
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int i,T=1;
    init();
    scanf("%d",&T);
    for (i=1;i<=T;i++)
    {
        cout<<"Case #"<<i<<":"<<endl;
        solve();
    }
    return 0;
}
