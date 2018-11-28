#include <bits/stdc++.h>

using namespace std;


int main()
{
    freopen("prot.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long i,j,k,l,m,n,p,q,rel=0;
    cin>>n;
    while(n--)
    {
        cin>>m;
        rel++;
        if(m==0)
        {
            cout<<"Case #"<<rel<<": INSOMNIA"<<endl;
        }
        else
        {
            int ara[10];
            for(i=0;i<10;i++) ara[i]=0;
            i=1;
            while(1)
            {
                p=i*m;
                q=p;
                while(q!=0)
                {
                    ara[q%10]=1;
                    q/=10;
                }
                l=0;
                for(j=0;j<=9;j++)
                {
                    if(ara[j]==0)
                        l=1;
                }
                if(l==0)
                {
                    cout<<"Case #"<<rel<<": "<<p<<endl;
                    break;
                }
                i++;
            }
        }
    }
    return 0;
}
