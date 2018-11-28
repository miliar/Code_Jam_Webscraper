#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int tc,n,m,a,ma[17],i,j,ans,coutn,k;
    cin>>tc;
    for(k=1;k<=tc;k++)
    {
        coutn=0;
        memset(ma,0,sizeof(ma));
        cin>>n;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>a;
                if(i==n-1)
                    ma[a]++;
            }
        }
        cin>>m;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>a;
                if(i==m-1)
                    ma[a]++;
            }
        }
        for(i=1;i<=16;i++)
        {
            if(ma[i]==2)
            {
                ans=i;
                coutn++;
            }

        }
        if(coutn==1)
        {
            cout<<"Case #"<<k<<": "<<ans<<endl;
        }
        else if(coutn==0)
        {
            cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
        }
        else
        {
            cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
        }

    }
    return 0;
}
