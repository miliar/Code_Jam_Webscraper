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
typedef long double ld;

const double PI = 2 * acos(0);
const double eps = 1e-9;

string getAnswer( int n, vector<string> str ) {
	vector< string > order;
	vector< vector< int > >  num;
	vector< int > center;

	order.resize(n);
	num.resize(n);

	rep( i, 0, n ) {
		int count = 0;
		rep(j, 0, str[i].size()) {
			if( j == 0 ) {
				order[i] = str[i][j];
				count = 1;
			} else {
				if(str[i][j] != order[i].back()) {
					order[i] += str[i][j];
					num[i].pb(count);
					count = 1;
				} else {
					count++;
				}
			}
		}
		num[i].pb(count);
	}

	rep(i, 0, n) {
		cout << order[i] << " : ";
		rep(j, 0, order[i].sz) {
			cout << num[i][j] << " ";
		}
		cout << endl;
	}

	rep( i, 0, n - 1 ) {
		if( order[i + 1] != order[i] ) {
			return "Fegla Won";
		}
	}

	center.resize( order[0].sz );
	double ave;
	rep(j, 0, order[0].sz) {
		ave = 0.0;
		rep(i, 0, n) {
			ave += num[i][j];
		}
		center[j] = round(ave / n);
	}

	int ans = 0;
	rep(i, 0, n) {
		rep(j, 0, order[0].sz) {
			ans += abs( num[i][j] - center[j] );
		}
	}

	ss sans;
	sans << ans;
	return sans.str();
}

int main(int argc, char *args[]) {

	std::ifstream fin;
	std::ofstream fout;
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        fin.open("A-small-attempt0.in");
        fout.open("A-small-attempt0.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
    	fin.open("A-large.in");
    	fout.open("A-large.out");
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
    vector<string> results;
    results.resize(N);

    rep(n, 0, N) {
    	cout << "Case #" << n+1 << endl;
    	ss ssbuf;
    	string stmp;
    	int nstring;
    	vector< string > str;
    	getline( fin, line );
    	ssbuf << line;
    	ssbuf >> nstring;
    	rep(i, 0, nstring) {
    		getline( fin, line );
    		ssbuf.str(""); ssbuf.clear();
    		ssbuf << line;
    		ssbuf >> stmp;
    		str.pb( stmp );
    	}
    	results[n] = getAnswer( nstring, str );
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
