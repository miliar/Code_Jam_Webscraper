#include<iostream>

int main()
{
using namespace std;
 int t,n,i,j,y,z=1;
 long long int m,x;
 cin>>t;
 while(t>0)
 {
 int flag=0,a[10]={0};
 cout<<"\n";
 cin>>n;
 if(n==0)
  cout<<"Case #"<<z++<<": "<<"INSOMNIA";
 else
 {
 for(i=1;i<200;i++)
 {
  if(i==10)
	a[0]++;
  x=i*n;
  m=x;
  while(x>0)
  {
	y=x%10;
	a[y]++;
	x=x/10;
  }
  flag=0;
  for(j=0;j<10;j++)
  {
	if(a[j]>0)
	 flag++;
  }
  if(flag==10)
  {
	cout<<"Case #"<<z++<<": "<<m;
	break;
  }
 }
 }
 t--;
 }
}
