#include<bits/stdc++.h>
using namespace std;
long long int getAnswer(long long int n)
{
	bool done[10];
	memset(done,0,sizeof(done));
	int count=0;
	long long int number=n;
	while(count!=10)
	{
		long long int temp=number;
		while(temp)
		{
			int digit = (int)(temp%10);
			if(done[digit]==0)
			{
				count++;
				done[digit]=1;
			}
			temp/=10;
		}
		if(count==10)
			break;
		number+=n;
	}
	return number;
}
int main()
{
	int t;
	cin>>t;
	for(int gh=1;gh<=t;gh++)
	{
		int n;
		cin>>n;
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",gh);
		}
		else
		{
			long long int answer = getAnswer(n);
			printf("Case #%d: %lld\n",gh,answer);
		}
	}
	return 0;
}

