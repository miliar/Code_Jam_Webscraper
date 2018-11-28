#include <cstring>
#include <string.h>
#include <fstream>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,s,e) for (int i = int(s); i < int(e); i++)
#define repit(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair

typedef stringstream ss;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const double PI = 2 * acos(0);
const double eps = 1e-9;

vector<string> cars;
int nsets;
int acount[26];

void connect( vector<string> rescars, string str, ull &count ) {

	if( rescars.empty() ) {
		rep(i, 0, 26) {
			acount[i] = 0;
		}
		rep(i, 0, str.size()) {
			if( i != 0 && acount[ str[i] - 'a'] != 0 && str[i-1] != str[i] ) {
				return;
			}
			acount[ str[i] - 'a']++;
		}
		count++;
		return;
	}

	rep(i, 0, rescars.sz) {
		vector<string> next = rescars;
		next.erase(next.begin() + i);
		connect( next, str + rescars[i], count );
	}

	return;
}


ull getAnswer( int nsets, vector<string> cars ){

	ull ans = 0;
	connect(cars, "", ans);
	return ans;

}

int main(int argc, char *args[]) {

	std::ifstream fin;
	std::ofstream fout;
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        fin.open("B-small-attempt0.in");
        fout.open("B-small-attempt0.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
    	fin.open("B-large.in");
    	fout.open("B-large.out");
    } else if  (argc == 2 && strcmp(args[1], "test") == 0) {
    	fin.open("test.in");
    	fout.open("test.out");
    }
    if(fin.fail()) {
    	cerr << "File do not exist.\n";
    	exit(0);
   	}

    string line;
    getline( fin, line );
    int N = stoi(line);
    vector<ull> results;
    results.resize(N);

    rep(n, 0, N) {
    	cout << "Case #" << n+1 << endl;

    	ss sstmp;
    	string stmp;
    	getline( fin, line );
    	nsets = stoi( line );

    	cars.clear();
    	cars.resize(nsets);
    	getline(fin, line);
    	sstmp << line;
    	rep(i, 0, nsets) {
    		sstmp >> stmp;
    		cars[i] = stmp;
    	}
    	results[n] = getAnswer( nsets, cars );
    }

    rep(n, 0, N) {
        fout << "Case #" << n+1 << ": ";
        fout << results[n];
        fout << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
