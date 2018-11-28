#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

const int MAX_SIZE = 1000;

int result(vector<int> v) {

    int minTime = MAX_SIZE;

    for(int maxSizeEnd = 1; maxSizeEnd <= MAX_SIZE; maxSizeEnd++) {
	int cur = maxSizeEnd;
	for(int p : v) {
	    cur += (p-1)/maxSizeEnd;
	}
	minTime = min(minTime,cur);
    }
    
    return minTime;
}

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
	int D;
	cin >> D;
	vector<int> v;
	for(int i = 0; i < D; i++) {
	    int p;
	    cin >> p;
	    v.push_back(p);
	}
	cout << "Case #" << t+1 <<": " << result(v) << endl;
    }
    return 0;
}
