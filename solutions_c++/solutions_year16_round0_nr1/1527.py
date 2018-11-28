#include <iostream>
#include <vector>
#define MAXN 100000
#define INF 1000000000
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		long long n;
		cin>>n;
		bool num[10] = {};
		int count = 0;
		if(n == 0)
		{
			cout<<"Case #"<<t<<": "<<"INSOMNIA"<<"\n";
			continue;
		}
		long long ans = n;
		long long temp = ans;
		while(temp)
		{
			int x = temp%10;
			if(!num[x])
			{
				num[x] = true;
				count++;
			}
			temp /= 10;
		}
		while(count != 10)
		{
			ans += n;
			temp = ans;
			while(temp)
			{
				int x = temp%10;
				if(!num[x])
				{
					num[x] = true;
					count++;
				}
				temp /= 10;
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	}
}
