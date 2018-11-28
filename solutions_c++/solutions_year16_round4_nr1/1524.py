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

vector<char> reduce(const vector<char>& input) {
	if (input.size() == 0) return vector<char>();

	vector<char> result(input.size() / 2);
	for (int i = 0; i < result.size(); i++) {
		char c1 = input[2*i], c2 = input[2*i+1], c3;
		if (c1 == c2) {
			return vector<char>();
		}
		if (c1 == 'R')
			c3 = (c2 == 'P') ? 'P' : 'R';
		else if (c1 == 'P')
			c3 = (c2 == 'S') ? 'S' : 'P';
		else {
			c3 = (c2 == 'R') ? 'R' : 'S';
		}
		result[i] = c3;
	}
	return result;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
    	int N, R, P, S;
    	cin >> N >> R >> P >> S;

    	vector<char> buf;
    	for (int i = 0; i < P; i++) {
    		buf.push_back('P');
    	}
    	for (int i = 0; i < R; i++) {
    		buf.push_back('R');
    	}
    	for (int i = 0; i < S; i++) {
    		buf.push_back('S');
    	}

    	vector<char> result;
    	do {
    		result = buf;
    		for (int i = 0; i < N; i++) {
    			result = reduce(result);
    		}
    		if (result.size() > 0) break;
    	} while (next_permutation(buf.begin(), buf.end()));

        cout << "Case #" << testCase << ": ";
        if (result.size() > 0) {
        	for (char c : buf) cout << c;
        } else {
        	cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
}
