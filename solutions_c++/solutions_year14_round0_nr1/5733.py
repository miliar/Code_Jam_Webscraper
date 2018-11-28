#include<iostream>
using namespace std;
int main(){ int a[4][4],x,y,flag=0,b[4][4]; int t,out=0; cin>>t;  while(t--) {  out++;  cin>>x;  x--;  for(int i=0;i<4;i++)     for(int j=0;j<4;j++)       cin>>a[i][j];    
  cin>>y;  y--;  for(int i=0;i<4;i++)  {   for(int j=0;j<4;j++)   {    cin>>b[i][j];   }  }  int temp=0;  flag=0;
  for(int i=0;i<4;i++)  {   for(int j=0;j<4;j++)   {    if(a[x][i]==b[y][j])    {flag++;temp=a[x][i];}   }  }
  
  if(flag==1)  cout<<"Case #"<<out<<": "<<temp<<"\n";  
  else if(flag==0)  cout<<"Case #"<<out<<": Volunteer cheated!\n";  
  else cout<<"Case #"<<out<<": Bad magician!\n"; }}
