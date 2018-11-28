#include <iostream>
#include <vector>
using namespace std;

int main(){
	int c;
	cin >> c;
		
	for(int k = 0; k < c; ++k){
	
		int n,m;
		cin >> n >> m;

		vector<int> h(n,-1);
		vector<int> v(m,-1);
		vector< vector<int> > matriu(n,vector<int>(m));

		for(int i = 0; i < n; ++i){
			for(int j = 0; j < m; ++j){
				int a;
				cin >> a;
				matriu[i][j] = a;
				if(h[i] < a) h[i] = a;
				if(v[j] < a) v[j] = a;		
			}
		}
		bool continuar = true;
		for(int i = 0; i < n and continuar; ++i){
			for(int j = 0; j < m and continuar; ++j){
				if(matriu[i][j] < h[i] and matriu[i][j] < v[j]) continuar = false;
			}
		}

		if(continuar) cout << "Case #" << k + 1 << ": YES" << endl;
		else cout << "Case #" << k + 1 << ": NO" << endl;
		
	}
}
