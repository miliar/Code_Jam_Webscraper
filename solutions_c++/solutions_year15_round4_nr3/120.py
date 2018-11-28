#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue>
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 

using namespace std; 

typedef long long ll; 
typedef pair<int, int> pii;

#define INF 1000000000
#define pb push_back 
#define itr iterator 
#define sz size() 
#define mp make_pair

//Input: cap (matriz de adjacência das capacidades), n, s (fonte), t (destino)
//output: retorna o fluxo, se prev[v] == -1, então não há caminho s->v no min cut

#include <string.h>
#include <stdio.h>
#include <algorithm>

using namespace std;

// the maximum number of vertices
#define NN 10100

// adjacency matrix (fill this up)
// If you fill adj[][] yourself, make sure to include both u->v and v->u.
int cap[NN][NN], deg[NN], adj[NN][NN];

// BFS stuff
int q[NN], prv[NN];

int dinic( int n, int s, int t )
{
    int flow = 0;

    // init the adjacency list adj[][] from cap[][]
    memset( deg, 0, sizeof( deg ) );
    for( int u = 0; u < n; u++ )
        for( int v = 0; v < n; v++ ) if( cap[u][v] || cap[v][u] )
            adj[u][deg[u]++] = v;

    while( true )
    {
        memset( prv, -1, sizeof( prv ) );
        int qf = 0, qb = 0;
        prv[q[qb++] = s] = -2;
        while( qb > qf && prv[t] == -1 )
            for( int u = q[qf++], i = 0, v; i < deg[u]; i++ )
                if( prv[v = adj[u][i]] == -1 && cap[u][v] )
                    prv[q[qb++] = v] = u;

        if( prv[t] == -1 ) break;

        for( int z = 0; z < n; z++ ) if( cap[z][t] && prv[z] != -1 )
        {
            int bot = cap[z][t];
            for( int v = z, u = prv[v]; u >= 0; v = u, u = prv[v] )
                bot = min(bot, cap[u][v]);
            if( !bot ) continue;

            cap[z][t] -= bot;
            cap[t][z] += bot;
            for( int v = z, u = prv[v]; u >= 0; v = u, u = prv[v] )
            {
                cap[u][v] -= bot;
                cap[v][u] += bot;
            }
            flow += bot;
        }
    }

    return flow;
}

int T, teste;
map<string, int> words;
int n, totwds;
char linha[110000];
string engwd, frewd;
string wd;

int main() {
	for(scanf("%d", &T); T; T--) {
		printf("Case #%d: ", ++teste);
		memset(cap,0,sizeof(cap));
		memset(deg,0,sizeof(deg));
		words.clear();
		totwds = 0;

		scanf("%d", &n);

		gets(linha);
		gets(linha);
		stringstream ss;
		ss << linha;

		int engwds = 0;
		while (ss >> engwd) {
			if (words.count(engwd) == 0) {
				words[engwd] = totwds++;
				engwds++;

				cap[0][n+2+words[engwd]] = 1;
			}
		}

		int ans = 0;

		gets(linha);
		stringstream ss2;
		ss2 << linha;

		int frewds = 0;
		while (ss2 >> frewd) {
			if (words.count(frewd) == 0) {
				words[frewd] = totwds++;
				frewds++;

				cap[n+2+words[frewd]][1] = 1;
			}
			else if (words[frewd] < engwds) {
				if (cap[0][n + 2 + words[frewd]]) {
					cap[0][n + 2 + words[frewd]] = 0;
					ans++;
				}
			}
		}

		int loosewds = 0;
		for (int i = 0; i < n-2; i++) {
			gets(linha);
			stringstream ss;
			ss << linha;

			while (ss >> wd) {
				if (words.count(wd) == 0) {
					words[wd] = totwds++; 
					loosewds++;

					int idx = n+2 + engwds + frewds + 2*(words[wd]-engwds-frewds);

					cap[2+i][idx] = 10000000;
					cap[idx][idx+1] = 1;
					cap[idx+1][2+i] = 10000000;
				}
				else {
					int wordloc = words[wd];

					if (wordloc < engwds) {
						cap[n + 2 + wordloc][2+i] = 10000000;
					}
					else if (wordloc < engwds + frewds) {
						cap[2+i][n + 2 + wordloc] = 10000000;
					}
					else {
						int idx = n+2 + engwds + frewds + 2*(words[wd]-engwds-frewds);
						cap[2+i][idx] = 10000000;
						cap[idx+1][2+i] = 10000000;
					}
				}
			}
		}

		//printf("ans = %d\n", ans);
		printf("%d\n", ans + dinic(n + 2 + engwds + frewds + 2*loosewds, 0, 1));
	}
}