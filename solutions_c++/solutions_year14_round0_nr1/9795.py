#include <iostream>
#include <set>
using namespace std;
int main ()
{
 
   long long int a[4][4],b[4],c[4],sum,t,r1,r2,i,j,k,val;
  cin>>t;
  for(i=0;i<t;i++)
  {
  	sum=0;
  cin>>r1;
  for(j=0;j<4;j++)
  {
  for (k=0; k<4;k++)
  {
  	cin>>a[j][k];
  	if(j==r1-1)
  	b[k]=a[j][k];
  }
  }
  cin>>r2;
  for(j=0;j<4;j++)
  {
  for (k=0; k<4;k++)
  {
  	cin>>a[j][k];
  	  	if(j==r2-1)
  	  	c[k]=a[j][k];
  }
  }
  	  	
  for(j=0;j<4;j++)
  {
  for (k=0; k<4;k++)
  {
   	if(b[j]==c[k])
  	{
  	sum++;
  	val=b[j];
  	}
  	
  }
  }
  	  
  if(sum==1)
  cout<<"Case #"<<i+1<<": "<<val<<endl;
else
   {
   	if(sum==0)
  cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
  else
  cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
  }
  }
  return 0;
}