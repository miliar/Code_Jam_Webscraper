#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int t,i,j,v,k,n,ps,ns,ne,ks,ke,pn,pk,dn,dk;
    float g[1005],b[1005];
    scanf("%d",&t);v=t;
    while(t--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        scanf("%f",&g[i]);
        for(i=0;i<n;i++)
        scanf("%f",&b[i]);
        sort(g,g+n);
        sort(b,b+n);
        pn=pk=0;
        ns=ks=0;
        ne=ke=n-1;
        for(k=0;k<n;k++)
        {
            if(g[ne]>b[ke])
            {pn++;ne--;ks++;}
            else if(g[ne]<b[ke])
            {pk++;ne--;ke--;}
        }
        ps=ns=ks=0;
        dn=dk=0;
        do
        {
            if(b[ks]>g[ns]) ns++;
            else if(b[ks]<g[ns])
            {dn++;ks++;ns++;}
        }
        while(ns<n&&ks<n);
        printf("Case #%d: %d %d\n",v-t,dn,pn);
    }
    return 0;
}
