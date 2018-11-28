/*	Try wygrać except trudno
 *	Stanisław Dobrowolski, Katarzyna Jabłonowska, Arkadiusz Wróbel
 *
 *	Zadanie: 
 *	Konkurs: 
 */
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)
#define FOREACH(IT, CON) for(__typeof(CON.begin()) IT=CON.begin(); IT!=CON.end(); ++IT)
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
#define SIZE(CON) ((int)CON.size())
const int INF=1000000000;
const LL INFLL=1000000000000000000LL;
int t, d, pocz, kon, srod, wyn;
int P[100005];
int wynik[100000];

int main()
{
	scanf("%d", &t);
	for (int z=0; z<t; z++)
	{
		scanf("%d", &d);
		int ileMax = 0;
		for (int i=0; i<d; i++)
		{
			scanf("%d", &P[i]);
			ileMax = max(ileMax, P[i]);
		}
		int ileCiec = 0;
		int m;
		wyn = INF;
		for (int i=1; i<ileMax+5; i++)
		{
			ileCiec = 0;
			m = 0;
			for (int j=0; j<d; j++)
			{
				ileCiec+=ceil(P[j]/(double)i)-1;
			}
			wyn = min(wyn, ileCiec+i);
		}
		printf("Case #%d: %d\n", z+1, wyn);
	}
	return 0;
}

