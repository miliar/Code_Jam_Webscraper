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

int n,r,c;
bool solve()
{
    if(r>c)swap(r,c);
    if(n==1)return 1;
    if(n==2)
    {
        if(r*c%n==0)return 1;
        return 0;
    }
    if(n==3)
    {
        if(r*c%n==0)
        {
            if(r==1)return 0;
            return 1;
        }
        return 0;
    }
    if(n==4)
    {
        if(r*c%n==0)
        {
            if(c==2)return 0;
            if(r<3)return 0;
            return 1;
        }
        return 0;
    }
}
int main()
{
    int T;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d",&T);

    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d%d%d",&n,&r,&c);
        printf("Case #%d: ",cas);
        if(solve())printf("GABRIEL\n");
        else printf("RICHARD\n");
    }
    return 0;
}
