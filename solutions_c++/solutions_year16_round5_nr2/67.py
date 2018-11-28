#include<set>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<string>
#include<time.h>
#include<math.h>
#include<memory>
#include<vector>
#include<bitset>
#include<fstream>
#include<stdio.h>
#include<utility>
#include<sstream>
#include<string.h>
#include<iostream>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int father[105];
vector<int> child[105];
string c[105];
char a[105];
int finds[105];
string ans="";
int n;
bool visit[105];
void tries()
{
    memset(visit,false,sizeof(visit));
    int i;
    for (i=0;i<n;i++)
    {
        int t=rand()%n;
        if (visit[t])
        {
            i--;
            continue;
        }
        for (;;)
        {
            if ((father[t]==-1)||(visit[father[t]]))
            {
                break;
            }
            t=father[t];
        }
        visit[t]=true;
        ans[i]=a[t];
    }
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int t;
    scanf("%d",&t);
    int zu;
    for (zu=0;zu<t;zu++)
    {
        printf("Case #%d: ",zu+1);
        int i;
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%d",&father[i]);
            father[i]--;
        }
        scanf("%s",a);
        int m;
        scanf("%d",&m);
        ans=a;
        for (i=0;i<m;i++)
        {
            cin>>c[i];
            finds[i]=0;
        }
        for (i=0;i<10000;i++)
        {
            tries();
            int j;
            for (j=0;j<m;j++)
            {
                if (ans.find(c[j])!=-1) finds[j]++;
            }
        }
        for (i=0;i<m;i++)
        {
            if (finds[i]==10000) finds[i]--;
        }
        for (i=0;i<m-1;i++)
        {
            printf("0.%04d ",finds[i]);
        }
        printf("0.%04d\n",finds[i]);
    }
    return 0;
}
