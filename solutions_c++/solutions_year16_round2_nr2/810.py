#include <bits/stdc++.h>

using namespace std;

string digs[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string repr = "ZWXUSGOTFN";
int nms[] = {0, 2, 6, 4, 7, 8, 1, 3, 5, 9};

signed main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		string a, b;
		cin >> a >> b;
		int minra = 10000;
		pair<string, string> ans;
		for(int A = 0; A < 1000; A++)
			for(int B = 0; B < 1000; B++)
			{
				auto aa = to_string(A);
				if(aa.size() > a.size())
					continue;
				while(aa.size() < a.size())
					aa.insert(aa.begin(), '0');
				auto bb = to_string(B);
				if(bb.size() > b.size())
					continue;
				while(bb.size() < b.size())
					bb.insert(bb.begin(), '0');
				if(abs(A - B) <= minra)
				{
					bool ok = 1;
					for(int i = 0; i < a.size(); i++)
						ok &= (a[i] == aa[i]) || (a[i] == '?');
					for(int i = 0; i < b.size(); i++)
						ok &= (b[i] == bb[i]) || (b[i] == '?');
					if(!ok)
						continue;
					if(abs(A - B) < minra)
						ans = {aa, bb};
					else
						ans = min(ans, {aa, bb});
					minra = abs(A - B);
				}
			}
		cout << ans.first << ' ' << ans.second;
		cout << "\n";
	}
	return 0;
}
