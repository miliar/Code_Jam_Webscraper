#include<iostream>
using namespace std;
int comp(void *a,void *b)
{
 return *(int *)b - *(int *)a;
}
main()
{
 int t;
 cin>>t;
 for(int u=1;u<=t;u++)
 {
  int n,m;
  cin>>n>>m;
  int a[105][105]={0};
  int *minrow = new int[n];
  int *maxrow = new int[n];
  int *mincol = new int[m];
  int *maxcol = new int[m];
  for(int i=0;i<n;i++)
   for(int j=0;j<m;j++)
    cin>>a[i][j];
  for(int i=0;i<n;i++)
  {
   int min=105,max=-1;
   for(int j=0;j<m;j++)
   {
    if(a[i][j]<min) min =a[i][j];
    if(a[i][j]>max) max =a[i][j];
   }
   minrow[i]=min;
   maxrow[i]=max;
  }
  for(int i=0;i<m;i++)
  {
   int min=105,max=-1;
   for(int j=0;j<n;j++)
   {
    if(a[j][i]<min) min = a[j][i];
    if(a[j][i]>max) max = a[j][i];
   }
   mincol[i]=min;
   maxcol[i]=max;
  }
 // for(int i=0;i<n;i++)
 // cout<<minrow[i]<<" "<<maxrow[i]<<endl;
  
 // for(int i=0;i<m;i++)
 // cout<<mincol[i]<<" "<<maxcol[i]<<endl;
  int flag;  
  for(int i=0;i<n;i++)
  {
   for(int j=0;j<m;j++)
   {
    flag=0;
    if(maxrow[i]==a[i][j]) continue;
    else if(maxcol[j]==a[i][j]) continue;
    else { flag=1; break; }
   }
  if(flag==1) break;
  }
  if(flag==1)
  cout<<"Case #"<<u<<": "<<"NO"<<endl;
  else
  cout<<"Case #"<<u<<": "<<"YES"<<endl;
 }
 return 0;
}
