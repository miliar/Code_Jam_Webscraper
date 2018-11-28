#include <functional>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <iterator>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <list>
#include <cassert>
#include <sstream>

using namespace std;

#define SWAP(a,b) do{auto k=a; a=b; b=k;}while(0)
#define inf 987654321
#define infl 10000000000000000000ll
#define REP(k,a,b) for(auto k=(a); k < (b); ++k)
#define PER(k,a,b) for(auto k=(b-1); k >= (a); k--)
#define SUM(v) accumulate(v.begin(), v.end(), 0)
#define PROD(v) accumulate(v.begin(), v.end(), 1, multiplies<long long>())
#define MAX(v) max_element(v.begin(), v.end())
#define MIN(v) min_element(v.begin(), v.end())
typedef long long LL;
typedef vector<long long> VI;

LL POS(LL x) { if (x>0)  return x; else return 0; }

struct ele {
	long double z, y, x;
	ele() {}
	ele(long double z, long double y, long double x) : z(z), y(y), x(x) {}
	ele operator + (const ele &p) const { return ele(z + p.z, y + p.y, x + p.x); }
	ele operator - (const ele &p)  const { return ele(z - p.z, y - p.y, x - p.x); }
	ele operator * (long double con)     const { return ele(z*con, y*con, x*con); }
	ele operator / (long double con)     const { return ele(z / con, y / con, x / con); }
	bool operator<(const ele &rhs) const { return make_pair(z, make_pair(y, x)) < make_pair(rhs.z, make_pair(rhs.y, rhs.x)); }
	bool operator==(const ele &rhs) const { return make_pair(z, make_pair(y, x)) == make_pair(rhs.z, make_pair(rhs.y, rhs.x)); }
};
vector<string> v;
int si;
vector<bool> occ;
vector<bool> allo;
int find(int curr, int cnt, vector<bool> occ, vector<bool> allo){
	for (int i = 0; i < v[curr].size()-1; i++){
		if (occ[v[curr][i]]){
		//	cout << curr << " ";
			return 0;
		}
		if (v[curr][i] != v[curr][i + 1]){
			occ[v[curr][i]] = 1;
		}
	}
	if (occ[v[curr][v[curr].size() - 1]]){
	//	cout << "h" << curr << " ";
		return 0;
	}
	if (cnt == si-1){
	//	cout << curr << " ";
		return 1;
	}
	int ans = 0;
	for (int i = 0; i < si; i++){
		if (!allo[i]){
			if (v[i][0] != v[curr][v[curr].size() - 1]){
				occ[v[curr][v[curr].size() - 1]] = 1;
			}
			else {
				occ[v[curr][v[curr].size() - 1]] = 0;
			}
			allo[i] = 1;
			ans += find(i, cnt + 1, occ, allo);
		//	cout << ans << endl;
			allo[i] = 0;
		}
	}
	return ans;
}
int main()
{
	long long n, m;
	int t;
	cin >> t;
	for (int x = 1; x <= t; x++){
		cout << "Case #" << x << ": ";
		cin >> n;
		vector<string> vs(n);
		for (int i = 0; i < n; i++){
			cin >> vs[i];
		}
		v = vs;
		si = vs.size();
		int ans = 0;
		for (int i = 0; i < n; i++){
			allo = vector<bool>(n, 0);
			occ = vector<bool>(150, 0);
			allo[i] = 1;
			ans += find(i, 0, occ, allo);
			allo[i] = 0;
	//		cout << ans << endl;
		}
		cout << ans << endl;
	}
	return 0;
}