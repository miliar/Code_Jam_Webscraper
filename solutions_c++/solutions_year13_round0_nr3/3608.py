#include<iostream>
#include<cmath>

int main()
{
using namespace std;
int j,i,n,l,u,k;
long long orig,rev,dig,a[500],b[500],count,count1;
cin>>n;

for(j=0;j<n;j++)
{
cin>>l>>u;

 count=0;
 count1=0;
 for(i=l;i<=u;i++)
 {
 orig = i;	 
 rev = 0;
 while(orig>0)
 {
      dig=orig%10;
      rev=rev*10+dig;
      orig=orig/10;
 }
 if(i==rev)
 {
	 a[count]=i;
	 count++;
 }
 }
 
 for(i=0;i<count;i++)
 {
  if(a[i]==1)
  count1++;
  else
  {
  for(k=2;k<=(a[i]/2)+1;k++)
 {
 if((double)k==sqrt(a[i]))
 {
 orig = k;	 
 rev = 0;
 while(orig>0)
 {
      dig=orig%10;
      rev=rev*10+dig;
      orig=orig/10;
 }
 if(k==rev)
 {
	count1++;
 }
 }
 }
}
}
cout<<"Case #"<<j+1<<": "<<count1<<"\n";

} 
 
return 0;
}
