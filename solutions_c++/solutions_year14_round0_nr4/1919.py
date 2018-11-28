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

int nwin_war( vector<double> Naomi, vector<double> Ken ) {
	int nwin = 0;
	FOR(i, 0, Naomi.size()) {
		double NaomiWeight = Naomi[i];
		double KenWeight = -1.0;
		vector<double>::iterator itKen = Ken.begin();
		while( itKen != Ken.end() ) {
			if( (*itKen) > NaomiWeight ) {
				KenWeight = (*itKen);
				Ken.erase(itKen);
				break;
			}
			itKen++;
		}
		if( KenWeight < 0 ) {
			Ken.erase(Ken.begin());
			nwin++;
		}
	}
	return nwin;
}

int nwin_deceitful_war( vector<double> Naomi, vector<double> Ken ) {
	int nwin_max = 0;
	int max_deceit = 0;
	int nbattle = Naomi.size();
	FOR(i, 0, nbattle) {
		if(Naomi[i] < Ken[Ken.size()-i-1]) max_deceit++;
	}

	FOR(n, 0, max_deceit+1) {
		int nwin = 0;
		vector<double> Naomi_copy = Naomi;
		vector<double> Ken_copy = Ken;
		if( n != 0 ) {
			FOR(i, 0, n) {
				Naomi_copy.erase(Naomi_copy.begin());
				Ken_copy.erase(Ken_copy.end()-1);
			}
		}
		FOR(i, 0, Naomi_copy.size()) {
			if( Naomi_copy[ Naomi_copy.size() - i - 1] > Ken_copy[ Ken_copy.size() - i - 1] ) nwin++;
		}
		nwin_max = max( nwin, nwin_max );
	}

	return nwin_max;
}

int main(int argc, char *args[]) {
	std::ifstream fin;
	std::ofstream fout;
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        fin.open("D-small-attempt0.in");
        fout.open("D-small-attempt0.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
    	fin.open("D-large.in");
    	fout.open("D-large.out");
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
    vector<int> results;
    vector<int> results_deceitful;
    results.resize(N);
    results_deceitful.resize(N);

    FOR(n, 0, N) {
    	vector<double> Naomi;
    	vector<double> Ken;
    	ss sstmp;
    	string stmp;
    	getline(fin, line);
    	int num_war = stoi(line);
    	// Naomi‚ÌŽè‚ð“¾‚é
    	getline(fin, line);
    	sstmp.str(""); sstmp.clear();
    	sstmp << line;
    	FOR(i, 0, num_war) {
    		sstmp >> stmp;
    		Naomi.push_back(stof(stmp));
    	}
    	// Ken‚ÌŽè‚ð“¾‚é
    	getline(fin, line);
    	sstmp.str(""); sstmp.clear();
    	sstmp << line;
    	FOR(i, 0, num_war) {
    	    sstmp >> stmp;
    	    Ken.push_back(stof(stmp));
    	}
    	sort( Naomi.begin(), Naomi.end() );
    	sort( Ken.begin(), Ken.end() );

    	results[n] = nwin_war(Naomi, Ken);
    	if( Naomi.size() == 1 ) {
    		results_deceitful[n] = results[n];
    	} else {
    		results_deceitful[n] = nwin_deceitful_war(Naomi, Ken);
    	}
    	/*
    	FOR(i, 0, num_war) {
    		cout << Naomi[i] << " " << Ken[i] << ":";
    	}
    	cout << endl;
    	*/
    }

    FOR(n,0,N) {
        fout << "Case #" << n+1 << ": ";
        fout << results_deceitful[n] << " " << results[n];
        fout << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
