#include<iostream>
#include<cstring>
using namespace std;
int u[64];
int main()
{
    int t,n,i,j,ans=0,w,l=0,k=0;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<k<<": ";
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        for(j=1;j;j++)
        {
            w=n*j;
            //cout<<w<<": ";
            while(w)
            {
                u[w%10]=1;
                w/=10;
            }
            for(i=0;i<10;i++)
            {
                //cout<<u[i]<<" ";
                if(u[i]==0)
                {
                    l=1;
                }
            }
            //cout<<endl;
            if(l==0)
            {
                cout<<"Case #"<<k<<": ";
                cout<<n*j<<endl;
                break;
            }
            l=0;
        }
        memset(u,0,64);
    }
	return 0;
}
