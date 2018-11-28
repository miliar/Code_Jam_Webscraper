#include<iostream>
using namespace std;
int main()
{
    int t,n,m,a[4][4],b[4][4],i,j,x;
    cin>>t;
    for(x=1;x<=t;x++)
    {
        cin>>n;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>a[i][j];
        cin>>m;
         for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>b[i][j];
         int c=0,ans;
         for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            if(a[n-1][i]==b[m-1][j])
              {
                  c++;
                  ans=a[n-1][i];
              }
         if(c==0)
           cout<<"Case #"<<x<<": Volunteer cheated!"<<endl;
         else if(c==1)
            cout<<"Case #"<<x<<": "<<ans<<endl;
            else
             cout<<"Case #"<<x<<": Bad magician!"<<endl;
    }
    return 0;
}
