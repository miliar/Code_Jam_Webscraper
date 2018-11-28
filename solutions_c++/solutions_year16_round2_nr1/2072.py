//CodeJam 2016 Round 1B A
//write by Lone Wolf in 2016.05.01
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
int n,m;
string str;
int F[30];
int G[10];
void solve()
{
    int i,j,k;
    memset(F,0,sizeof(F));
    memset(G,0,sizeof(G));
    cin>>str;
    for (i=0;i<str.length();i++)
    {
        F[str[i]-'A']++;
    }
    G[0]=F[25];
    F[25]-=G[0];F[4]-=G[0];F[14]-=G[0];F[17]-=G[0];

    G[2]=F[22];
    F[22]-=G[2];F[14]-=G[2];F[19]-=G[2];

    G[4]=F[20];
    F[20]-=G[4];F[17]-=G[4];F[5]-=G[4];F[14]-=G[4];

    G[6]=F[23];
    F[23]-=G[6];F[8]-=G[6];F[18]-=G[6];

    G[5]=F[5];
    F[5]-=G[5];F[4]-=G[5];F[8]-=G[5];F[21]-=G[5];

    G[7]=F[21];
    F[21]-=G[7];F[4]-=G[7]+G[7];F[13]-=G[7];F[18]-=G[7];

    G[3]=F[17];
    F[17]-=G[3];F[4]-=G[3]+G[3];F[7]-=G[3];F[19]-=G[0];

    G[8]=F[6];
    F[6]-=G[8];F[4]-=G[8];F[8]-=G[8];F[7]-=G[8];F[19]-=G[8];

    G[1]=F[14];
    F[14]-=G[1];F[4]-=G[1];F[13]-=G[1];

    G[9]=F[8];
    F[8]-=G[9];F[4]-=G[9];F[14]-=G[9];F[14]-=G[9];

    for (i=0;i<10;i++)
    {
        if (G[i]>0)
        {
            for (j=0;j<G[i];j++)
                printf("%d",i);
        }
    }
    printf("\n");
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
