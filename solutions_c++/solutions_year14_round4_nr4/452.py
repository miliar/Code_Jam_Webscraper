#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector <ll> VI;
typedef vector <VI> VVI;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef pair <ll, ll> PII;
typedef set <int> SI;
typedef set <string> SS;
typedef map <int, int> MII;

void Backtracking (int z, VI &pos, vector <vector <string> > &V, int &maxim, int &tot, int M, int N){
	if (z == M){
		vector <SS> vv(N);
		for (int i = 0; i < N; ++i){
			int cont = 0;
			for (int j = 0; j < M; ++j){
				if (pos[j] == i){
					++cont;
					for (int k = 0; k < V[j].size(); ++k) vv[i].insert(V[j][k]);
				}
			}
			if (cont == 0) return;
		}
		int total = 0;
		for (int i = 0; i < N; ++i){
			total += vv[i].size();
		}
		if (total > maxim){
			maxim = total;
			tot = 1;
		}
		else if (total == maxim) ++tot;
		return;
						
					
					
	}
	for (int i = 0; i < N; ++i){
		pos[z] = i;
		Backtracking(z+1, pos, V, maxim, tot, M, N);
	}
}

int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t){
		int M, N;
		cin >> M >> N;
		vector <string> v(M);
		for (int i = 0; i < M; ++i) cin >> v[i];
		vector <vector <string> > V(M);
		for (int i = 0; i < M; ++i){
			string s;
			V[i].push_back(s);
			for (int j = 0; j < (int) v[i].size(); ++j){
				s.push_back(v[i][j]);
				V[i].push_back(s);
			}
		}
		//cout << "ola k ase" << endl;
		int tot = 0;
		int maxim = -1;
		VI pos(M);
		Backtracking(0, pos, V, maxim, tot, M, N);
		cout << "Case #" << t << ": " << maxim << " " << tot << endl;
		
		
	}
	
}
