#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <cctype>
#include <set>
#include <bitset>
#include <algorithm>
#include <list>
#include <vector>
#include <sstream>
#include <iostream>
#include<time.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> paii;


#define PI (2*acos(0))
#define ERR 1e-5
#define mem(a,b) memset(a,b,sizeof a)
#define pb push_back
#define popb pop_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define SZ(x) (int)x.size()
#define oo (1<<25)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define Contains(X,item)        ((X).find(item) != (X).end())
#define popc(i) (__builtin_popcount(i))
#define fs      first
#define sc      second
#define EQ(a,b)     (fabs(a-b)<ERR)
#define MAX 12
#define wait getchar()

double naomi[MAX],ken[MAX];
int n,dp[12][1<<12];

int rec(int pos,int ken_mask)
{
    if(ken_mask==0) return 0;

    int &ret=dp[pos][ken_mask];
    if(ret!=-1) return ret;

    ret=0;
    int add;
    for(int i=0;i<n;i++)
    {
        if(ken_mask&(1<<i))
        {
            if(ken[i]<naomi[pos]) add=1;
            else add=0;
            ret=max(ret,rec(pos+1,ken_mask^(1<<i))+add);
        }
    }
    return ret;
}

int main()
{
    freopen("pp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t,ans1,ans2,flag[MAX],flg,loop=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%lf",&naomi[i]);
        for(int i=0;i<n;i++) scanf("%lf",&ken[i]);

        sort(naomi,naomi+n);
        sort(ken,ken+n);

        mem(dp,-1);
        ans1=rec(0,(1<<n)-1);

        mem(flag,0); ans2=0;
        for(int i=0;i<n;i++)
        {
            flg=0;
            for(int j=0;j<n;j++)
                if(flag[j]==0 && ken[j]>naomi[i]) { flag[j]=1; flg=1; break; }
            if(flg==0)
            {
                for(int j=n-1;j>=0;j--)
                    if(flag[j]==0) { flag[j]=1; ans2++; }
            }
        }

        printf("Case #%d: %d %d\n",loop++,ans1,ans2);
    }
    return 0;
}

