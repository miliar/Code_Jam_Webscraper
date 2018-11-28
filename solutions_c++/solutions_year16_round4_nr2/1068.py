#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
double p[205],q[205];
int perm[205],perm2[205];
int used[205],used2[205];
double ans1=0;
void dfs2(int d, const int &n, const int &k, int *arr)
{
    if(d==k)
    {
        double ret=1;
        //puts("###");
        for(int i=0;i<n;i++)
        {
            //if(used2[i]) printf("%d ",i);
            if(used2[i]) ret*=p[arr[i]];
            else ret*=q[arr[i]];
        }
        //puts("");
        //printf("ret %f\n",ret);
        ans1+=ret;
        //return ret;
    }
    int i=(d==0)?0:perm2[d-1];
    for(;i<n;i++)
    {
        if(!used2[i])
        {
            used2[i]=true;
            perm2[d]=i;
            dfs2(d+1,n,k,arr);
            used2[i]=false;
        }
    }
    //return 0;
}
double ans=0;
void dfs(int d, const int &n, const int &k)
{
    if(d==k)
    {

        /*for(int i=0;i<k;i++)
            printf("%d ",perm[i]);
        puts("");*/
        ans1=0;
        memset(used2,0,sizeof(used2));
        //puts("###");
        dfs2(0,k,k/2,perm);
        ans=max(ans,ans1);
        return;
    }
    int i=(d==0)?0:perm[d-1];
    for(;i<n;i++)
    {
        if(!used[i])
        {
            used[i]=true;
            perm[d]=i;
            dfs(d+1,n,k);
            used[i]=false;
        }
    }
}
int main()
{
    //memset(used,0,sizeof(used));
    //dfs(0,4,2);
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small.out","w",stdout);
	int T,n,k;
    scanf("%d",&T);
    for(int cases=1;cases<=T;cases++)
	{
	    scanf("%d%d",&n,&k);
	    for(int i=0;i<n;i++)
        {
            scanf("%lf",&p[i]);
            q[i]=1-p[i];
        }
        ans=0;
        memset(used,0,sizeof(used));
        dfs(0,n,k);
        printf("Case #%d: %f\n",cases,ans);
	}
	return 0;
}
