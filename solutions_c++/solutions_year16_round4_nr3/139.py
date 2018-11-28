#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int N,M,V[1010],g[1010];
map<vector<int>, pair<vector<int>, int> > u[1010];

void proc()
{
	scanf ("%d %d",&N,&M);
	for (int i=0;i<2*(N+M);i++){
		scanf ("%d",&V[i]);
		if (V[i] > M+N+M){
			V[i] -= M+N+M;
			V[i] = N-V[i]+1;
			V[i] *= 2;
			V[i] += M-1;
		}
		else if (V[i] > M+N){
			V[i] -= M+N;
			V[i] = 2*(N+M)-V[i]+1;
		}
		else if (V[i] > M){
			V[i] -= M;
			V[i] *= 2;
			V[i] += M;
		}
	}
	for (int i=0;i<2*(N+M);i+=2){
		g[V[i]] = V[i+1];
		g[V[i+1]] = V[i];
	}

	for (int i=0;i<=N*M;i++) u[i].clear();
	vector<int> fi;
	for (int i=0;i<=M;i++) fi.push_back(i+1);
	u[0][fi] = make_pair(vector<int>(),-1);
	for (int i=0;i<N;i++){
		for (int j=0;j<M;j++){
			map<vector<int>, pair<vector<int>, int> > &now = u[i*M+j], &nxt = u[i*M+j+1];
			for (auto &p : now){
				auto &v = p.first;
				// '/'
				{
					auto n = v;
					int a = n[M], b = n[j];
					if (a <= 0) n[-a] = b;
					if (b <= 0) n[-b] = a;
					if (a >= 1 && b >= 1){
						if (g[a] == b){
							n[M] = -j;
							n[j] = -M;
							nxt[n] = make_pair(v,0);
						}
					}
					else{
						n[M] = -j;
						n[j] = -M;
						nxt[n] = make_pair(v,0);
					}
				}

				// '\'
				{
					auto n = v;
					int a = n[M], b = n[j];
					if (a != -j){
						if (a <= 0) n[-a] = -j;
						if (b <= 0) n[-b] = -M;
						n[M] = b;
						n[j] = a;
					}
					nxt[n] = make_pair(v,1);
				}
			}
		}
		map<vector<int>, pair<vector<int>, int> > &now = u[i*M+M], tmp;
		for (auto &p : now){
			auto n = p.first;
			int a = n[M], b = M + i * 2 + 2;
			if (a <= 0) n[-a] = b;
			
			bool good = 1;
			if (a >= 1 && b >= 1 && g[a] != b) good = 0;

			if (good){
				n[M] = M + i * 2 + 3;
				tmp[n] = p.second;
			}
		}
		now = tmp;
	}

	map<vector<int>, pair<vector<int>, int> > &now = u[N*M];
	vector<int> st;
	for (auto &p : now){
		auto &n = p.first;
		bool good = 1;
		for (int j=0;j<M;j++){
			int a = n[j], b = M + N + N + j + 1;

			if (a <= 0){
				a = M + N + N - a + 1;
			}
			if (g[a] != b) good = 0;
		}
		if (good){
			st = n; break;
		}
	}

	if (st.empty()){
		puts("IMPOSSIBLE");
		return;
	}

	int map[1010] = {0,};
	for (int i=N-1;i>=0;i--) for (int j=M-1;j>=0;j--){
		auto p = u[i*M+j+1][st];
		map[i*M+j] = p.second;
		st = p.first;
	}

	for (int i=0;i<N;i++){
		for (int j=0;j<M;j++){
			putchar(map[i*M+j]?'\\':'/');
		}
		puts("");
	}
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		fprintf (stderr,"%d\n",Case);
		printf ("Case #%d:\n",Case);
		proc();
	}

	return 0;
}