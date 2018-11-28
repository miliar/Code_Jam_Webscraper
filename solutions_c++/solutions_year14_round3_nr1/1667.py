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
	for (int x = 1; x <= t; x++){
		cout << "Case #" << x << ": ";
		cin >> n;
		char a;
		cin >> a;
		cin >> m;
		long long mm = m;
		int c = 0;
		for (int i = 2; i < sqrt(mm); i++){
			if (i%n == 0 && i%m == 0){
				m /= i;
				n /= i;
				i--;
			}
		}
		if (m%n == 0){
			m /= n;
			n = 1;
		}
		mm = m;
		while(mm%2 == 0){
			c++;
			mm /= 2;
		}
	//	cout << mm << endl;
		if (mm > 1){
			cout << "impossible" << endl;
			continue;
		}
		long double aa = 1;
		c = 0;
		long double bb = (long double)n / m;
		while (aa > bb){
			c++;
			aa /= 2;
		}
		cout << c << endl;
	}
	return 0;
}