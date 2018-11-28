#include<iostream>
#include<cstdio>
using namespace std;
int main()
{

    int a[4];
    int b[4];
    int t,n,j,i,x,cnt=0,z,m=1;
    cin>>t;
    while(t--)
    {   cnt=0;
        cin>>n;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
               cin>>x;
               if(n==i+1)
               {
                   a[j]=x;
               }
            }
        }
        cin>>n;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
               cin>>x;
               if(n==i+1)
               {
                   b[j]=x;
               }
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i]==b[j])
                {
                    cnt++;
                    z=a[i];
                }
            }
        }
        if(cnt==1)
        {
            cout<<"Case #"<<m++<<": "<<z<<endl;
        }
        else if(cnt==0)
        {
            cout<<"Case #"<<m++<<": Volunteer cheated!\n";
        }
        else if(cnt>1){
            cout<<"Case #"<<m++<<": Bad magician!\n";
        }
    }
}
