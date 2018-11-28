#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,p=0;
	cin>>t;
	while (t--)
	{
		int num;
		string s;
		cin>>num>>s;
		int count = 0,ans = 0;
		for (int i = 0; i <= num; i++)
		{
			if (count <= i && s[i] != '0'){
				ans += (i - count);
				count += (i-count);
			}
				
			count += (s[i] - 48);		
		}
		cout<<"Case #"<<++p<<": "<<ans<<endl;
	}
	return 0;
}