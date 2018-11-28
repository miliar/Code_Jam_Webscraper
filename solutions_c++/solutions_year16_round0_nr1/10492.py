#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    cin>>test;
    for(int t=1;t<=test;t++)
    {
        ll p,n;
        cin>>p;
        n=p;
        int hash[10];
        memset(hash,0,sizeof(hash));
        ll ite=1000000000;
        int flag;
        while(ite--)
        {

                ll temp=n;
                while(temp>0)
                {
                    hash[temp%10]++;
                    temp=temp/10;
                }
                /*for(int i=0;i<10;i++)
                    cout<<hash[i]<<" ";
                    cout<<"\n";*/
                flag=1;

                for(int i=0;i<10;i++)
                {
                    if(hash[i]==0)
                    {
                        flag=0;
                        break;
                    }
                }
                if(flag==1)
                   {
                        cout<<"Case #"<<t<<": "<<n<<"\n";
                        break;
                   }
                   n=n+p;
            }

           if(flag==0)
            {
                cout<<"Case #"<<t<<": INSOMNIA\n";
            }
    }
}
