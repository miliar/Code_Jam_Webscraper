#include <iostream>
#include <cmath>
using namespace std;
int palin(int a)
{
	int A,reva=0,r;
	A=a;
	while(a!=0)
	{
		r=a%10;
		a=a/10;
		reva=r+reva*10;
	}
	if(A==reva)
		return 1;
	else
		return 0;
}
int fairandsq(int a)
{
	int sqa;
	sqa=(int)sqrt(a);
	if((sqa*sqa)!=a)
		return 0;
	//cout<<a<<endl;
	//cout<<palin(a)<<" "<<palin((int)sqrt(a))<<endl;
	if(palin(a) && palin((int)sqrt(a)))
		return 1;
	else
		return 0;
}
int main()
{
	int t,i,j,a,b,k,T,count=0;
	cin>>t;
	T=t;

	while(t--)
	{
		count=0;
		cout<<"Case #"<<T-t<<": ";
		cin>>a>>b;
		for(;a<=b;a++)
		{
			if(fairandsq(a))
				count++;
		}
		cout<<count<<endl;
		
	}
	return 0;
}
 
 
