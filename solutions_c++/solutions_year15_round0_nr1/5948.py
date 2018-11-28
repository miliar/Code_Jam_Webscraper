#include<bits/stdc++.h>

using namespace std;

#define LL long long int
#define ULL unsigned long long
#define sd(x) scanf("%d", &x)
#define MP make_pair
#define PB push_back
#define vi vector<int> 
#define pii pair<int,int> 
#define F first
#define S second
#define D double
#define LD long double


inline void solve()
{
	int s_max;
	sd(s_max);
	string str;
	cin >> str;
	vector<int> v;
	for(int i = 0; i < str.size(); i++)
	{
		int n = str[i] - '0';
		for(int j = 0; j < n; j++)
			v.push_back(i);
	}
	sort(v.begin(), v.end());
	int ans = 0;
	for(int i = 0; i < v.size(); i++)
		ans = max(ans, v[i] - i);
	cout << ans << endl;
}

int main()
{
	int t, i;
	sd(t);
	for(i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
    return 0;
}