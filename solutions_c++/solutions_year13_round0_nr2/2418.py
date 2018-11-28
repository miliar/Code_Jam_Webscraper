#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void){
	int T;
	cin >> T;

	for(int t=1;t<=T;t++){
		cout << "Case #"<<t<<": ";
		int n,m; cin >> n >> m;
		vector<vector<int> > g(n,vector<int> (m));
		vector<int> N(n),M(m);
		for(int i=0;i<n;i++){
			int ma = 0;
			for(int j=0;j<m;j++){ cin >> g[i][j]; ma = max(ma,g[i][j]); /*cout << g[i][j] << " ";*/ }
			N[i] = ma;//	cout << "*" << N[i] << endl;
		}
		for(int i=0;i<m;i++){
			int ma = 0;
			for(int j=0;j<n;j++){  ma = max(ma,g[j][i]); /*cout << g[j][i] << " ";*/ }
			M[i] = ma;// cout <<"+"<< M[i] << endl;
		}
		bool kos = true;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				if(g[i][j] != min(N[i],M[j]))kos = false;
		if(kos){cout << "YES" <<endl; }
		else cout << "NO" << endl;
	}
}