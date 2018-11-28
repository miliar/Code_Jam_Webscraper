#include<algorithm>
#include<cassert>
#include<complex>
#include<map>
#include<iomanip>
#include<sstream>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define CLR(x) memset((x), 0, sizeof(x))
#define SQR(a) ((a)*(a))
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FORE(it, (x)) cerr <<*it <<", "; cout <<endl; }}
using namespace std;
//typedef long long LL;
//typedef long double LD;
//typedef pair<int, int>P;
//typedef vector<int>VI;
//const int INF=1E9+7;
template<typename T> void mini(T&a4, T b4) {
	a4 = min(a4, b4);
}
template<typename T> void maxi(T&a4, T b4) {
	a4 = max(a4, b4);
}

void Deceitful_War() {
	int N;
	cin >> N;

	double tmp;
	vector<double> Naomi, Ken;
	FOR(i,1,N) {
		cin >> tmp;
		Naomi.push_back(tmp);
	}

	FOR(i,1,N) {
		cin >> tmp;
		Ken.push_back(tmp);
	}

	sort(ALL(Naomi), greater<double>());
	sort(ALL(Ken), greater<double>());

	int best_naomi = 0;
	FOR(i,0,N-1) {
		int tmp = 0;
		FOR(j,0,N-1-i) {
			if (Naomi.at(j) > Ken.at(i + j))
				tmp++;
		}
		if (tmp > best_naomi)
			best_naomi = tmp;
	}

	int best_ken = 0;
	FOR(i,0,N-1) {
		int tmp = 0;
		FOR(j,0,N-1-i) {
			if (Ken.at(j) > Naomi.at(i + j))
				tmp++;
		}
		if (tmp > best_ken)
			best_ken = tmp;
	}

	cout << best_naomi << "\t" << N - best_ken << endl;

}

