#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<string>
#include<cstdlib>
#include<cmath>
#include<set>
#include<cstring>
using namespace std;
main()
{
  long long int t;scanf("%lld",&t);
  for(int k=1;k<=t;k++)
  {
      long long int a,b;
      scanf("%lld",&a);
      a=a-1;
      int m1[4][4],m2[4][4];
      for(int i=0;i<4;i++)
      {
      	for(int j=0;j<4;j++)
      	{
            cin>>m1[i][j];
      	}
      }
      scanf("%lld",&b);
      b=b-1;
      for(int i=0;i<4;i++)
      {
        for(int j=0;j<4;j++)
        {
           cin>>m2[i][j];
        }
      }
      int c=0,x;
      for(int i=0;i<4;i++)
      {
      	for(int j=0;j<4;j++)
      	{
      		if(m1[a][i]==m2[b][j])
      		{
      			x=m1[a][i];c++;
      		}
      	}
      }
      // cout<<c<<endl;
      if(c==0)
      {
         cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
      }
      else if(c>1)
      {
         cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
      }
      else
      {
         cout<<"Case #"<<k<<": "<<x<<endl;
      }
  }
}