#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <map>
using namespace std;


#define name "B2"
int main()
{
	
	freopen(name".in","r",stdin);
	freopen(name".out","w",stdout);
	int T;

	cin >> T;
	for(int t=1;t<=T;++t)
	{
		int n; cin >> n;
		int P[10001];
		for(int i=0;i<n;++i)
			cin >> P[i];

		int ans = 1000000000;
		for(int i=1;i<=1000;++i)
		{
			int temp = i;
			for(int j=0;j<n;++j)
			{
				temp += (P[j]+i-1)/i - 1;
			}
			ans = min(temp,ans);
		}

		cout << "Case #" << t << ": " << ans << endl; 
	}
	return 0;
}