#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>

#define D(x) x

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
	os << "[";
	for (int i = 0; i < vec.size(); i++) {
		if (i > 0) os << ", ";
		os << vec[i];
	}
	os << "]";
	return os;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
    	int N, K;
    	cin >> N >> K;

    	vector<double> p(N);
    	for (int i = 0; i < N; i++) {
    		cin >> p[i];
    	}

    	double best = 0.0;

    	for (int bitmask = 0; bitmask < (1<<N); bitmask++) {
    		int count = 0;
    		for (int i = 0; i < N; i++) {
    			if (bitmask & (1<<i)) count++;
    		}
    		if (count != K) continue;

    		vector<double> outcomes = {1.0};
    		for (int i = 0; i < N; i++) {
    			if (bitmask & (1<<i)) {
    				vector<double> next(outcomes.size() + 1);
    				for (int x = 0; x < next.size(); x++) {
    					if (x < outcomes.size()) next[x] += outcomes[x] * (1.0 - p[i]);
    					if (x > 0) next[x] += outcomes[x-1] * p[i];
    				}
    				outcomes = next;
    			}
    		}
    		best = max(best, outcomes[K/2]);

    	}
        cout << "Case #" << testCase << ": " << best << endl;
    }
}
