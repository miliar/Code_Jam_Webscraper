#include<bits/stdc++.h>
#define PB push_back
using namespace std;

int mc=0;
int d;
int dp(int idx,vector<int> v,int len)
{

    sort(v.begin(),v.end());
    int i,j,k;
    int mn=len-d+v[len-1];
    /*
    for(i=0;i<v.size();i++)
    {
        printf("%d ",v[i]);

    }
    printf("\n");
    system("pause");
    */
    for(i=2;i<=v[len-1]/2;i++)
    {
        int a=v[len-1];
        //printf("Vector Size = %d\n",v.size());
        if(a%i>0)
        {
            v[len-1]=a/i;
            for(j=0;j<i-a%i-1;j++)
                v.PB(a/i);
            for(j=0;j<a%i;j++)
                v.PB(a/i+1);
            mn=min(mn,dp(idx+1,v,v.size()));
            for(j=0;j<i-a%i-1;j++)
                v.pop_back();
            for(j=0;j<a%i;j++)
                v.pop_back();
            v[len-1]=a;
        }
        else
        {
            v[len-1]=a/i;
            for(j=0;j<i-1;j++)
                v.PB(a/i);
            mn=min(mn,dp(idx+1,v,v.size()));
            for(j=0;j<i-1;j++)
                v.pop_back();
            v[len-1]=a;
        }
    }
    //printf("== %d\n",mn);
    return mn;
}

int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,t,i,j,k;
    scanf("%d",&T);
    for(t=0;t<T;t++)
    {
        vector<int> in;
        int sum=0;
        scanf("%d",&d);

        for(i=0;i<d;i++)
        {
            int a;
            scanf("%d",&a);
            mc=max(mc,a);
            in.PB(a);
        }
        sort(in.begin(),in.end());
        printf("Case #%d: %d\n",t+1,dp(0,in,d));
        //printf("Case #%d: %d\n",t+1,mn);
    }
}
