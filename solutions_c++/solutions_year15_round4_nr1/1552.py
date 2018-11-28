#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <memory.h>
#include <ctime>
#include <bitset>
#include <vector>
#include <stack>
#include <string>
#include <queue>

using namespace std;

#define ABS(a) (((a) > 0)? (a): -(a))
#define MIN(a, b) (((a) < (b))? (a): (b))
#define MAX(a, b) (((a) < (b))? (b): (a))
#define MFOR(i, a, n) for (int i = (a); i < (n); i++)
#define FOR(i, a, n) for (int i = (a); i <= (n); i++)
#define DFOR(i, a, n) for (int i = (a); i >= (n); i--)
#define SORT(a, first_element, last_element) sort(&(a)[(first_element)], &(a)[(last_element) + 1])
#define SQR(a) (a) * (a)
#define PI 3.14159265358979323846264
#define MEMS(a, b) memset((a), (b), sizeof(a))
#define MP make_pair
#define PB push_back
#define endl '\n'
#define LL long long
#define UN unsigned
#define Or ||
#define And &&
/////////////////////////////////////////////

string f[150];
char bad[150][150];
char R[150], C[150];
char RR[150], CC[150];
int dx, dy;

void proc(char t)
{
	if (t == '^')
	{
		dx = -1;
		dy = 0;
		return;
	}
	if (t == 'v')
	{
		dx = 1;
		dy = 0;
		return;
	}
	if (t == '>')
	{
		dx = 0;
		dy = 1;
		return;
	}
	if (t == '<')
	{
		dx = 0;
		dy = -1;
		return;
	}
	return;
}

void solution()
{
	int T;
	cin >> T;
	f[0] = "X";
	FOR(i, 1, 120)
		f[0] = f[0] + "X";

	FOR(t, 1, T)
	{
		int r, c;
		cin >> r >> c;
		FOR(i, 1, r)
		{
			cin >> f[i];
			f[i] = "X" + f[i] + "X";
		}
		f[r + 1] = f[0];

		MEMS(bad, 0);
		MEMS(RR, 0);
		MEMS(CC, 0);
		FOR(i, 1, r)
		{
			FOR(j, 1, c)
			{
				if (f[i][j] != '.')
				{
					RR[i]++;
					CC[j]++;
					int x = i;
					int y = j;
					proc(f[x][y]);
					x += dx;
					y += dy;
					while (f[x][y] == '.')
					{
						x += dx;
						y += dy;
					}
					if (f[x][y] == 'X')
						bad[i][j] = 1;
				}
			}
		}

		bool q = true;
		int ans = 0;
		FOR(i, 1, r)
		{
			FOR(j, 1, c)
			{
				if (bad[i][j])
				{
					if (RR[i] > 1 Or CC[j] > 1)
						ans++;
					else
						q = false;
				}
			}
		}

		printf("Case #%d: ", t);
		if (q)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;

	}
}

/*-------------------*/

int main()
{
#ifdef Files
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
/*Test*/
//freopen("input.txt", "w", stdout);

long double OcZ2X = clock();
#else
//freopen("unionday.in", "r", stdin);
//freopen("unionday.out", "w", stdout);
#endif

solution();

#ifdef Time
long double P2HxQ = clock();
printf("\n*** Total time = %.3f sec ***\n", (P2HxQ - OcZ2X) / CLOCKS_PER_SEC);
#endif
}