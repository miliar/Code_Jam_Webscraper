#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<queue>
#include<map>
#include<stdlib.h>
#include<algorithm>
#define i_n(a) scanf("%d",&a)
#define l_n(a) scanf("%I64d",&a)
#define LL long long int
#define pb(a) push_back(a)
#define i_p(a) printf("%d\n",a)
#define l_p(a) printf("%I64d\n",a)
#include<limits.h>

using namespace std;
int maximum(int a,int b)
{
    if(a>b)
        return a;
    else
    return b;
}
bool cmp(const pair<int, int>& firs, const pair<int, int>& sec)
 {
  return firs.first < sec.first;
 }
int main()
{
int t,i,j,k;
i_n(t);
for(k=1;k<=t;k++)
{
    int cn=0,a,b,ans;
    i_n(a);
    vector<int>v[17];
    vector<int>v1[17];
    int in[5][5]={0},out[5][5]={0};
    for(i=0;i<17;i++)
        v[i].clear();
    for(i=0;i<17;i++)
        v1[i].clear();
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            i_n(in[i][j]);
            v[i+1].pb(in[i][j]);
        }
    }
    i_n(b);
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            i_n(out[i][j]);
            v1[i+1].pb(out[i][j]);
        }
    }
    for(i=0;i<=16;i++)
    {
        sort(v[i].begin(),v[i].end());
        sort(v1[i].begin(),v1[i].end());
    }
    if(a==b)
    {
         cn=0;
        for(i=0;i<4;i++)
        {
            int idx=0;
             idx=binary_search(v[a].begin(),v[a].end(),v1[b][i]);
             if(idx==1)
             {
                cn++;
                ans=v1[b][i];
             }

        }
        if(cn==0)
            printf("Case #%d: Volunteer cheated!\n",k);
        else if(cn==1)
            printf("Case #%d: %d\n",k,ans);
        else
            printf("Case #%d: Bad magician!\n",k);
     }
     else
     {
         cn=0;
       for(i=0;i<4;i++)
        {
             int idx=0;
             idx=binary_search(v[a].begin(),v[a].end(),v1[b][i]);
             if(idx==1)
             {
                cn++;
                ans=v1[b][i];
             }
        }
        if(cn==1)
            printf("Case #%d: %d\n",k,ans);
        else if (cn==0)
            printf("Case #%d: Volunteer cheated!\n",k);
        else
            printf("Case #%d: Bad magician!\n",k);

        }

}
 return 0;
}
