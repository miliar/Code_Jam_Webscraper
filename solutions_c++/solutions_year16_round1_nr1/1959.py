#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;

string solve(string S)
{
	vector<char> ans;
	ans.push_back(S[0]);
	for( uint i = 1; i < S.size(); i++ ) {
		if( S[i] >= ans.front() ) {
			ans.insert(ans.begin(), S[i]);
		} else {
			ans.insert(ans.end(), S[i]);
		}
	}
	string word;
	for( uint i = 0; i < ans.size(); i++ ) {
		word += ans[i];
	}
	return word;
}

int main(int argc, char *argv[]) {

    int T;
    string S;

    ifstream ifs(argv[1]);
    ofstream ofs(argv[2]);

    string line;
    std::getline(ifs, line);
    T = stoi(line);

    for( int i = 1; i <= T; i++ ) {
    	std::getline(ifs, line);
    	stringstream ss(line);
    	ss >> S;
    	ofs << "Case #" << i << ": " << solve(S) << endl;;
    }

    return 0;
}





