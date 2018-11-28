#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int T;

	scanf("%d", &T);
	int i;
	int l;
	int N;
	int id;
	vector<string> a;

	string c;
	string s;
	vector<int> current_positions;
	vector<int> current;
	int j, k, m;
	int sum;
	int current_large;
	bool out = false;
	int medium;
	for (l = 1; l <= T; ++l){
		c.clear();
		out = false;
		scanf("%d", &N);
		a.clear();
		sum = 0;
		current_positions.assign(N, 0);
		current.assign(N, 0);
		for (i = 0; i<N; ++i){
			cin >> s;
			a.push_back(s);
		}
		c.push_back(a[0][0]);
		for (i = 1; i<a[0].size(); ++i){
			if (c.back() != a[0][i]){
				c.push_back(a[0][i]);
			}
		}

		for (i = 0; i<c.size(); ++i){
			current.assign(N, 0);
			if (out)break;
			current_large = 0;
			for (j = 0; j< N; ++j){
				while ((current_positions[j] <  a[j].size()) && (a[j][current_positions[j]] == c[i])){
					++current_positions[j];
					++current_large;
					++current[j];
				}
				if (current[j] == 0){
					printf("Case #%d: Fegla Won\n", l);
					out = true;
					break;
				}
			}

			current_large = round(((double)current_large) / N);
			for (j = 0; j< N; ++j){
				sum += abs(current[j] - current_large);
			}
		}
		if (out == true ) continue;
		for (j = 0; j< N; ++j){
			if (current_positions[j] != a[j].size()){
				printf("Case #%d: Fegla Won\n", l);
				out = true;
				break;
			}
		}
		if (out == true)
			continue;
		printf("Case #%d: %d\n", l, sum);
	}



	return 0;
}
