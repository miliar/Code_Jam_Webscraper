#include <bits/stdc++.h>
using namespace std;

int smax, counts[1262];
string s;

void pain()	{
	cin >> smax >> s;
	memset(counts, 0, sizeof counts);
	for(int i=0; i<=smax; i++)	{
		counts[i] = (s[i] - '0');
	}
	int ans = 0, sum = counts[0];
	for(int i=1; i<=smax; i++)	{
		ans = max(ans, i - sum);
		sum += counts[i];
	}
	cout << ans << "\n";
}

int main()	{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string input = "input-qual-A.txt";
	string output = "output-qual-A.txt";
	freopen(input.c_str(), "r", stdin);
	freopen(output.c_str(), "w", stdout);
	int tt; cin >> tt;
	for(int iii=1; iii<=tt; iii++)	{
		cout << "Case #" << iii << ": ";
		pain();
	}
}
