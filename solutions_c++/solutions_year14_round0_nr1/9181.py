#include <iostream>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for (int i=0;i<t;i++)
  {
    int a[5][5],b[5][5];
    int x,y;
    cin>>x;
    for (int j=1;j<=4;j++)
    for (int k=1;k<=4;k++)
    cin>>a[j][k];
    cin>>y;
    for (int j=1;j<=4;j++)
    for (int k=1;k<=4;k++)
    cin>>b[j][k];
    int z=0,q=0;
    for (int j=1;j<=4;j++)
    {
      int r=b[y][j];
      for (int k=1;k<=4;k++)
      if (r==a[x][k])
      z++,q=r;
    }
    cout<<"Case #"<<i+1<<": ";
    if (z==1)
    cout<<q;
    else if (z==0)
    cout<<"Volunteer cheated!";
    else cout<<"Bad magician!";
    cout<<endl;
    
  }
  return 0;
}
