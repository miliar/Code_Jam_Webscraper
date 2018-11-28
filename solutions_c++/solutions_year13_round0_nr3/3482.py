#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <limits.h>

typedef unsigned long long ULL;
typedef long long LL;

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) ((a>0)?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define PII pair<int,int>
#define MOD 1000000007
using namespace std;
vector<int>vec,vec1;

int ispalin(int num)
{
    vec.clear();
    vec1.clear();
    while(num>0)
    {
        int x=num%10;
        num=num/10;

        vec.push_back(x);
    }
    vec1=vec;
    reverse(vec.begin(),vec.end());

    /*for(int i=0;i<vec.size();i++)
    {
        printf("%d ",vec[i]);
    }
    printf("\n");*/
    /*for(int i=0;i<vec1.size();i++)
    {
        printf("%d ",vec1[i]);
    }*/
    if(vec==vec1)
    return 1;
    else return 0;
}
int main()
{
    int t,n,n1,n2;
    int ctr=0;
    scanf("%d",&t);
    while(t--)
    {
        ctr++;
        scanf("%d %d",&n1,&n2);
        int ans=0;
        for(int i=n1;i<=n2;i++)
        {
            int sqr=sqrt(i);
            if((sqr*sqr)!=i)
            {continue;}
            if(ispalin(i) && ispalin(sqr))
            {
                //printf("%d\n",i);
                ans++;
            }
        }

        printf("Case #%d: %d\n",ctr,ans);
    }
    return 0;
}
