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

map<int,int> cod;

int main()
{
	freopen("test.txt","r",stdin);
	freopen("testout.txt","w",stdout);

	string s;
	int t;
	cin >> t;

	forsn(caso,1,t+1)
	{
		cin >> s;
		int cant[300];
		forn(i,300) cant[i] = 0;
		vector<int> ans;
		int n = s.size();

		forn(i,n)
		{
			cant[(int)(s[i])]++;
		}
		//'Z'
		forn(i, cant[(int)('Z')])
		{
			cant[(int)('E')]--;
			cant[(int)('R')]--;
			cant[(int)('O')]--;
			ans.pb(0);
		}
		forn(i, cant[(int)('W')])
		{
			cant[(int)('T')]--;
			cant[(int)('O')]--;
			ans.pb(2);
		}
		forn(i,cant[(int)('U')])
		{
			cant[(int)('F')]--;
			cant[(int)('O')]--;
			cant[(int)('R')]--;
			ans.pb(4);
		}
		forn(i,cant[(int)('X')])
		{
			cant[(int)('S')]--;
			cant[(int)('I')]--;
			ans.pb(6);
		}
		forn(i,cant[(int)('G')])
		{
			cant[(int)('E')]--;
			cant[(int)('I')]--;
			cant[(int)('H')]--;
			cant[(int)('T')]--;
			ans.pb(8);
		}
		forn(i,cant[(int)('F')])
		{
			cant[(int)('I')]--;
			cant[(int)('V')]--;
			cant[(int)('E')]--;
			ans.pb(5);
		}
		forn(i,cant[(int)('S')])
		{
			cant[(int)('E')] -= 2;
			cant[(int)('V')]--;
			cant[(int)('N')]--;
			ans.pb(7);
		}
		forn(i,cant[(int)('T')])
		{
			cant[(int)('H')]--;
			cant[(int)('R')]--;
			cant[(int)('E')] -= 2;
			ans.pb(3);
		}
		forn(i,cant[(int)('I')])
		{
			cant[(int)('N')] -= 2;
			cant[(int)('E')]--;
			ans.pb(9);
		}
		forn(i,cant[(int)('O')])
		{
			ans.pb(1);
		}

		sort(ans.begin(), ans.end());
		int m = ans.size();

		cout << "Case #" << caso << ": ";
		forn(i,m) cout << ans[i];
		cout << endl;
	}

	return 0;
}