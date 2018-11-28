#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <bitset>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <fstream>
//#include <tuple>
#include <set>
#include <functional> 
#include <string.h>
#include <time.h>

#define X first
#define Y second
#define MP make_pair
//#define MT make_tuple
#define FOR(i, n) for(int (i) = 0; (i) < (n); (i)++)
#define REP(i, a, n) for(int (i) = (a); (i) < (n); (i)++)
typedef long long ll;
typedef std::pair<int, int> pii;
typedef std::pair<ll, ll > pll;
using namespace std;
const int MAX = 101;
const double PI = 3.1415926535897932384;

template<class T, class U>
void convert(T &t, U &u){
	stringstream ss;
	ss << t;
	ss >> u;
}

int main(){
	int t; cin >> t;
	FOR(i, t){
		map<int, int> tb;
		int first[4][4] = {}, second[4][4] = {};
		
		int n; cin >> n;
		FOR(j, 4) FOR(k, 4){
			int s; cin >> s;
			first[j][k] = s;
		}

		int m; cin >> m;
		FOR(j, 4) FOR(k, 4){
			int s; cin >> s;
			second[j][k] = s;
		}

		FOR(j, 4){
			tb[first[n - 1][j]]++;
			tb[second[m - 1][j]]++;
		}

		vector<int> ans;
		for (auto j: tb){
			if (j.second >= 2) ans.push_back(j.first);
		}

		cout << "Case #" << i + 1 << ":" << " ";
		if (ans.size() == 1) 
			cout << ans[0];
		else if (ans.size() == 0)
			cout << "Volunteer cheated!";
		else 
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}