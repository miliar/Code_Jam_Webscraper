#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
	int T; // number of tests
	scanf("%d", &T);

	vector<vector<int> > result;

	for (int i = 0; i < T; i++) {
		int N;
		scanf("%d", &N);

		map<int, int> mymap;

		for (int j = 0; j < N*2-1; j++) {
			for (int k = 0; k < N; k++) {
				int a;
				scanf("%d", &a);
				map<int,int>::iterator it=mymap.find(a);
				if (it != mymap.end()) {
					mymap.erase(it);
				} else {
					mymap[a] = 1;
				}
			}
		}

		vector<int> v;
		for (map<int,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it) {
			v.push_back(it->first);
		}

		sort(v.begin(), v.end());
		result.push_back(v);
	}

	for (int i = 0; i < T; i++) {
		vector<int> v = result[i];
		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < v.size(); j++) {
			cout << v[j];
			if (j != v.size()-1) {
				cout << " ";
			}
		}
		cout << endl;
	}
}
