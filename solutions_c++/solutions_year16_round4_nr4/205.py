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

int main()
{
	int T;
	scanf("%d", &T);
	
	REP(t, 1, T)
	{
		printf("Case #%d: ", t);
		fprintf(stderr, "Case #%d.\n", t);
		
		int N;
		scanf("%d\n", &N);
		bool can[4][4];
		bool newcan[4][4];
		char c;
		REP(i, 0, N-1)
		{
			REP(j, 0, N-1)
			{
				scanf("%c", &c);
				if(c == '0') can[i][j] = false;
				else can[i][j] = true;
			}
			scanf("\n");
		}
		
		int bestcost = 1000;
		
		REP(z, 0, (1 << N*N))
		{
			int cost = 0;
			REP(i, 0, N*N-1)
			{
				if(z & (1 << i)) cost++;
			}
			if(cost < bestcost)
			{
				REP(i, 0, N-1)
				{
					REP(j, 0, N-1)
					{
						int g = N*i+j;
						if(can[i][j] || (z & (1 << g))) newcan[i][j] = true;
						else newcan[i][j] = false;
					}
				}
				
				
				bool ok = true;
				
				int perm[4];
				REP(i, 0, N-1) perm[i] = i;
				do
				{
					int otherperm[4];
					REP(i, 0, N-1) otherperm[i] = i;
					do
					{
						bool busy[4];
						REP(i, 0, N-1) busy[i] = false;
						REP(i, 0, N-1)
						{
							int qui = perm[i];
							bool found = false;
							REP(j, 0, N-1)
							{
								int machine = otherperm[j];
								if(newcan[qui][machine] && !busy[machine])
								{
									busy[machine] = true;
									found = true;
									break;
								}
							}
							if(!found)
							{
								ok = false;
								break;
							}
						}
					} while(next_permutation(otherperm, otherperm+N) && ok);
				} while(next_permutation(perm, perm+N) && ok);
				
				if(ok)
				{
					bestcost = cost;
				}
			}
		}
		
		printf("%d\n", bestcost);
	}

  return 0;
}
