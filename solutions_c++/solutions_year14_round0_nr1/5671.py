#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
//Google Code Jam'14 Qual - 1st - Small
int main()
{
    int t,row1,row2,i,j,x;
    cin>>t;
    for(x=1;x<=t;x++)
    {
      cin>>row1;
      int g1[4][4],g2[4][4];
      for(i=0;i<4;i++)
      for(j=0;j<4;j++)
        cin>>g1[i][j];
      cin>>row2;
      for(i=0;i<4;i++)
      for(j=0;j<4;j++)
        cin>>g2[i][j];
      int fans=0,crr=0;
      for(i=0;i<4;i++)
      {
        for(j=0;j<4;j++)
        {
          if(g1[row1-1][i] == g2[row2-1][j])
          {
            crr++;
            if(crr==1)
            fans=g1[row1-1][i];
          }
        }
      }
      
      if(crr==0)
      cout<<"Case #"<<x<<": Volunteer cheated!\n";
      else if(crr==1)
      cout<<"Case #"<<x<<": "<<fans<<endl;
      else
      cout<<"Case #"<<x<<": Bad magician!\n";
    }
    return 0;
}
