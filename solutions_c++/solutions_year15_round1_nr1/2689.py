#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main(){

	int t, n, maior1, maior2, rate, ant;
	vector<int> pedacos(200);
	cin >> t;

	for (int i = 0; i < t; i ++){
		cin >> n;
		maior1 = 0; ant = 0; rate = 0;
		for (int j = 0; j<n; j++){
			cin >> pedacos[j];
			if (ant - pedacos[j] > 0) maior1 += ant-pedacos[j];
			if (rate < (ant - pedacos[j])) rate = ant - pedacos[j];
			ant = pedacos[j];
		}
		maior2 = 0;
		for (int j = 0; j < n-1; j++){
			maior2 += min(rate, pedacos[j]);
		}

		cout << "Case #" << i+1 << ": " << maior1 << " " << maior2 << endl;

	}

	return 0;
}
