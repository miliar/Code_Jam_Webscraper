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

int R, C, M;
vector<short> make_zero_region( vector<short> prv, int max, int n) {

	if( n == R ) {
		int num_empty = 0;
		vector<short> res;
		res.resize(R);
		FOR(i, 0, R - 1) {
			if( i == 0 ) {
				if( prv[i] != 0 ) {
					if( prv[i] != C ) {
						num_empty += ( prv[i] + 1 ) * 2;
						res[i] = res[i+1] = prv[i] + 1;
					} else {
						num_empty += prv[i] * 2;
						res[i] = res[i+1] = prv[i];
					}
				}
			} else {
				if( prv[i] != 0 ) {
					if( prv[i] != C ) {
						num_empty += prv[i] + 1;
						res[i+1] = prv[i] + 1;
					} else {
						num_empty += prv[i];
						res[i+1] = prv[i];
					}
				}
			}
		}
		if( R * C - num_empty == M ) { cout << "hit!" << endl; return res; }
	} else if( n == 0 ) {
		FOR(i, 0, C + 1) {
			prv[n] = i;
			vector<short> res = make_zero_region( prv, i, n + 1 );
			if(!res.empty()) return res;
		}
	} else {
		FOR(i, 0, max+1) {
			prv[n] = i;
			vector<short> res =  make_zero_region( prv, i, n + 1 );
			if(!res.empty()) return res;
		}
	}

	return vector<short>();
}

int N;
int main(int argc, char *args[]) {
	std::ifstream fin;
	std::ofstream fout;
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        fin.open("C-small-attempt0.in");
        fout.open("C-small-attempt0.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
    	fin.open("A-large-practice.in");
    	fout.open("A-large-practice.out");
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
    vector< vector<string> > board;
    results.resize(N);
    board.resize(N);

    FOR(n, 0, N) {
    	cout << "case #" << n + 1 << endl;
    	ss sstmp;
    	getline( fin, line );
    	sstmp << line;
    	sstmp >> R >> C >> M;
    	board[n].resize(R);
    	// ’n—‹‚ÌŒÂ”‚ªƒ}ƒX–Ú‚Ì”-1‚Ì‚Æ‚«
    	if( M == R * C - 1 ) {
    		FOR(y, 0, R) {
    			string board_line;
    			FOR(x, 0, C) {
    				if( x==0 && y==0 ) board_line += "c";
    				else			   board_line += "*";
    			}
    			board[n][y] = board_line;
    		}
    		results[n] = "Possible";
    	} else if( M == R * C ) {
    		results[n] = "Impossible";
    	} else if( R == 1 ){
    		results[n] = "Possible";
    		string board_line;
    		FOR(x, 0, C) {
    			if( x == 0 )		  board_line += "c";
    			else if( x >= C - M ) board_line += "*";
    			else				  board_line += ".";
    		}
    		board[n][0] = board_line;
    	} else if( C == 1 ){
    		results[n] = "Possible";
    		FOR(y, 0, R) {
    			string board_line;
    			if( y == 0 )		  board_line += "c";
    			else if( y >= R - M ) board_line += "*";
    			else				  board_line += ".";
    			board[n][y] = board_line;
    		}
    	} else {
    		vector<short> empty;
    		empty.resize(R);
    		empty = make_zero_region( empty, 0, 0 );
    		if( !empty.empty() ){
    			results[n] = "Possible";
    			FOR(y, 0, R) {
    			    string board_line;
    			    FOR(x, 0, C) {
    			    	if( x==0 && y==0 )	 	 board_line += "c";
    			    	else if( x >= empty[y] ) board_line += "*";
    			    	else					 board_line += ".";
    			    }
    			    board[n][y] = board_line;
    			}
    		} else {
    			results[n] = "Impossible";
    		}
    	}

    }

    FOR(n,0,N) {
        fout << "Case #" << n+1 << ":" << endl;
        if( results[n] == "Impossible" ) {
        	fout << "Impossible" << endl;
        } else {
        	FOR(y, 0, board[n].size()) {
        		fout << board[n][y] << endl;
        	}
        }
    }

    fin.close();
    fout.close();
    return 0;
}
