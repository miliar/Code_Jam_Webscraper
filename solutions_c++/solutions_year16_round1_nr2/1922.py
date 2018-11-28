#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;

string solve(vector<vector<int> > soldiers)
{
	map<int, int> counts;
	for( uint i = 0; i < soldiers.size(); i++ ) {
		for( uint j = 0; j < soldiers[i].size(); j++ ) {
			if( counts.count(soldiers[i][j]) == 0 ) {
				counts.insert( map<int, int>::value_type(soldiers[i][j], 1) );
			} else {
				counts[soldiers[i][j]]++;
			}
		}
	}
	map<int, int>::iterator it;
	vector<int> shortage_soldiers;
	for( it = counts.begin(); it != counts.end(); it++ ) {
		if( (*it).second % 2 == 1 ) {
			shortage_soldiers.push_back((*it).first);
		}
	}
	assert( shortage_soldiers.size() == soldiers[0].size() );
	std::sort( shortage_soldiers.begin(), shortage_soldiers.end() );
	std::stringstream ss;
	for(int i = 0; i < shortage_soldiers.size(); i++ ) {
		if( i == shortage_soldiers.size() - 1) {
			ss << shortage_soldiers[i];
		} else {
			ss << shortage_soldiers[i] << " ";
		}
	}
	return ss.str();
}

int main(int argc, char *argv[]) {

    int T, N;

    ifstream ifs(argv[1]);
    ofstream ofs(argv[2]);

    string line;
    std::getline(ifs, line);
    T = stoi(line);

    for( int i = 1; i <= T; i++ ) {
    	std::getline(ifs, line);
    	stringstream ss(line);
    	ss >> N;
    	vector<vector< int > > soldiers;
    	for( int j = 0; j < 2 * N - 1; j++ ) {
    		soldiers.push_back( vector<int>() );
    		std::getline(ifs, line);
    		ss.clear(); ss.str(""); ss << line;
    		for( int k = 0; k < N; k++ ) {
    			int s;
    			ss >> s;
    			soldiers[j].push_back(s);
    		}
    	}
    	for( uint j = 0; j < soldiers.size(); j++ ) {
    		for( uint k = 0; k < soldiers[j].size(); k++ ) {
    			cout << soldiers[j][k] << " ";
    		}
    		cout << endl;
    	}
    	ofs << "Case #" << i << ": " << solve(soldiers) << endl;
    }

    ifs.close();
    ofs.close();

    return 0;
}







