#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for(i = (a) ; i<(b) ; i++)
#define RFOR(i, a, b) for(i = (a)-1 ; i>=(b); i--)
#define MEM(a,b) memset(a,b,sizeof(a))

#define SMALL 1
//#define SMALL 0

void Solve()
{
	int N;
	cin >> N;
	vector<int> party;
	party.resize(N);

	int i,j,k, total = 0;
	FOR(i, 0, N)
	{
		cin >> party[i];
		total += party[i];
	}
	
	double majority;
	bool IsTrue = true;

	while (total != 0)
	{
		FOR(i, 0, N)
		{
			if (party[i] != 0)
			{
				FOR(j, 0, N)
				{
					if (party[j] != 0)
					{
						IsTrue = true;
						party[i]--;
						party[j]--;
						FOR(k, 0, N)
						{
							majority = (double)(party[k]) / (total - 2);
							if (majority > 0.5)
							{
								party[i]++;
								party[j]++;
								IsTrue = false;
								break;
							}
						}

						if (IsTrue)
						{
							total -= 2;
							printf("%c%c ", 'A' + i, 'A' + j);
							break;
						}
						else
						{
							IsTrue = true;
							party[i]--;
							FOR(k, 0, N)
							{
								majority = (double)(party[k]) / (total - 1);
								if (majority > 0.5)
								{
									party[i]++;
									IsTrue = false;
									break;
								}
							}
							if (IsTrue)
							{
								total--;
								printf("%c ", 'A' + i);
								break;
							}
						}
					}
				}
			}
		}
	}
	cout << endl;
}

int main()
{
	if (SMALL)
	{
		freopen("A-small-attempt0.in", "r", stdin);
		freopen("A-small-attempt0.out", "w", stdout);
	}
	else
	{
		freopen("A-large.in", "r", stdin);
		freopen("A-large.out", "w", stdout);
	}

	int t, T;
	cin >> T;
	FOR(t, 0, T)
	{
		cout << "Case #" << t + 1 << ": ";
		Solve();
	}

	return 0;
}