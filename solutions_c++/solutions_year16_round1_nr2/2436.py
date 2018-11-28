#include <bits/stdc++.h>

using namespace std;
int t, k = 1, val, n;
int used[100000], vis = 1;
int mat[100][100];
multiset < vector < int > > tem;
vector < vector < int > > vet;
set < vector < int > > opa;

void solve( int at, int w ){
	for(int z = 0; z < (1 << ((n*2)-1)); z++){
		if( __builtin_popcount(z) != n ) continue;
		vector < int > pegou;
		for(int j = 0; j < (2*n)-1; j++){
			if( z & (1 << j) ) pegou.push_back(j);
		}
		bool ok = true;
		for( int i = 0; i < pegou.size() && ok; i++ ){
			for(int j = 0; j < n; j++){
				mat[i][j] = vet[pegou[i]][j];
			}
			for(int j = 0; j < n; j++){
				if( mat[i-1][j] >= mat[i][j] ){
					ok = false;
					break;
				}
			}
		}
		if( !ok ) continue;
		multiset < vector < int > > aux = tem;
		vector < int > resp;
		int no = 0;
		for(int i = 0; i < n; i++){
			vector < int > linha;
			for( int j = 0; j < n; j++ ){
				linha.push_back(mat[i][j]);
			}
			multiset < vector < int > > :: iterator it = aux.find(linha);
			if( it == aux.end() ){
				no++;
				if( no > 1 ){
					ok = false;
					break;
				}
				resp = linha;
			}
			else aux.erase(it);
		}
		for(int i = 0; i < n; i++){
			vector < int > coluna;
			for( int j = 0; j < n; j++ ){
				coluna.push_back(mat[j][i]);
			}
			multiset < vector < int > > :: iterator it = aux.find(coluna);
			if( it == aux.end() ){
				no++;
				if( no > 1 ){
					ok = false;
					break;
				}
				resp = coluna;
			}
			else aux.erase(it);
		}
		if( ok && no == 1){
			cout << "Case #" << k++ << ":";
			for( int i = 0; i < n; i++ ) cout << " " << resp[i];
			cout << '\n';
			return;
		}
	}
}

int main(){
	ios::sync_with_stdio(false);
	
	cin >> t;
	while( t-- ){
		cin >> n;
		
		for(int i = 0; i < (2*n)-1; i++ ){
			vector < int > aux;
			for( int j = 0; j < n; j++ ){
				cin >> val;
				aux.push_back(val);
			}
			vet.push_back(aux);
			tem.insert(aux);
		}
		sort(vet.begin(), vet.end());
		solve(0, n);
		vet.clear();
		tem.clear();
		opa.clear();
		vis++;
	}
	return 0;
}