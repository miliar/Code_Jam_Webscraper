
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <utility>
#include <string>
#include <queue>
#include <bitset>
#include <set>
#include <utility>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>

#define mp make_pair
#define f first
#define s second
#define dim 1000009
#define oo 0x3f3f3f3f
#define pb push_back

using namespace std;


int X;

int dist[dim];

bitset < dim > uz;
queue < int > Q;

vector < int > G[dim];
typedef vector < int >::iterator IT;

void build();
void Bfs(int x);
int ogl(int x)
{
	int cp = x;
	int nr = 0;
	while (cp)
	{
		nr = 10 * nr + cp % 10;
		cp /= 10;
	}
	return nr;
}

int main()
{

	int T;
	cin >> T;

	build();
	Bfs(1);
	int i = 1;
	for (int X; T; --T)
	{
		cin >> X;
		cout << "Case #" << i << ": " << dist[X] + 1 << '\n';
			i++;
	}

	return 0;

}


void build()
{

	for (int i = 1; i <= 1000000; i++)
	{

		int nr1 = i + 1;
		int nr2 = ogl(i);
		G[i].pb(nr1);

		if (nr2 != i)
			G[i].pb(nr2);

	}

}


void Bfs(int x)
{

	dist[x] = 0;
	Q.push(x);
	uz[x] = 1;

	while (!Q.empty())
	{
		int k = Q.front();
		Q.pop();

		for (IT i = G[k].begin(); i != G[k].end(); ++i)
			if (!uz[*i])
			{
				dist[*i] = dist[k] + 1;
				uz[*i] = 1;
				Q.push(*i);
			}

	}

}
