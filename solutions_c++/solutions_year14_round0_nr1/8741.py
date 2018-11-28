#include <iostream>
#include<cstdlib>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in", "r+", stdin);
	freopen("outputfile10.txt", "w+", stdout);
    int i,j,c=0,t,y,x,a[4][4],b[4][4],z=-1,k;

    cin>>t;
    for(k=1;k<=t;k++)
    {
      cin>>x;
      x--;
      for(i=0;i<4;i++)
      {
       for(j=0;j<4;j++)
       {
         cin>>a[i][j];
       }
      }
      cin>>y;
      for(i=0;i<4;i++)
      {
       for(j=0;j<4;j++)
       {
         cin>>b[i][j];
       }
      }
      y--;
      for(i=0;i<4;i++)
      {
        for(j=0;j<4;j++)
        {
          if(a[x][i]==b[y][j])
          {
              c++;
              z=a[x][i];
          }
        }
      }
      if(c==1)
        cout<<"Case #"<<k<<": "<<z<<'\n';
      else if(c>1)
        cout<<"Case #"<<k<<": "<<"Bad magician!"<<'\n';
      else
        cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<'\n';
      c=0;









    }


    return 0;
}
