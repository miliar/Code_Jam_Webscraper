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
const int N=100010;
const int M=100010;
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
LL n,m;
bool flag[10];
bool cheak()
{
    LL t=n*m;
    while(t>0)
    {
        flag[t%10]=true;
        t=t/10;
    }
    for (int i=0;i<10;i++)
        if (flag[i]==false) return true;
    return false;
}
void solve()
{
    int i,j,k;
    cin>>n;
    if (n==0)
    {
        cout<<"INSOMNIA"<<endl;
        return;
    }
    memset(flag,false,sizeof(flag));
    m=1;
    while (cheak())
    {
        m++;
    }
    cout<<m*n<<endl;
    return;
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int i,T=1;
    scanf("%d",&T);
    for (i=1;i<=T;i++)
    {
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
