#include<cstdio>
#include<cmath>
#include<stdlib.h>
#include<map>
#include<set>
#include<time.h>
#include<vector>
#include<queue>
#include<string>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define eps 1e-8
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
int n;
struct hike
{
    double st;
    double v;
} her[22222];
bool cmp(hike a,hike b)
{
    return ((360.0-a.st)/a.v)>((360.0-b.st)/b.v);
}
int numh;
int main()
{
//    printf("%f\n",(360.0-276.0)/360*710914169.0/117033118*360+168);
    freopen("C-small-1-attempt2.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
//    printf("%d\n",t);
    for(int cas=1; cas<=t; cas++)
    {
        int ans=99999999;
        memset(her,0,sizeof(her));
        numh=0;
        scanf("%d",&n);
//        printf("%d\n",n);
        for(int i=0; i<n; i++)
        {
            int st,num,vv;
            scanf("%d%d%d",&st,&num,&vv);
//            printf("%d %d %d\n",st,num,vv);
            for(int j=0; j<num; j++)
            {
                her[numh].st=st;
                her[numh++].v=(360.0)/(vv+j);
            }
        }
//        sort(her,her+numh,cmp);
        for(int i=0;i<numh;i++)
        {
            int term=0;
            double t=(360.0-her[i].st)/her[i].v;
            for(int j=0;j<numh;j++)
            {
                if(i==j)
                    continue;
                if(her[j].st+t*her[j].v<=360)
                    term++;
                if(her[j].st+t*her[j].v>=720)
                    term++;
            }
            ans=min(ans,term);
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
