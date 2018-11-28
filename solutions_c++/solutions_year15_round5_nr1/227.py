#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <functional>
#include <cstdint>
#include <cmath>
#include <unordered_set>
#include <unordered_map>
#include <sstream>

#define D(x)

using namespace std;

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
    	int N, D;
    	cin >> N >> D;
    	vector<int> S(N), M(N);

    	int As, Cs, Rs;
    	cin >> S[0] >> As >> Cs >> Rs;
    	int Am, Cm, Rm;
    	cin >> M[0] >> Am >> Cm >> Rm;

    	for (int i = 1; i < N; i++) {
    		S[i] = (int) (((long long) S[i-1] * As + Cs) % Rs);
    		M[i] = (int) (((long long) M[i-1] * Am + Cm) % Rm);
    	}
    	for (int i = 1; i < N; i++) {
    		M[i] = M[i] % i;
    	}

    	vector<pair<int, int>> pairs;
    	for (int i = 0; i < N; i++) {
    		pairs.push_back({S[i], i});
    	}
    	sort(pairs.begin(), pairs.end());

    	vector<int> activeDescendants(N);
    	vector<bool> isActive(N);

    	int endIdx = 0;
    	int maxEmployees = 0;

    	for (int startIdx = 0; startIdx < N; startIdx++) {
    		int start = pairs[startIdx].second;

    		while (endIdx < N && pairs[endIdx].first - pairs[startIdx].first <= D) {
    			int end = pairs[endIdx].second;
    			D(cerr << "adding " << end << endl);
    			isActive[end] = true;
    			// propagate upward
    			int current = end;
    			while (current > 0 && isActive[current]) {
    				activeDescendants[M[current]] += activeDescendants[end]+1;
    				D(cerr << "  active[" << M[current] << "] <- " << activeDescendants[M[current]] << endl);
    				current = M[current];
    			}
    			endIdx++;
    		}
    		if (isActive[0]) {
    			D(cerr << "max is " << activeDescendants[0] + 1 << endl);
    			maxEmployees = max(maxEmployees, activeDescendants[0]+1);
    		}
    		
    		D(cerr << "removing " << start << endl);
    		int current = start;
    		while (current > 0 && isActive[current]) {
    			activeDescendants[M[current]] -= activeDescendants[start]+1;
    			D(cerr << "  active[" << M[current] << "] <- " << activeDescendants[M[current]] << endl);
    			current = M[current];
    		}
    		isActive[start] = false;
    	}

        cout << "Case #" << testCase << ": " << maxEmployees << endl;
    }
}
