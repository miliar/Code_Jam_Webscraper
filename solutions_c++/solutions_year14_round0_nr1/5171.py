//siddharth prasad

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
 int t;
 cin>>t;
 for(int x=1;x<=t;x++)
 {
  int a[4][4],i,j,n,m,b[4][4],c=0;
  cin>>n;
  for(i=0;i<4;i++)
  {
  for(j=0;j<4;j++)
  {
   cin>>a[i][j];
  }
  }
  cin>>m;
  for(i=0;i<4;i++)
  {
  for(j=0;j<4;j++)
  {
   cin>>b[i][j];
  }
  }
  int ans;
   for(i=0;i<4;i++)
    for(j=0;j<4;j++)

       if(a[n-1][i]==b[m-1][j])
        {
            c++;
            ans=a[n-1][i];
        }

   if(c==1)
    cout<<"case #"<<x<<": "<<ans<<endl;
    else if(c==0)
        cout<<"case #"<<x<<": " <<"Volunteer cheated!"<<endl;
    else
        cout<<"case #"<<x<<": "<<"Bad magician!"<<endl;
  }
 return 0;
 system("PAUSE");
}
