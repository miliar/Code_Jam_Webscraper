#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	long int t,smax,sum,ans;
	ifstream iff("A-large.in");
	ofstream off("answer.txt");
	iff>>t;
	for(long int it=0;it<t;it++)
	{
		iff>>smax;
		const long int a=smax+1;
		char str[a];
		iff>>str;
		long int arr[a],i;
		sum=0;ans=0;
		for(i=0;i<a;i++)
			arr[i]=(int)(str[i]-'0');
		for(i=0;i<a-1;i++)
		{
			sum+=arr[i];
			if(sum<i+1)
			{
				ans+=i+1-sum;
				sum+=i+1-sum;
			}
		}
		off<<"Case #"<<it+1<<": "<<ans<<'\n';
	}
}
