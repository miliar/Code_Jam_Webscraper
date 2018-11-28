#include<iostream>
#include<string.h>
#include<map>
#include<vector>
#include<math.h>
#include<algorithm>

using namespace std;

int main()
{
	long long first=1;
	long long kase=0;
	cin>>kase;
	while(first<=kase)
	{
		long long sum=0;
		long long r,t;
		cin>>r>>t;
		long long a = 2*r+1;
		long long b = 2*(r+2)+1;
		long long d = b-a;
		long long count =1;
		while(sum<=t)
		{
			sum =count*(2*a+(count-1)*d)/2;
			if(sum>t)
				count--;
			else
				count++;
		}

		cout<<"Case #"<<first<<": "<<count<<endl;
		first++;
	}
	return 0;
}