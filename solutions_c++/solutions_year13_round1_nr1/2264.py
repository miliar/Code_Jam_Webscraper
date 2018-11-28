#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main(void)
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-Large.out", "w", stdout);

	long long int T;
	cin>>T;
	long long int r, t, sum, count;
	count = 0;
	while(T--)
	{
		cin>>r>>t;
		count++;
		sum = 0;
		long long int j = 0;
		for(long long int i = r; sum <= t; i+=2, j++)
		{
			sum += (2*i + 1);
		}
		cout<<"Case #"<<count<<": "<<j-1<<endl;
	}
}
