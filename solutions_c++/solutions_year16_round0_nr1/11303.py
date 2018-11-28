#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<map>
#include<queue>
#include <deque>
#include <list>
#include <ctime>
#include <stack>
#include <vector>
#include<iomanip>
#include<set>
#include <bitset>
#include <cassert>
using namespace std;
#define Maxn
#define mod
typedef long long ll;
typedef pair<int, int> PII;
#define FOR(i,j,n) for(int i=j;i<=n;i++)
#define DFR(i,j,k) for(int i=j;i>=k;--i)
#define lowbit(a) a&-a
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define mem(a) memset(a,0,sizeof(a))
#define eps 1e-9
#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define SZ size()
#define BG begin()
#define OP begin()
#define ED end()
#define SQ(x) ((x)*(x))
const int inf = 0x7f7f7f7f;
const double pi = acos(-1.0);
int ans,n;
bool book[11];
bool check()
{
    FOR(i,0,9)
    if(!book[i]) return false;
    return true;
}
void fun(int i)
{   //book[0]=true;
    while(i)
    {
        book[i%10]=true;
        i/=10;
        //book[i%10]=true;
    }
    return ;
}
bool flag;
int main()
{   int T;
    freopen("A-small-attempt0.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取

    freopen("A-small-attempt0.out","w",stdout); //输出重定向，输出数据将保存在out.txt文件中
    scanf("%d",&T);
    FOR(x,1,T)
    {   mem(book);
        scanf("%d",&n);
         flag=true;
        FOR(i,1,100)
        {fun(n*i);
        if(check())
            {ans=n*i;break;}
        if(i==100 && !check()) flag=false;
        }

        if(flag)
        printf("Case #%d: %d\n",x,ans);
        else printf("Case #%d: INSOMNIA\n",x);
    }
    return 0;
}



