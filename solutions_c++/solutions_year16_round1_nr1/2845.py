#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <vector>
#include <cstring>
#include <set>

#define forn(i,n) for(int i = 0; i < (n); i++)
#define forsn(i,s,n) for(int i = (s); i < (n); i++)
#define all(v) ((v).begin, (v).end)
#define pb push_back
#define x first
#define y second
#define mp make_pair

using namespace std;

typedef pair<int,int> par;
typedef long long int tint;

int main()
{
	string s;

	freopen("test.txt","r",stdin);
	freopen("testout.txt","w",stdout);

	int t;

	cin >> t;

	forsn(caso,1,t+1)
	{
		cin >> s;
		int n = s.size();

		string ans = ""; ans += s[0];

		forsn(i,1,n)
		{
			if(s[i] >= ans[0]) ans = s[i] + ans;
			else ans += s[i];
		}
		cout << "Case #" << caso << ": " << ans << endl;
	}

	return 0;
}