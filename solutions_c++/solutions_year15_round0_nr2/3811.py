#include <bits/stdc++.h>

using namespace std;

vector < int > vet;

int bfs( ){
	queue < pair < int, vector < int > > > fila;
	fila.push(make_pair(0,vet));
	set < vector < int > > used;
	while( !fila.empty() ){
		pair < int, vector < int > >  at = fila.front();
		fila.pop();
		int tam = at.second.size();
		int ok = 1, mm = 0, idx = 0;
		for( int i = 0; i < tam; i++ ){
			if( at.second[i] > 0 ){
				ok = 0;
			}
			if( at.second[i] > mm ){
				mm = at.second[i];
				idx = i;
			}
			at.second[i]--;
		}
		if( ok ) return at.first;
		fila.push(make_pair(at.first+1,at.second));
		for( int i = 0; i < tam; i++ ) at.second[i]++;
		for( int i = 1; i <= mm>>1; i++ ){
			at.second[idx] -= i;
			at.second.push_back(i);
			if( !used.count(at.second) ){
				used.insert(at.second);
				fila.push(make_pair(at.first+1,at.second));
			}
			at.second[idx] += i;
			at.second.pop_back();
		}
	}
	return 0;
}

int main(){
	ios::sync_with_stdio(false);
	int t, k = 1, n, val;
	cin >> t;
	while( t-- ){
		cin >> n;
		int ans = 0;
		vet.clear();
		for( int i = 0; i < n; i++ ){
			cin >> val;
			vet.push_back(val);
		}
		ans = bfs();
		cout << "Case #" << k++ << ": " << ans << "\n";
	}
	return 0;
}