#include<iostream>
#include<algorithm>
using namespace std;
main()
{
 int t;
 cin>>t;
 for(int i=1;i<=t;i++)
 {
  int a,n,x[105],cnt=0,flag=0,max=2147483647;
  cin>>a>>n;
  for(int j=0;j<n;j++)
   cin>>x[j];
  sort(x,x+n);
 // cout<<a<<endl; 
//  for(int j=0;j<n;j++) cout<<x[j]<<" ";
//  cout<<"\n";
  for(int j=0;j<n;j++)
  {
   if(x[j]<a) a+=x[j];
   else
   {
    if(a==1) { cnt=n-j; break; }
    int m=0;
    if(flag==0) max=n-j;
    flag=1;
    while(a<=x[j]) { m++; a+=(a-1); }
    if(m<n-j) { cnt+=m;   a+=x[j]; } else { cnt+=n-j; break; }
   }
  }
  if(cnt>=max) cnt=max;
  cout<<"Case #"<<i<<": "<<cnt<<endl;
 
 }
 return 0;
}
