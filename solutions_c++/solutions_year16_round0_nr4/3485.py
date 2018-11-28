#include<iostream>
using namespace std;
unsigned long long 	int t,k,c,s,kc,count=1;
unsigned long long f(unsigned long long a,unsigned long long b)
{
	if(b==1)
	return a;
	unsigned long long p=f(a,b/2);
	if(b%2==0)
	return p*p;
	return a*p*p;
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w+",stdout);
	cin>>t;
	while(count<=t)
	{
		cin>>k>>c>>s;
		cout<<"Case #"<<count<<": ";
		kc=f(k,c);
		while(s)
		{
			cout<<kc<<" ";
			s--;
			kc--;
		}
		cout<<endl;
		count++;
		
	}
	
}
