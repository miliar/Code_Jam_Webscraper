#include <iostream>
#include <vector>

using namespace std;

void solve(int test){
	int n = 0, m = 0;
	cin >> n >> m;
	
	vector<vector<int> > lvec(n);
	vector<vector<int> > maxvec(n);
	for(int i=0; i < n; i++){
		lvec[i].resize(m);
		maxvec[i].resize(m);
	}

	for(int i = 0; i < n; i++){
		int max = 0;
		for(int j = 0; j < m; j++){
			cin >> lvec[i][j];
			if(lvec[i][j] > max) max = lvec[i][j];
		}
		for(int j = 0; j < m; j++){
			if(lvec[i][j] == max) maxvec[i][j] = 1;//this is the max in this row.
			else maxvec[i][j] = 0;
		}
	}

	for(int j = 0; j < m; j++){
		int max = 0;
		for(int i = 0; i <n; i++){
			if(lvec[i][j] > max) max = lvec[i][j];
		}
		for(int i = 0; i<n; i++){
			if(lvec[i][j] == max) maxvec[i][j] = 1;
		}
	}

	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			if(maxvec[i][j] == 0){
				cout << "Case #" << test << ": " << "NO" << endl;
				return;
			}
		}
	}

	cout << "Case #" << test << ": " << "YES" << endl;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests = 0;
	scanf("%d", &tests);
	for(int i=1; i <= tests; ++i){
		solve(i);
	}
}