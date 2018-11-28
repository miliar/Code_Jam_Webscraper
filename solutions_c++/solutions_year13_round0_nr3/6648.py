#include<iostream>
#include<cmath>
using namespace std;
main()
{
 long long pal[11000]={0},k=0;
 for(int i=1;i<=10000000;i++)
 {
  int m=i,num=0;
  while(m>0)
  {
   int x = m%10;
   m=m/10;
   num=num*10+x;
  }
  if(num==i) 
  {
   long long m=i*i,num=0;
   while(m>0)
   {
    int x = m%10;
    m = m/10;
    num = num*10+x;
   }
   if(num==i*i)
     pal[k++]=i*i;
  }
 }
// for(int i=0;i<k;i++)
// cout<<sqrt(pal[i])<<" "<<pal[i]<<endl; 
 int t;
 cin>>t;
 for(int i=1;i<=t;i++)
 {
  long long x,y,count=0;
  cin>>x>>y;
  for(int j=0;j<k;j++)
  if((pal[j]>=x)&&(pal[j]<=y)) count++;
  cout<<"Case #"<<i<<": "<<count<<endl;
 }
 return 0;
}
