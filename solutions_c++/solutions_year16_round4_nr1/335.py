#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
// p 0  r 1 s 2
vector<int> ans;
int ch=0;
int n,r,p,s;
int cmp(vector<int> a,int d1,vector<int> b,int d2,int d3)
{
    for(int i=0;i<d3;i++)
    if(a[d1+i]>b[d2+i]) return 1;
    else if(a[d1+i]<b[d2+i]) return 0;
    return 0;
}
void update(vector<int> a)
{
    for(int i=1;i<=n;i++)
    {
        int dt=1<<i;
        for(int j=0;j<(1<<n);j+=dt)
        {
            if(cmp(a,j,a,j+dt/2,dt/2))
            for(int k=0;k<dt/2;k++) swap(a[j+k],a[j+dt/2+k]);
        }
    }
    if(ch==0)
    {
        ch=1;
        ans=a;
    }
    else if(cmp(ans,0,a,0,1<<n))
    ans=a;
}
main()
{
    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        ch=0;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        for(int i=0;i<3;i++)
        {
            vector<int> a;
            a.push_back(i);
            for(int j=1;j<=n;j++)
            {
                vector<int> b;
                for(int k=0;k<a.size();k++)
                {
                    int cur=a[k];
                    if(cur==0)
                    {
                        b.push_back(0);
                        b.push_back(1);
                    }
                    else if(cur==1)
                    {
                        b.push_back(1);
                        b.push_back(2);
                    }
                    else if(cur==2)
                    {
                        b.push_back(0);
                        b.push_back(2);
                    }
                }
                a=b;
            }
            int d1=0,d2=0,d3=0;
            for(int j=0;j<a.size();j++)
            {
                if(a[j]==0) d1++;
                else if(a[j]==1) d2++;
                else d3++;
            }
            if(d1!=p||d2!=r||d3!=s) continue;
            update(a);
        }
        printf("Case #%d: ",++cas);
        if(ch==0) printf("IMPOSSIBLE\n");
        else
        {
            for(int i=0;i<ans.size();i++)
            if(ans[i]==0) printf("P");
            else if(ans[i]==1) printf("R");
            else printf("S");
            printf("\n");
        }
    }
}
