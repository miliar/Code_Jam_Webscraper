#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
        freopen( "input.txt", "r", stdin );
       	freopen( "output.txt", "w", stdout );

    int t;
    cin>>t;
    int c=0;
    while(t--)
    {
              int n1,n2,i,j;
              int a[4][4],b[4][4];
              cin>>n1;
              for(i=0;i<4;i++)
              for(j=0;j<4;j++)
              cin>>a[i][j];
              
              cin>>n2;
              for(i=0;i<4;i++)
              for(j=0;j<4;j++)
              cin>>b[i][j];
              
              int count=0,m;
              
              for(i=0;i<4;i++)
              {
              for(j=0;j<4;j++)
              {
              if(a[n1-1][i]==b[n2-1][j])
              {count++;m=i;}}
              }
              c++;
              //cout<<count<<n1<<n2;
              if(count==1)
              cout<<"Case #"<<c<<": "<<a[n1-1][m];
              else if(count>1)
              cout<<"Case #"<<c<<": "<<"Bad magician!";
              else if(count==0)
              cout<<"Case #"<<c<<": "<<"Volunteer cheated!";
             cout<<endl;
                       
    }
}
