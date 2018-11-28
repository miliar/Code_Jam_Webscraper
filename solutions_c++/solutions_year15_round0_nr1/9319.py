#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	int N;
	cin>>N;
	for(int cnt = 0; cnt<N;cnt++)
	{
		int m;
		cin>>m;
		string s;
		cin>>s;
		int sum = 0, ans = 0;
		for(int i = 0; i< s.size();i++)
		{
			if(s[i] > '0')
			{
				int add = max(0, i - sum);
				ans += add;
				sum += add;
			}
			sum += s[i] - '0';
		}
		cout<<"Case #"<<cnt+1<<": "<<ans<<endl;
	}
	return 0;
}
