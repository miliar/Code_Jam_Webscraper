//be name oo
#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <sstream>
#include <set>
#include <complex>
#include <iomanip>
#include <queue>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define show(x) cerr << "#" << #x << ": " << x << endl
#define F first
#define S second
#define X real()
#define Y imag()

using namespace std;
typedef pair<int, int> pii;
typedef complex<double> point;

const int MAX_N = 200 + 10;
const int MAX_S = (1 << 20) + 10;

int n;
vector<int> initial;
vector<int> list[MAX_N];
int type[MAX_N];

vector<int> dp[MAX_S];

vector<int> solve(int mask){

	if(SZ(dp[mask]))
		return dp[mask];

	vector<int>& ret = dp[mask];

	if(mask == (1 << n) - 1){
		ret.PB(n);
		return ret;
	}

	multiset<int> have;
	have.insert(initial.begin(), initial.end());
	FOR(i, n)
		if(mask & (1 << i))
			have.insert(list[i].begin(), list[i].end());
	FOR(i, n)
		if(mask & (1 << i))
			have.erase(have.find(type[i]));

	FOR(i, n)
		if(!(mask & (1 << i)) && have.find(type[i]) != have.end()){
			vector<int> res = solve(mask + (1 << i));
			if(res[0] != -1){
				ret.PB(i);
				FOR(j, SZ(res))
					ret.PB(res[j]);
				return ret;
			}
		}
	ret.PB(-1);
	return ret;
}

int main(){
	int testCount;
	cin >> testCount;
	for(int testNumber = 1; testNumber <= testCount; testNumber++){
		cout << "Case #" << testNumber << ":";

		initial.clear();
		int k;
		cin >> k >> n;
		FOR(i, k){
			int a;
			cin >> a;
			initial.PB(a);
		}

		FOR(i, n){
			list[i].clear();
			int k;
			cin >> type[i] >> k;
			FOR(j, k){
				int a;
				cin >> a;
				list[i].PB(a);
			} 
		}

		FOR(i, MAX_S)
			dp[i].clear();

		vector<int> ans = solve(0);
		if(ans[0] == -1)
			cout << " IMPOSSIBLE" << endl;
		else{
			FOR(i, n)
				cout << " " << (ans[i] + 1);
			cout << endl;
		}
	}
	return 0;
}

