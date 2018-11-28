#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <map>
using namespace std;


#define name "A2"
int main()
{
	
	freopen(name".in","r",stdin);
	freopen(name".out","w",stdout);
	int T;

	cin >> T;
	for(int t=1;t<=T;++t)
	{
		int n; string s;
		cin >> n >> s;
		int ans = 0, good = 0;
		for(int j=0;j<=n;++j)
		{
			if(good+ans<j)
				ans += j-(good + ans );
			good+=s[j]-'0';
		}
		cout << "Case #" << t << ": " << ans << endl; 
	}
	return 0;
}