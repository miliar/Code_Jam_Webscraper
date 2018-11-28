#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iterator>
using namespace std;

const string file = "file";

const string infile = file + ".in";
const string outfile = file + ".out";

const int INF = 0x3f3f3f3f;

int MaxFlow;
int N, M;



struct Arc
{
	int dst;
	int cap;
	int flux;
	int p;
	Arc(int dst, int cap, int p)
    {
        this->dst = dst;
        this->cap = cap;
        this->flux = 0;
        this->p = p;
    }

};

vector<bool> uz;
int S;
int T;

vector<Arc> arcs;
vector<vector<int> > G;

vector<int> dijParent;
vector<int> dijArc;



bool bfs(int x)
{
    uz.clear();
    uz.resize(2 * N * M + 2);
    queue<int> q;
    q.push(x);

    uz[S] = true;

    while(q.empty() == false)
    {
        int c = q.front();
        q.pop();

        if ( c == T)
            return true;

        for(vector<int>::iterator itr = G[c].begin();
            itr != G[c].end();
            itr++)
        {
			if(uz[arcs[*itr].dst] == true)
                continue;

			if(arcs[*itr].cap - arcs[*itr].flux > 0)
			{
				uz[arcs[*itr].dst] = true;
				dijParent[arcs[*itr].dst] = c;
				dijArc[arcs[*itr].dst] = *itr;
				q.push(arcs[*itr].dst);
			}
        }
    }
    return false;
}


int toInt(int i, int j)
{
	return i * M + j;
}

bool isIn(int i, int j)
{
	return (0 <= i && i < N && 0 <= j && j < M);
}

int di[] = {-1, 0, 1, 0};
int dj[] = {0, -1, 0, 1};


void addEdge(int x, int y)
{
	G[x].push_back(arcs.size());
	G[y].push_back(arcs.size() + 1);

	Arc to(y, 1, arcs.size() + 1);
    Arc from(x, 0, arcs.size());

	arcs.push_back(to);
	arcs.push_back(from);
}


int main()
{
    fstream fin(infile.c_str(), ios::in);
	fstream fout(outfile.c_str(), ios::out);

	int Z;
	fin >> Z;
	for(int t = 1; t <= Z; t++)
	{
		fin >> N >> M;

		MaxFlow = 0;


		G.clear();
		dijParent.clear();
		dijArc.clear();
		arcs.clear();

		dijParent.resize(2 * N * M + 2, -1);
		dijArc.resize(2 * N * M + 2, -1);


		G.resize(2 * N * M + 2);

		T = 2 * N * M + 1;
		S = 2 * N * M;

		for(int i = 0; i < N; i++)
		{
			addEdge(S, toInt(i, 0));

			addEdge(toInt(i, M -1) + N * M, T);

		}

		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < M; j++)
			{
				addEdge(toInt(i, j), toInt(i, j) + N * M);


				for(int k = 0; k < 4; k++)
				{
					int ni = i + di[k];
					int nj = j + dj[k];
					if(isIn(ni, nj) == false)
						continue;


					int sour = toInt(i, j);
					sour += N * M;
					int dst = toInt(ni, nj);
					addEdge(sour, dst);


				}
			}

		}

		int x;
		fin >> x;
		for(int k = 0; k < x; k++)
		{
			int a, b, c, d;
			fin >> a >> b >> c >> d;

			for(int i = a; i <= c; i++)
			{
				for(int j = b; j <= d; j++)
				{

					for(vector<int>::iterator itr = G[toInt(i, j)].begin();
						itr != G[toInt(i, j)].end();
						itr++)
					{
						if(arcs[*itr].dst == toInt(i, j) + N * M)
						{
							arcs[*itr].cap = 0;
							break;
						}
					}
				}
			}
		}

		while(bfs(S))
		{
			//for(vector<int>::iterator itr = G[T].begin();
				//itr != G[T].end();
				//itr++)
			{
				//if(uz[*itr] && Cap[*itr][T] - Flux[*itr][T] > 0)
				//{
					//prec[T] = *itr;

					int minflow = INF;
					for(int n = T; n != S; n = dijParent[n])
					{
						minflow = min(minflow, arcs[dijArc[n]].cap - arcs[dijArc[n]].flux);
					}

					if(minflow == 0)
						continue;

					MaxFlow += minflow;

					for(int n = T; n != S; n = dijParent[n])
					{

						arcs[dijArc[n]].flux += minflow;
						arcs[arcs[dijArc[n]].p] .flux -= minflow;
					}


				//}
			}
		}

		fout << "Case #" << t << ": " << MaxFlow << "\n";

	}

    fout.close();
}
