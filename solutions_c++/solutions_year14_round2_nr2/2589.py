/*Programmed by Ayush Jaggi*/

#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<ctype.h>
#include<climits>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<set>
#include<deque>
#include<list>
#include<utility>
#include<fstream>
#include<iterator>
#include<ctime>
#include<deque>
#include<numeric>
#include<functional>
#include<sstream>

using namespace std;
#define MOD 1000000007
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define L(i,x,y) for(i=x;i<y;i++)
#define l0(i,x) for(i=0;i<x;i++)
#define l1(i,x) for(i=1;i<x;i++)
#define pd(n) printf("%d",n)
#define pdn(n) printf("%d\n",n)
#define pds(n) printf("%d ",n)
#define plld(n) printf("%lld",n)
#define plldn(n) printf("%lld\n",n)
#define pllds(n) printf("%lld ",n)
#define pc(n) printf("%c",n)
#define pn printf("\n")
#define ps printf(" ")
#define plf(n) printf("%.6lf",n)
#define plfn(n) printf("%.6lf\n",n)
#define plfs(n) printf("%.6lf ",n)
#define psn(n) printf("%s\n",n)
#define pss(n) printf("%s ",n)
#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%ld",&n)
#define slld(n) scanf("%lld",&n)
#define slf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define sc(n) scanf("%c",&n)
#define mem(n,m) memset(n,m,sizeof(n))
#define W(t) while(t--)

typedef long long int LL;
typedef vector<int> VD;
typedef vector< vector<int> > V2D;
typedef vector<string> VS;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("OutputBsmall.out","w",stdout);
    LL a, b, k, count, i, j;
    int t, l;
    sd(t);
    l0(l,t)
    {
        slld(a);
        slld(b);
        slld(k);
        count=0;
        l0(i,a)
        l0(j,b)
        if((i&j)<k)
            count++;
        printf("Case #%d: %lld\n",l+1,count);
    }
    return 0;
}
