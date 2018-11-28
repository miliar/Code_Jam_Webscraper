#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <map>

using namespace std;

void solve_case(int N, int case_num) {
  	stringstream answer;
  	int M = N;
	map <char, bool> seen;
  	bool done = false;

  	for (int i = 0; i < 1000; ++i) {
  		stringstream ss;
  		ss << M;
  		string s = ss.str();
  		for (int j = 0; j < s.length(); ++j) {
  			char c = s.at(j);
  			if (seen.find(c) == seen.end()) {
  				seen[c] = true;
  			}
  		}
  		if (seen.size() == 10) {
  			answer << M;
  			done = true;
  			break;
  		}
  		M += N;
  	}

  	if (!done) answer << "INSOMNIA";

  	cout << "Case #" << case_num+1 << ": " << answer.str() << "\n";
}


int main() {
  	int T;
  	cin >> T;
  	for (int i = 0; i < T; i++) {
    	int N;
    	cin >> N;
    	solve_case(N, i);
 	}
}
