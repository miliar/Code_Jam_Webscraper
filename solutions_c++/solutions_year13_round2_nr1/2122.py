#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int min(int a, int b) {
	if(a < b) {
		return a;
	} else {
		return b;
	}
}

int solve(int size, vector<int> &v) {
	int answer = v.size();
	int oper = 0;
	int i = 0;
	while(i < v.size()) {
		if(v[i] < size) {
			size += v[i];
			i++;
		} else {
			answer = min(oper+v.size()-i, answer);
			oper++;
			if(size == 1) {
				i++;
			} else {
				size = 2*size - 1;
			}
		}
	}
	
	return min(answer, oper);
}

int main() {
	int T, size, N, t, i;
	cin >> T;
	
	for(i=1; i<=T; i++) {
		cin >> size >> N;
		vector<int> v;
		for(int j=0; j<N; j++) {
			cin >> t;
			v.push_back(t);
		}
		
		sort(v.begin(), v.end());
		cout << "Case #" << i << ": " << solve(size, v) << endl;
	}
	return 0;
}
