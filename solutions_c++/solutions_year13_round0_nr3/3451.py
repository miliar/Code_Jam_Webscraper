#include <cstdio>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <queue>
#include <list>
#include <stack>
#include <fstream>
#include <bitset>
#include <iomanip>
using namespace std;
#define INF 0x7ffffff
#define eps 1e-9
#define pi 3.14159265358979626
#define LL long long
#define clr(a,b) memset(a,b,sizeof(a))
#define FOR(i,a,b) for (int i=a;i<=b;i++)
#define exch(a,b) {int t111=a;a=b;b=t111;}
#define sp struct point
#define sl struct line
#define zero(x) (((x)>0?(x):-(x))<eps)
#define read(a) scanf("%d",&a);

#define N 50500
#define M 600

bool check(LL n)
{
    LL m=1;
    int w=1;
    while(n/m>=10)
    {
        m*=10;
        w+=1;
    }

    LL a,b;
    FOR(i,1,w/2)
    {
        a=n/m;
        b=n%10;
        if (a!=b) return false;

        m/=100;
    }

    return true;
}

int main()
{
    //freopen("subset.in","r",stdin);freopen("subset.out","w",stdout);
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("small2.out","w",stdout);
    //freopen("a.txt","r",stdin);

    int T;
    scanf("%d\n",&T);

    LL a,b;
    FOR(kk,1,T)
    {
        printf("Case #%d: ",kk);
        scanf("%lld%lld",&a,&b);
        LL x,y;
        x=(LL)sqrt(a);
        y=(LL)sqrt(b);
        if (x*x<a) x++;

        LL sum=0;
        for(LL i=x;i<=y;i++)
        if (check(i) && check(i*i)) sum++;
        printf("%lld\n",sum);
    }

    return 0;
}
