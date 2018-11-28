#include <bits/stdc++.h>
using namespace std;

int a[15];

int main()
{
    freopen("A-small-attempt2.txt","r",stdin);
    freopen("outputA.txt","w",stdout);
    int n,t,u,s,v,c,i,j,k;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        j=1;
        memset(a,0,sizeof(a));
        while(1)
        {
            c=0;
            s=n*j;
            u=s;
            while(u!=0)
            {
                v=u%10;
                a[v]++;
                u=u/10;
            }
            for(k=0;k<=9;k++)
            {
                if(a[k]==0)
                    break;
                else c++;
            }
            if(c==10)
                break;
            if(j>1000)
                break;
            j++;
        }
        if(c==10) printf("Case #%d: %d\n",i,s);
        else printf("Case #%d: INSOMNIA\n",i);
    }
return 0;
}
