#include <fstream>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;
int T, n, m, B, sol, codin[110][510], codout[110][510], S, D, C[100100][16], F[100100][16];
bool cladire[110][510];
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
vector <int> G[100100];
queue <int> Q;
int pred[100100];

inline bool BFS()
{
	int i, x;
	for(i = 1; i <= D; ++i)
		pred[i] = 0;
    Q.push(S);
    pred[S] = -1;
    while(!Q.empty())
    {
        x = Q.front();
        Q.pop();
        for(i = 0; i < G[x].size(); ++i)
        {
            if(pred[G[x][i]] == 0)
            {
                if(F[x][i] < C[x][i])
                {
                    pred[G[x][i]] = x;
                    Q.push(G[x][i]);
                }
            }
        }
    }
    if(pred[D] == 0)
        return false;
    return true;
}

inline void Maxflow()
{
	int i, x, j, val;
	sol = 0;
	while(BFS())
	{
		for(i = 0; i < G[D].size(); ++i)
        {
            x = G[D][i];
			j = 0;
			while(G[x][j] != D)
				j++;
            if(F[x][j] < C[x][j] && pred[x])
            {
                val = C[x][j] - F[x][j];
                while(x != S)
                {
					j = 0;
					while(G[pred[x]][j] != x)
						j++;
                    val = min(val, C[pred[x]][j] - F[pred[x]][j]);
                    x = pred[x];
                }
                x = G[D][i];
				j = 0;
				while(G[x][j] != D)
					j++;
                F[x][j] += val;
                F[D][i] -= val;
                while(x != S)
                {
					j = 0;
					while(G[pred[x]][j] != x)
						j++;
                    F[pred[x]][j] += val;
					j = 0;
					while(G[x][j] != pred[x])
						j++;
                    F[x][j] -= val;
                    x = pred[x];
                }
                sol += val;
            }
        }
	}
}

int main()
{
	int t, i, j, k, X0, Y0, X1, Y1, x, y;
	ifstream fin("C.in");
	ofstream fout("C.out");
	fin >> T;
	for(t = 1; t <= T; ++t)
	{
		fin >> n >> m >> B;
		for(i = 1; i <= n; ++i)
			for(j = 1; j <= m; ++j)
				cladire[i][j] = false;
		while(B--)
		{
			fin >> X0 >> Y0 >> X1 >> Y1;
			X0++;
			Y0++;
			X1++;
			Y1++;
			for(i = X0; i <= X1; ++i)
				for(j = Y0; j <= Y1; ++j)
					cladire[i][j] = true;
		}
		memset(C, 0, sizeof(C));
		memset(F, 0, sizeof(F));
		for(i = 1; i <= n; ++i)
			for(j = 1; j <= m; ++j)
			{
				codin[i][j] = (i - 1) * m + j;
				codout[i][j] = codin[i][j] + n * m;
			}
		S = 2 * n * m + 1;
		D = 2 * n * m + 2;
		for(i = 1; i <= n; ++i)
			for(j = 1; j <= m; ++j)
			{
				if(cladire[i][j])
					continue;
				G[codin[i][j]].push_back(codout[i][j]);
				G[codout[i][j]].push_back(codin[i][j]);
				C[codin[i][j]][G[codin[i][j]].size() - 1] = 1;
				for(k = 0; k < 4; ++k)
				{
					x = i + dx[k];
					y = j + dy[k];
					if(1 <= x && x <= n && 1 <= y && y <= m && !cladire[x][y])
					{
						G[codout[i][j]].push_back(codin[x][y]);
						G[codin[x][y]].push_back(codout[i][j]);
						C[codout[i][j]][G[codout[i][j]].size() - 1] = 1;
					}
				}
			}
		for(i = 1; i <= n; ++i)
		{
			if(!cladire[i][1])
			{
				G[S].push_back(codin[i][1]);
				G[codin[i][1]].push_back(S);
				C[S][G[S].size() - 1] = 1;
			}
			
			if(!cladire[i][m])
			{
				G[codout[i][m]].push_back(D);
				G[D].push_back(codout[i][m]);
				C[codout[i][m]][G[codout[i][m]].size() - 1] = 1;
			}
		}
		Maxflow();
		fout << "Case #" << t << ": " << sol << "\n";
		for(i = 1; i <= n; ++i)
			for(j = 1; j <= m; ++j)
			{
				G[codin[i][j]].clear();
				G[codout[i][j]].clear();
			}
		G[S].clear();
		G[D].clear();
	}
	fin.close();
	fout.close();
	return 0;
}
