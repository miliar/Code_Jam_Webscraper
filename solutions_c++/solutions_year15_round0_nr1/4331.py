#include <iostream>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int t = 1; t <= T; ++t)
	{
		int s;
		char str[1003];
		cin>>s>>str;
		int ans = 0, sum = 0;
		for (int i = 0; i <=s; ++i)
		{
			if(str[i]-'0')
			{
				if(sum >= i)
					sum += str[i]-'0';
				else
				{
					ans+=(i-sum);
					sum+=ans+str[i]-'0';
				}
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}