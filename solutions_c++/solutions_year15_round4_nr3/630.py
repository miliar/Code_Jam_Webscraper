#include <iostream>
#include <stdio.h>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <bitset>
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define NAME ""

using namespace std;
	
typedef long long ll;
typedef long double ld;

const ld PI = acos(-1.0);
const int MAXN = 4001;
ld rt[MAXN], tm[MAXN];
ld v, x, sm;
int n;
string str[MAXN];
int sc = 0;
vector <int> a[MAXN];
vector <string> b[MAXN];
int tp[MAXN];
string s;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tst;
	cin >> tst;
	for (int tt = 0; tt < tst; tt++)
	{
		cout << "Case #" << tt + 1 << ": ";
		int n;
		cin >> n;
		getline(cin, s);
		sc = 0;
		for (int i = 0; i < n; i++)
		{
			a[i].clear();
			b[i].clear();
			getline(cin, s);
			s += ' ';
			stringstream ss;
			ss.clear();
			ss << s;
			string wr;
			while (true)
			{
				wr = "";
				ss >> wr;
				if (wr == "") break;
				str[sc++] = wr;
				b[i].push_back(wr);
			}
		}
		sort(str, str + sc);
		sc = unique(str, str + sc) - str;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < b[i].size(); j++) a[i].push_back(lower_bound(str, str + sc, b[i][j]) - str);
		}
		int ans = sc;
		for (int nmsk = 0; nmsk < (1 << (n - 2)); nmsk++)
		{
			int msk = nmsk;
			msk *= 4;
			msk += 2;
			for (int i = 0; i < sc; i++) tp[i] = 0;
			for (int i = 0; i < n; i++)
			{
				int vl = 1;
				if (msk & (1 << i)) vl = 2; 
				for (int j = 0; j < a[i].size(); j++)
				{
					tp[a[i][j]] |= vl;
				}
			}
			int cur = 0;
			for (int i = 0; i < sc; i++) 
				if (tp[i] == 3) cur++;
			ans = min(ans, cur);
		}
		cout << ans << endl;
	}
	return 0;
}