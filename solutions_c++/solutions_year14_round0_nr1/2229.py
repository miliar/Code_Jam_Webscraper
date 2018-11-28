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

void Practice() {

	int row_chosen;
	cin >> row_chosen;

	vector<int> first;
	int tmp;
	FOR(i,1,4) {
		FOR(j,1,4) {
			cin >> tmp;
			if (row_chosen == i)
				first.push_back(tmp); //store values to a set
		}
	}

	sort(first.begin(), first.end());

	int row_chosen_second;
	cin >> row_chosen_second;

	vector<int> second;
	FOR(i,1,4) {
		FOR(j,1,4) {
			cin >> tmp;
			if (row_chosen_second == i)
				second.push_back(tmp); //store values to a set
		}
	}

	sort(second.begin(), second.end());

	vector<int> intersection(4);
	vector<int>::iterator it;

	it = set_intersection(first.begin(), first.end(), second.begin(), second.end(),
			intersection.begin());

	intersection.resize(it-intersection.begin());

	if (intersection.size() == 0)
		cout << "Volunteer cheated!" << endl;
	else if (intersection.size() == 1)
		cout << intersection.at(0) << endl;
	else
		cout << "Bad magician!" << endl;

}
