/*Since sharing solution is allowed,
 I am sharing this solution
 with 
 Name: Subodh Yadav
 Nickname: */
#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin>>T;
	for(int x=1;x<=T;x++)
	{
		int n;
		cin>>n;
		string str;
		cin>>str;
		long long int count = str[0] - '0';
		long long int ans = 0;
		for(int i=1;i<n+1;i++)
		{
			int digit = str[i] - '0';
			if(i > count && digit > 0)
			{
				ans += i-count;
				count += i-count;
				count += digit;
			}
			else
			{
				count += digit;
			}
		}
		cout<<"Case #"<<x<<": "<<ans<<"\n";
	}
	return 0;
}