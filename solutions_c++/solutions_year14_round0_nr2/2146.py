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

// boost library link
// http://www.boost.org

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

double times = 1.0e10;

unsigned long long convert_ull( string number ) {
	unsigned long long number_ull = 0;
	unsigned long long times_ = times;
	int point_pos = number.find('.');
	FOR(i, 0, point_pos-1) {
		times_ *= 10;
	}
	FOR(i, 0, number.size()) {
		if( i == point_pos ) { continue; }
		number_ull += ( number[i]-'0' ) * times_;
		times_ /= 10;
	}

	return number_ull;
}

string convert_str( unsigned long long number ) {
	ss sstmp;
	sstmp << number;
	int ndigit = sstmp.str().size();
	//cout << ndigit << endl;

	string number_str;
	FOR(i, 0, ndigit) {
		if( i == ndigit - 10 ) {
			if( i == 0 ) {
				number_str += "0";
				number_str += ".";
			} else {
				number_str += ".";
			}
		}
		number_str += sstmp.str()[i];

	}
	//cout << number_str << endl;
	return number_str;
}

int main(int argc, char *args[]) {
	std::ifstream fin;
	std::ofstream fout;
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        fin.open("B-small-attempt4.in");
        fout.open("B-small-attempt4.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
    	fin.open("B-large-attempt0.in");
    	fout.open("B-large-attempt0.out");
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
    unsigned long long C, F, X;

    FOR(n, 0, N) {
    	ss sstmp;
    	string stmp;
    	getline( fin, line );
    	sstmp << line;
    	sstmp >> stmp; C = convert_ull(stmp);
    	sstmp >> stmp; F = convert_ull(stmp);
    	sstmp >> stmp; X = convert_ull(stmp);
    	//cout << C << " " << F << " " << X << endl;
    	unsigned long long min_time = X / 2;
    	string min_time_str;
    	if( X <= 2 * times ) {
    		min_time_str = convert_str( min_time );
    	    results.push_back( min_time_str );
    	    continue;
    	}
    	/*
    	int max_case = ceil( (X - 2 * times) / F );
    	cout << max_case << endl;
    	*/
    	unsigned long long time;
    	int i = 1;
    	while(1) {
    	//FOR(i, 1, max_case+1) {
    		time = 0;
    		FOR(j, 0, i) {
    			time += C * times / (2 * times + F*j);
    		}
    		time += X * times / (2 * times + F*i);
    		min_time = min( min_time, time );
    		if( min_time != time ) { break; }
    		i++;
    	}
    	min_time_str = convert_str( min_time );
    	results.push_back( min_time_str );
    }


    FOR(n,0,N) {
        fout << "Case #" << n+1 << ": ";
        fout << fixed << setprecision(7) << results[n];
        fout << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
