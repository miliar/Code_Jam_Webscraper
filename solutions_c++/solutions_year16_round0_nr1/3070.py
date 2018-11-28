#include<bits/stdc++.h>
using namespace std;
int main()
{
        freopen("A-large (3).in","r",stdin);
        freopen("opa.txt","w",stdout);
    int t,z;
    cin>>t;
    for(z=1;z<=t;z++)
    {
        int i=2,j=0;
        long long int n;
        cin>>n;
       //n=999900+z-1;
        bool vis[10]={0};
        int temp=n;
        cout<<"Case #"<<z<<": ";
        if(temp==0)
            cout<<"INSOMNIA\n";
        else
        {


        while(n)
        {

            while(temp>0)
            {
                vis[temp%10]=1;
                temp/=10;
            }
            for(j=0;j<10;j++)
            {
                if(vis[j]==0)
                    break;
            }
            if(j==10)
            {
                break;
            }
            else
            {
                temp=n*i;
                i++;
            }
        }
        cout<<n*(i-1)<<"\n";
        }
    }
    return 0;
}
