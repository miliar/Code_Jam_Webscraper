#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <bitset>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
#define REP(i, a, b) for(int i = int(a); i <= int(b); i++)
#define LOOP(i, v) for(int i = 0; i < v.size(); i++)
#define EPS 1e-9
#define INF 1e12
#define debug(x) cerr << "DEBUG : " << (#x) << " => " << (x) << endl

// Order 0 : R < P < S
int y[6][3];
char letter[3];

// 0 --> 02
// 1 --> 01
// 2 --> 12

pair<int, int> next(int c, int order)
{
	int a, b;
	if(c == 0)
	{
		a = 0;
		b = 2;
	}
	else if(c == 1)
	{
		a = 0;
		b = 1;
	}
	else
	{
		a = 1;
		b = 2;
	}
	if(y[order][a] < y[order][b]) return ii(a, b);
	else return ii(b, a);
}

bool better(vi x, vi z, int order)
{
	REP(i, 0, x.size()-1)
	{
		if(y[order][x[i]] < y[order][z[i]]) return true;
		if(y[order][x[i]] > y[order][z[i]]) return false;
	}
	return false;
}

vi realnext(vi x, int order)
{
	vi ans;
	REP(i, 0, x.size()-1)
	{
		ii g = next(x[i], order);
		ans.push_back(g.first);
		ans.push_back(g.second);
	}
	return ans;
}

int main()
{

letter[0] = 'R';
letter[1] = 'P';
letter[2] = 'S';

y[0][0] = 0;
y[0][1] = 1;
y[0][2] = 2;
y[1][0] = 0;
y[1][1] = 2;
y[1][2] = 1;
y[2][0] = 1;
y[2][1] = 0;
y[2][2] = 2;
y[3][0] = 1;
y[3][1] = 2;
y[3][2] = 0;
y[4][0] = 2;
y[4][1] = 0;
y[4][2] = 1;
y[5][0] = 2;
y[5][1] = 1;
y[5][2] = 0;

	int T;
	scanf("%d", &T);
	
	REP(t, 1, T)
	{
		printf("Case #%d: ", t);
		fprintf(stderr, "Case #%d.\n", t);
		
		int N, R, P, S;
		scanf("%d %d %d %d", &N, &R, &P, &S);
		
		int x[13][3];
		bool ok = false;
		
		REP(i, 0, 2)
		{
			x[0][0] = 0;
			x[0][1] = 0;
			x[0][2] = 0;
			x[0][i] = 1;
			REP(j, 1, N)
			{
				x[j][0] = x[j-1][0]+x[j-1][1];
				x[j][1] = x[j-1][1]+x[j-1][2];
				x[j][2] = x[j-1][0]+x[j-1][2];
			}
			if(x[N][0] == R && x[N][1] == P && x[N][2] == S)
			{
				vi answer[13][6];
				REP(j, 0, 5) answer[0][j].push_back(i);
				REP(k, 1, N)
				{
					REP(j, 0, 5)
					{
						answer[k][j] = realnext(answer[k-1][0], j);
						REP(l, 1, 5)
						{
							vi poss = realnext(answer[k-1][l], j);
							if(better(poss, answer[k][j], j))
							{
								answer[k][j] = poss;
							}
						}
					}
				}
				
				REP(j, 0, answer[N][2].size()-1)
				{
					printf("%c", letter[answer[N][2][j]]);
				}
				printf("\n");
				ok = true;
			}
		}
		if(!ok)
		{
			printf("IMPOSSIBLE\n");
		}
		
	}

  return 0;
}
