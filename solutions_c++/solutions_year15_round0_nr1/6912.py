#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int t;
	cin>>t;

	for(int tt=1;tt<=t;tt++)
	{
		int smax;
		cin>>smax;

		string s;
		cin>>s;

		int sum = 0, res = 0;

		for(int i=0;i<=smax;i++)
		{
			if(sum < i and s[i] != '0')
				res += (i - sum), sum = i;
			sum += (s[i] - '0');
		}
		
		cout<<"Case #"<<tt<<": "<<res<<"\n";
	}

	return 0;
}
