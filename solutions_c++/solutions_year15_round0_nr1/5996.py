typedef long long ll;
#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
using namespace std;
int main()
{
	ll t,i,n,c,w=1;
	string a;
	ll sum;
	scanf("%lld",&t);
	while(t--)
	{
		c=0;
		cin>>n;	   
sum=0;
	cin>>a;
	for(i=0;i<=n;i++)
	{
	
			if(i>sum)
			{
			c+=i-sum;
			sum=i;
			}
			sum+=a.at(i)-'0';
	
			}
			
			cout<<"Case #"<<w++<<": "<<c<<endl;			
		}
}