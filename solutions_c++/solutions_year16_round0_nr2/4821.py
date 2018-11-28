#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

long solve(vector<bool>* vec){
	long count = 0;
	while(42) {
		for(int i = vec->size() - 1; i >= 0 &&  vec->at(i); i--) {
			vec->erase(vec->begin() + i);
		}

		if(vec->size() == 0) return count;

		vector<bool>::reverse_iterator tmp = vec->rbegin();
		int pos = vec->size() - 1;
		while(vec->at(pos) != vec->at(0))
			pos--;

		for(int i = 0; i <= pos; i++) {
			if(vec->at(i) == false) vec->at(i) = true;
			else vec->at(i) = false;
		}

		for(int i = 0; i <= pos / 2; i++) {
			bool tmp = vec->at(pos - i);
			vec->at(pos - i) = vec->at(i);
			vec->at(i) = tmp;
		}
		count++;
	}
}

int main() {
	int t;
	string s;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> s;
		vector<bool>* vec = new vector<bool>();

		for(string::iterator it = s.begin(); it != s.end(); it++) {
			if(*it == '+')
				vec->push_back(true);
			else
				vec->push_back(false);
		}

		cout << "Case #" << (i + 1) << ": " << solve(vec) << endl;

		delete vec;
	}

	return EXIT_SUCCESS;
}
