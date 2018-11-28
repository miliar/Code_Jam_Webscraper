#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <string>
#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)
#define all(x) (x).begin(), (x).end()
#define se second
#define fi first
#define mp make_pair
#define pb push_back
#define op operator
typedef vector <int> vi;
typedef pair<int, int> pii;
typedef long long i64;

const int maxn = 105;

int last_pos[30];
int s[maxn][maxn];
int per[maxn];
int len[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	fore(test, 1, tests)
	{
		printf("Case #%d: ", test);
		int n;
		scanf("%d", &n);
		fore(j, 1, n)
		{
			string s1;
			cin >> s1;
			len[j] = s1.length();
			forn(p, len[j])
				s[j][p] = s1[p] - 'a';
		}
		fore(j, 1, n)
			per[j] = j;
		int answer = 0;
		do
		{
			forn(j, 26)
				last_pos[j] = -1;
			int it = 0;
			bool fail = false;
			fore(step, 1, n)
			{
				int number = per[step];
				forn(pos, len[number])
				{
					int letter = s[number][pos];
					if (last_pos[letter] != -1 && last_pos[letter] != it - 1)
					{
						fail = true;
						break;
					}
					last_pos[letter] = it;
					it++;
				}
				if (fail)
					break;
			}
			if (!fail)
				answer++;
		}
		while(next_permutation(per + 1, per + n + 1));
		printf("%d\n", answer);
	}

	return 0;
}