#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

const double eps = 1e-9;
const int inf = 1e9 + 23;

const int size = 200;

int grass[size][size], des[size][size];

int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N;
	cin >> N;
	
	for (int it = 1; it <= N; it++){
		cout << "Case #" << it << ": ";
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++){
				cin >> des[i][j];
				grass[i][j] = 100;
			}
		for (int i = 0; i < n; i++){
			int Max = 0;
			for (int j = 0; j < m; j++)
				Max = max(Max, des[i][j]);
			for (int j = 0; j < m; j++)
				grass[i][j] = min(grass[i][j], Max);
		}
		for (int j = 0; j < m; j++){
			int Max = 0;
			for (int i = 0; i < n; i++)
				Max = max(Max, des[i][j]);
			for (int i = 0; i < n; i++)
				grass[i][j] = min(grass[i][j], Max);
		}
		bool flag = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (grass[i][j] != des[i][j])
					flag = false;
		if (flag)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}

	return 0;
}