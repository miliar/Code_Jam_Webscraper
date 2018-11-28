//Karol Kaszuba

#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef double D;
typedef long double LD;
typedef vector<PII> VII;
typedef unordered_set<int> USI;
typedef unordered_set<LL> USLL;

#define FOR(i,x,y) for(auto i=(x);i<=(y);++i)
#define REP(i,x) FOR(i,0,(x)-1)
#define FORD(i,x,y) for(auto i=(x);i>=(y);--i)
#define VAR(i,c) __typeof(c) i=(c)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define SIZE(c) (int)((c).size())
#define ALL(c) (c).begin(),(c).end()
#define PB push_back
#define IN insert
#define ER erase
#define MP make_pair
#define ST first
#define ND second
#define IOSYNC ios_base::sync_with_stdio(0)
#define FREOPEN(f) freopen(f, "r", stdin),freopen(f, "w", stdout)

string s[102];
int r, c;
int licz(int a, int b)
{
	int res = 0;
	REP(i, r)
		res += s[i][b] == '.';
	REP(j, c)
		res += s[a][j] == '.';
	res = r + c - 1 - res;
	//	cout << "licz " << a << " " << b << " " << res << "\n";
	return res;
}

void jebaj()
{
	cin >> r >> c;
	REP(i, r)
	{
		cin >> s[i];
	}
	
	set<PII> to_rotate;
	
	REP(i, r)
	{
		string t = s[i];
		
			int j = 0;
			while(j < SIZE(t) && t[j] == '.') j++;
			if(j < SIZE(t) && t[j] == '<')
			{
				if(licz(i, j) == 1)
				{
					cout << "IMPOSSIBLE\n";
					return;
				}
				to_rotate.IN(MP(i, j));
			}
			
			
			j = SIZE(t) - 1;
			while(j >= 0 && t[j] == '.') j--;
			if(j >= 0 && t[j] == '>')
			{
				if(licz(i, j) == 1)
				{
					cout << "IMPOSSIBLE\n";
					return;
				}
				to_rotate.IN(MP(i, j));
			}
	}
	
	REP(i, c)
	{
		string t = "";
		REP(ii, r) t.PB(s[ii][i]);
		
			int j = 0;
			while(j < SIZE(t) && t[j] == '.') j++;
			if(j < SIZE(t) && t[j] == '^')
			{
				if(licz(j, i) == 1)
				{
					cout << "IMPOSSIBLE\n";
					return;
				}
				to_rotate.IN(MP(j, i));
			}
			
			
			j = SIZE(t) - 1;
			while(j >= 0 && t[j] == '.') j--;
			if(j >= 0 && t[j] == 'v')
			{
				if(licz(j, i) == 1)
				{
					cout << "IMPOSSIBLE\n";
					return;
				}
				to_rotate.IN(MP(j, i));
			}
	}
	
	cout << SIZE(to_rotate) << "\n";
}

int main()
{
	IOSYNC;
	int t = 1;
	cin >> t;
	
	REP(i, t)
	{
		cout << "Case #" << i + 1 << ": ";
		jebaj();
	}
}
