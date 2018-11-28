#include <bits/stdc++.h>

using namespace std;

int n, t, k, ans;
string s;

int main()
{
	ifstream in;	in.open("tt.txt");	ofstream out;	out.open("ans.out");
	in >> t;
	for(int i = 0; i < t; i++)
	{
		in >> s >> k; out << "Case #" << i + 1 << ": " ; 
		n = s.length(); ans = 0;
		for(int j = n - 1; j >= k - 1; j--)
		{
			if (s[j] == '+') continue;
			ans++;
			for(int y = j - k + 1; y <= j; y++)
				s[y] = (s[y] == '+' ? '-' : '+');
		}
		bool wa = false;
		for(int j = 0; j < k - 1; j++)
			if (s[j] == '-')
				wa = true;
		if (wa)	out << "IMPOSSIBLE" << endl;
		else	out << ans << endl;
	}
	return 0;
}
