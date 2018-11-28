#include <iostream>
#include <vector>
#include <string>

using namespace std;

int eatAll(const vector<int> &v) {
	int ret = 0;
	for(int i=1; i<v.size(); i++) {
		if (v[i-1]>v[i]) {
			ret += v[i-1]-v[i];
		}
	}
	return ret;
}

int eatFix(const vector<int> &v) {
	int minRate = 0;
	for (int i=1; i<v.size(); i++) {
		int dum = v[i-1]-v[i];
		minRate = (dum>minRate)?dum:minRate;	
	}

	int count = 0;
	for (int i=1; i<v.size(); i++) {
		count += (minRate>v[i-1])?v[i-1]:minRate;
	}
	return count;
}

int main() {
	int nCase;
	cin >> nCase;
	for (int i=0; i<nCase; i++) {
		cout << "Case #" << i+1 << ": ";
		vector<int> v;
		int N, dum;
		cin >> N;
		for (int i=0; i<N; i++) {
			cin >> dum;
			v.push_back(dum);
		}

		cout << eatAll(v) << " ";
		cout << eatFix(v) << endl;
	}
}
