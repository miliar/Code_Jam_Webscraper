#include <iostream>
using namespace std;

int main() {
int n,d,i,t,standing,tobring,k;
cin>>t;
int l=1;
while(t--)
{
cin>>n>>d;
k= n+1;
int a[k];
for(i=0;i<k;i++)
{
	a[k-1-i]=d%10;
	d/=10;
	
}
standing =0;
tobring=0;
for(i=0;i<=k-1;i++)
{   if(i==0)
	{standing+=a[i];
	
	}
else{
	if(standing<i)
{	tobring+=1;
	standing+=1;
	standing+=a[i];
	}
	else
	standing+=a[i];
}}

cout<<"Case #"<<l<<": "<<tobring<<endl;
/*for(i=0;i<k;i++)
{
	cout<<a[i];
}*/
l++;}
}
