#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int n,m,a[128][128],r[128],c[128];

void read ()
{
  int i,j,ma;
  cin>>n>>m;
  for(i=0;i<n;i++)
  for(j=0;j<m;j++)
  cin>>a[i][j];
  for(i=0;i<n;i++)
  {
    ma=0;
    for(j=0;j<m;j++)
    if(a[i][j]>ma)ma=a[i][j];
    r[i]=ma;
  }
  for(i=0;i<m;i++)
  {
    ma=0;
    for(j=0;j<n;j++)
    if(a[j][i]>ma)ma=a[j][i];
    c[i]=ma;
  }
  /*for(i=0;i<n;i++)
  cout<<r[i]<<" ";
  cout<<endl;
  for(i=0;i<m;i++)
  cout<<c[i]<<" ";
  cout<<endl;*/
  return ;
}

string solve ()
{
  int i,j,k,p;
  for(i=0;i<n;i++)
  for(j=0;j<m;j++)
  if(a[i][j]<r[i]&&a[i][j]<c[j])return "NO";
  return "YES";
}

int main ()
{
  int t,t1;
  cin>>t;
  for(t1=0;t1<t;t1++)
  {
    read ();
    cout<<"Case #"<<t1+1<<": "<<solve ()<<endl;
  }
  return 0;
}
