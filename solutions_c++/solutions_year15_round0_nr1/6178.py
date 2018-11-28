#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t = 0, T;
	cin>>T;
	while(t++ < T)
	{
		int n, i, br = 0, ans = 0;
		cin>>n;
		string s;
		cin>>s;
		for(i = 0; i <= n; i++)
		{
			if(br < i) ans += (i - br), br = i;
			br += s[i]-'0';
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	return 0;
}
