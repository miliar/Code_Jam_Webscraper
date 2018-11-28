#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,temp=1;
	int nsp,as,npa,ans,max=0;
	char *arr;
	cin>>t;
	while(t--)
	{
		cin>>max;
		arr = new char[max+2];
		cin>>arr;
		nsp=npa=ans=0;
		for(int s=0;s<=max;s++)
		{
			as = arr[s] - '0';
			if(nsp<s)
			{
				npa = s-nsp;
				nsp = nsp + npa+as;
				ans = ans + npa;
				npa = 0;
			}
			else
			{
				nsp = nsp + as;
			}
		}
		cout<<"Case #"<<temp<<": "<<ans<<endl;
		temp++;
	}
return 0;
}
