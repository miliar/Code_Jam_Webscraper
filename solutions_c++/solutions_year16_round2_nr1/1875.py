#include <bits/stdc++.h>

#define FOR(i, n) for(int i=0; i < n; i++)
#define FOR1(i, n) for(int i=1; i <= n; i++)

using namespace std;

constexpr int INF = 0x7fffffff;

typedef long long ll;            // –9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (19 digits)
typedef unsigned long long llu;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

typedef vector<vi> graph;
typedef vector<vii> weighted_graph;

void print(const char* msg, ...);

map<char, int> m;

int main()
{
	int T;
	scanf("%d", &T);
	getchar(); // skip \n

	for(int tc=1; tc <= T; tc++)
	{
		string current;
		vector<int> solution;

		printf("Case #%d: ", tc);
		getline(cin, current);

		for(auto &c : current)
		{
			if (m.find(c) == m.end())
				m[c] = 1;
			else
				m[c] += 1;
		}

		if (m.find('Z') != m.end())
		{
			while(m['Z'] > 0)
			{
				solution.push_back(0);
				string t = "ZERO";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		if (m.find('X') != m.end())
		{
			while(m['X'] > 0)
			{
				solution.push_back(6);
				string t = "SIX";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		if (m.find('W') != m.end())
		{
			while(m['W'] > 0)
			{
				solution.push_back(2);
				string t = "TWO";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		if (m.find('G') != m.end())
		{
			while(m['G'] > 0)
			{
				solution.push_back(8);
				string t = "EIGHT";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		if (m.find('S') != m.end())
		{
			while(m['S'] > 0)
			{
				solution.push_back(7);
				string t = "SEVEN";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		if (m.find('H') != m.end())
		{
			while(m['H'] > 0)
			{
				solution.push_back(3);
				string t = "THREE";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		if (m.find('R') != m.end())
		{
			while(m['R'] > 0)
			{
				solution.push_back(4);
				string t = "FOUR";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		if (m.find('F') != m.end())
		{
			while(m['F'] > 0)
			{
				solution.push_back(5);
				string t = "FIVE";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		if (m.find('O') != m.end())
		{
			while(m['O'] > 0)
			{
				solution.push_back(1);
				string t = "ONE";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		if (m.find('I') != m.end())
		{
			while(m['I'] > 0)
			{
				solution.push_back(9);
				string t = "NINE";
				for(auto &c : t)
				{
					m[c] -= 1;
				}
			}
		}

		sort(solution.begin(), solution.end());
		for(auto &n : solution)
			printf("%d", n);
		printf("\n");
	}

	return EXIT_SUCCESS;
}

void print(const char* msg, ...)
{
	#ifdef ONLINE_JUDGE
		va_list argptr;
		va_start(argptr, msg);
		vfprintf(stderr, msg, argptr);
		va_end(argptr);
	#endif
}