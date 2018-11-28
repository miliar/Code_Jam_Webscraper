#include<iostream>
using namespace std;
int main()
{
  int t,j,i ;
  cin>>t;
  for(int x=1;x<=t;x++)
    {
      int r1,r2,a[4][4],b[4][4];
      cin>>r1;
      for(i=0;i<4;i++)
        for(j=0;j<4;j++)
          cin>>a[i][j];
      cin>>r2;
      int cnt=0,ans=0;
      for(i=0;i<4;i++)
        for(j=0;j<4;j++)
          {
            cin>>b[i][j];
            if(i+1==r2)
              {
                for(int k=0;k<4;k++)
                  if(b[i][j]==a[r1-1][k])
                    {cnt++;ans=b[i][j];}
              }
          }
	cout<<"Case #"<<x<<": ";
      if(cnt==0)
        cout<<"Volunteer cheated!\n";
      else if(cnt==1)
        cout<<ans<<endl;
      else if(cnt>1)
        cout<<"Bad magician!\n";
        }

}
