#include <cstdio>
#include <utility>
#include <algorithm>
#include <vector>
#include <set>

#define mp make_pair
#define point pair<int, int> 
#define px first
#define py second
#define INF 100000000
#define EPS 1e-9
#define rfloat(x) scanf("%lf", &(x))
#define rint(x) scanf("%d", &(x))
#define loop(i, x) for (int i = 0; i < (x); i++)

using namespace std;

int N;

double P1[1000];
double P2[1000];

int playWar();

void change()
{
	loop(i, N)
		swap(P1[i], P2[i]);
}

int playDeceit()
{
	change();
	int ans = N - playWar();
	change();
	return ans;
}

int playWar()
{
	int rem = N;
	int points = 0;
	
	while (rem)
	{
		double block = P1[0];
		swap(P1[0], P1[rem-1]);
		
		double best = 0;
		int bestIndex = -1;
		loop(i, rem)
		{
			if (bestIndex < 0 || (best > block && P2[i] > block && P2[i] < best) || (best < block && P2[i] < best) || (best < block && P2[i] > block))
			{
				best = P2[i];
				bestIndex = i;
			}
		}
		
		if (best < block)
			points++;
		
		swap(P2[bestIndex], P2[rem-1]);
		rem--;
	}
	
	return points;
}

int main()
{
	int cases;
	rint(cases);
	
	loop(testcase, cases)
	{
		rint(N);
		
		loop(i, N)
			rfloat(P1[i]);
		loop(i, N)
			rfloat(P2[i]);
		
		printf("Case #%d: %d %d\n", testcase+1, playDeceit(), playWar());
	}
}