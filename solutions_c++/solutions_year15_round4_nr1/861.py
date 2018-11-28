#include<iostream>
#include<vector>

using namespace std;

int main(){
	int tests;

	cin >> tests;

	for(int test = 1; test <= tests; ++test){
		int m, n;
		bool possible = true;
	
		cin >> m >> n;
		vector<string> grid(m);

		for(int i = 0; i < m; ++i)
			cin >> grid[i];

		vector<int> countn1(n, 0);
		vector<int> countm1(m, 0);
		vector<int> countn2(n, 0);
		vector<int> countm2(m, 0);

		int sum = 0;

		for(int i = 0; i < m; ++i)
			for(int j = 0; j < n; ++j){
				if(grid[i][j] != '.'){
					countn1[j] += 1;
					if(countn1[j] == 1 && grid[i][j] == '^')
						sum += 1;
				}
			}

		for(int i = m-1; i >= 0; --i)
			for(int j = 0; j < n; ++j){
				if(grid[i][j] != '.'){
					countn2[j] += 1;
					if(countn2[j] == 1 && grid[i][j] == 'v')
						sum += 1;
				}
			}

		for(int j = 0; j < n; ++j)
			for(int i = 0; i < m; ++i){
				if(grid[i][j] != '.'){
					countm1[i] += 1;
					if(countm1[i] == 1 && grid[i][j] == '<')
						sum += 1;
				}
			}

		for(int j = n-1; j >= 0; --j)
			for(int i = m-1; i >= 0; --i){
				if(grid[i][j] != '.'){
					countm2[i] += 1;
					if(countm2[i] == 1 && grid[i][j] == '>')
						sum += 1;
				}
			}

		for(int i = 0; i < m && possible; ++i)
			for(int j = 0; j < n && possible; ++j){
				if(grid[i][j] != '.' && countn1[j] == 1 && countm1[i] == 1){
					possible = false;
				}
			}


		cout << "Case #" << test << ": ";
		if(possible)
			cout << sum << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
