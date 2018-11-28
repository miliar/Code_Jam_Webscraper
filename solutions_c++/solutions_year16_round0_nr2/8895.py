#include<iostream>
using namespace std;
int main()
{
	long long j,t;
	cin>>t;
	for(long long j=1;j<=t;j++)
	{
		string s;
		cin>>s;
		long long i=0,count=0;
		long long l=s.size();
		for(i=0;i<l-1;i++)
		{
			while(s[i+1]==s[i] && i<l-1)
			i++;
			if(i!=l-1)
			count++;
		}

		if(s[l-1]=='-')
			count++;

		printf("Case #%lld: %lld\n",j,count);

	}
	return 0;
}