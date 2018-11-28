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

int main()
{
	long long n, m;
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++){
		cout << "Case #" << tc << ": ";
		set<int> sett;
		cin >> n;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> m;
				if (i == n-1){
					sett.insert(m);
				}
			}
		}
		cin >> n;
		int ans = 0;
		int a;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> m;
				if (i == n - 1){
					ans += sett.count(m);
					if (sett.count(m)>0)
					a = m;
				}
			}
		}
		if (ans > 1){
			cout << "Bad magician!" << endl;
		}
		else {
			if (ans ==0 ){
				cout << "Volunteer cheated!" << endl;
			}
			else{
				cout << a << endl;
			}
		}
	}
	return 0;
}