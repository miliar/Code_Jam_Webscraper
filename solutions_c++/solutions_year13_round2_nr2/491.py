/*
ID: oooctav1
PROG: checker
LANG: C++
*/
#include <iostream> 
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <stack>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>

using namespace std;
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define mp make_pair
#define pb push_back


double count(pair<int,int> p, pair<int,int> q, int n, int x, int y, bool has) {
	if (n == 0) {
		return has ? 1.0:0.0;
	}

	if (p == q) {
		if (p.first != 0) cout << "ASDSADASD " << endl;

		bool h = has;
		if (mp(x,y) == p) h = true;
		return count(mp(p.second +2, 0),mp(-p.second-2,0),n-1,x,y, h);
	}


	bool h1 = has, h2 = has;
	if (mp(x,y) == p) h1 = true;
	if (mp(x,y) == q) h2 = true;

//	h1 = true; h2 = true;


	if (p.first == 0) {
		return count(p,mp(q.first+1, q.second+1),n-1,x,y, h2);
	}
	if (q.first == 0){
		return count(mp(p.first -1, p.second +1),q,n-1,x,y, h1);
	} 

	double rez = 0;
	rez += 0.5 * count(p,mp(q.first+1, q.second+1),n-1,x,y, h2);
	rez += 0.5 * count(mp(p.first -1, p.second +1),q,n-1,x,y, h1);

	return rez ;
} 

int main() {
//	freopen ("checker.out","w",stdout);
//	freopen ("checker.in","r",stdin);

/*
	int t;cin >> t;string ss;getline(cin, ss);
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": " << nrmax << endl; 
	}
*/


//	ios_base::sync_with_stdio(false);

	int ttt;cin >> ttt;string ss;getline(cin, ss);

	for (int tt = 1; tt <= ttt; tt++) {

		int n ,x,y; cin >> n >> x >> y;
		if (x == 0 && y == 0) {
			cout << "Case #" << tt << ": 1.0" << endl; 
			continue;
		}
		n--;

		double rez = count(mp(2,0), mp(-2,0), n , x , y, false);

		cout << "Case #" << tt << ": ";
		printf("%.7lf\n", rez); 
	}

	return 0;
}

