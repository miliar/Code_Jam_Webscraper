#include<iostream>
using namespace std;
int main()
{
    int t,ans1,ans2,i,j,tt;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
      cin>>ans1;
      int g1[4][4],g2[4][4];
      for(i=0;i<4;i++)
      {
        for(j=0;j<4;j++)
        {
          cin>>g1[i][j];
        }
      }
      cin>>ans2;
      for(i=0;i<4;i++)
      {
        for(j=0;j<4;j++)
        {
          cin>>g2[i][j];
        }
      }
      int ans=-1,ctr=0;
      for(i=0;i<4;i++)
      {
        for(j=0;j<4;j++)
        {
          if(g1[ans-1][i] == g2[ans2-1][j])
          {
            ctr++;
            if(ctr==1)
            ans=g1[ans1-1][i];
          }
        }
      }
      if(ctr==1)
      cout<<"Case #"<<tt<<": "<<ans<<endl;
      else if(ctr==0)
      cout<<"Case #"<<tt<<": Volunteer cheated!\n";
      else
      cout<<"Case #"<<tt<<": Bad magician!\n";
    }
    return 0;
}
