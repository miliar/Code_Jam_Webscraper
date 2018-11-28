#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	int t, k;
	string s;
	cin>>t;
	for (int y = 0; y < t; y++)
	{
		cin>>s;
		cin>>k;
		int count = 0;
		for (int i = 0; i < s.size()-k+1; i++)
		{	
			//cout<<i<<" "<<s[i]<<"\n";
			if (s[i] == '-')
			{
				int temp = i;
				while (temp < i+k)
				{
					if (s[temp] == '+')
						s[temp] = '-';
					else
						s[temp] = '+';
					temp++;
				}
				count++;
			}
		}
		int flag = 0;
		for (int i = 0; i < s.size(); i++)
		{	
			if (s[i] == '-')
			{
				flag = 1;
				break;
			}
		}
		//cout<<s<<"\n";
		if (flag)
			cout<<"Case #"<<y+1<<": IMPOSSIBLE\n";
		else
			cout<<"Case #"<<y+1<<": "<<count<<"\n";
	}
}