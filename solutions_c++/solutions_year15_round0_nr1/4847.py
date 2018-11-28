#include <iostream>
#include <string>

using namespace std;

int T, n;
string s;

int main(){
	// freopen("a.in", "r", stdin);
	// freopen("b.out", "w", stdout);
	cin>>T;
	for (int kase = 1; kase <= T; kase++)
	{
		cin>>n;

		cin>>s;
		int sum = 0, ans=0;
		for (int i = 0; i <= n; ++i)
		{
			if (i > sum)
			{
				ans += i-sum;
				sum += i-sum;
			}
			sum += s[i]-'0';
		}
		printf("Case #%d: ", kase);
		cout<<ans<<endl;
	}
	return 0;
}
