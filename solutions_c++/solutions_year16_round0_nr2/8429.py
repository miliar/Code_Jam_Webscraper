#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string>
#include <set>

using namespace std;

typedef long long ll;
typedef double ld;
typedef pair<ll , pair<ll,ll>> piii;

const ll N = 2e6;
const ll M = 11;
const ll INF = 2e9;
const ll SQ = 320;
const ll MOD = 1e9+7;

#define inf cin
#define of cout
#define mp make_pair

set<int> st;

int main()
{
	ios_base::sync_with_stdio(false);
	ifstream inf("input.txt");
	ofstream of("output.txt");
	cin.tie();

	int t;
	cin >> t;
	for (int i = 1; i<=t; i++)
	{
		cout << "Case #" << i << ": ";
		string s;
		cin >> s;
		int l = s.size();
		int ans = 0;
		for (int j = 1; j<l; j++)
			if (s[j]!=s[j-1])
				ans++;
		if (s[l-1]=='+')
			cout << ans << '\n';
		else
			cout << ans+1 << '\n';
	}

	return 0;
}