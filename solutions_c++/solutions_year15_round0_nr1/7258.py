#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("inl.in" , "r" , stdin);
	freopen("outl.out" , "w" , stdout);
	long long test;
	cin>>test;
	for (long long i = 1; i <= test ; ++i)
	{
		;
		long long n;
		cin>>n;
		string s;
		cin>>s;
		long long sum = 0;
		long long friends = 0;
		long long val = 0;
		for (long long j = 0; j <= n ; ++j)
		{
			val = s[j] - 48;
			if(sum >= j)
			{
				sum = sum + val;
			}
			if(sum < j)
			{
				friends = friends + (j - sum);
				sum = sum +  val + j - sum;
			}
		}
		cout<<"Case #"<<i<<": "<<friends<<endl;

	}
	return 0;
}