#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<queue>

#define INF 1000000000
#define endl '\n'
#define ll long long

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	for(int t=1 ; t<=T ; t++)
	{
		string s;
		cin >> s;
		
		
		int n = s.size();
		char hold = '+';
		int ans = 0;
		for(int i = n-1 ; i >= 0 ; i--)
		{
			if(s[i] != hold)
			{
				ans++;
				hold = s[i];
			}
		}
		
		cout << "Case #" << t << ": " << ans << endl;
	}
	
	return 0;
}

