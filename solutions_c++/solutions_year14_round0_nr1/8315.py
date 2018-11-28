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
    freopen("A-small-attempt1.in","r",stdin);
    freopen("Output1.out","w",stdout);
    int t, m1[5][5], m2[5][5], c1, c2, i, j, flag, ans, c, count=0;
    sd(t);
    W(t)
    {
        flag=0;
        ans=1;
        sd(c1);
        l0(i,4)
        l0(j,4)
        sd(m1[i][j]);
        sd(c2);
        l0(i,4)
        l0(j,4)
        sd(m2[i][j]);
        l0(i,4)
        l0(j,4)
        if(m1[c1-1][i]==m2[c2-1][j])
            if(flag)
                ans=2;
            else
            {
                flag=1;
                c=m1[c1-1][i];
            }
        if(!flag)
            ans=3;
        count++;
        if(ans==1)
            printf("Case #%d: %d\n",count,c);
        else if(ans==2)
            printf("Case #%d: Bad magician!\n",count);
        else printf("Case #%d: Volunteer cheated!\n",count);
    }
    return 0;
}
