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
#define FOR(i,s,e) for (int i = int(s); i != int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int I, J;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

int N;
int main(int argc, char *args[]) {
	std::ifstream fin;
	std::ofstream fout;
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        fin.open("A-small-attempt1.in");
        fout.open("A-small-attempt1.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
    	fin.open("A-large-practice.in");
    	fout.open("A-large-practice.out");
    }
    else if (argc == 2 && strcmp(args[1], "test") == 0) {
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

    unsigned int count[16];

    FOR(n, 0, N) {
    	vector<unsigned int> card_count_two;
    	memset( count, 0, 16 * sizeof(unsigned int) );
    	FOR(i, 0, 2) {
    		int select_line;
    		getline( fin, line );
    		select_line = stoi(line);
    		FOR( r, 0, 4 ) {
    			getline( fin, line );
    			if( r == select_line - 1 ) {
					ss cards_in_line;
					cards_in_line << line;
					FOR( c, 0, 4) {
						unsigned int number;
						cards_in_line >> number;
						count[number-1]++;
					}
    			}
    		}
    	}
    	FOR( i, 0, 16 ) {
    	    if( count[i] == 2 ) {
    	    	card_count_two.pb( i+1 );
    	    }
    	}

    	switch( card_count_two.size() ) {
    	    case 0:
    	    	results.pb("Volunteer cheated!");
    	    	//cout << "Volunteer cheated!" << endl;
    	    	break;
    	    case 1:
    	    {
    	    	ss selectcard;
    	    	selectcard << card_count_two.front();
    	    	results.pb(selectcard.str());
    	    	//cout << selectcard.str() << endl;
    	    	break;
    	    }
    	    default:
    	    	results.pb("Bad magician!");
    	    	//cout << "Bad magician!" << endl;
    	    	break;
    	}

    }

    FOR(n,0,N) {
        fout << "Case #" << n+1 << ": ";
        fout << results[n];
        fout << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
