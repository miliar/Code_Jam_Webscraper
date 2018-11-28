#include <functional>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cctype>
#include <ctime>
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
#include <limits>
#include <cassert>
#include <sstream>

using namespace std;

//#define SWAP(a,b) do{ll k=a; a=b; b=k;}while(0)
#define inf 987654321
#define infl 1000000000000000000ll
#define rep(k,a,b) for(ll k=(a); k < (b); ++k)
#define repi(i, a) for(auto i = (a).begin(), _##i = (a).end(); i != _##i; ++i)
#define per(k,a,b) for(ll k=(a-1); k >= (b); k--)
#define SUM(v) accumulate(v.begin(), v.end(), 0)
#define PROD(v) accumulate(v.begin(), v.end(), 1, multiplies<long long>())
#define MAX(v) max_element(v.begin(), v.end())
#define MIN(v) min_element(v.begin(), v.end())
#define trailval(x) (x & ~(x - 1))
#define ispo2(x) ((x - trailval(x)) == 0 ? 1 : 0)
#define clbit(x,b) (x &= ~(1 << b))
#define stbit(x,b) (x |= 1 << b)
#define tsbit(x,b) (( (x & 1 << b) != 0) ? 1:0)
typedef long long ll;
typedef vector<long long> VI;
typedef vector<vector<ll> >VV;
typedef vector<string> VS;
typedef vector<list<ll> > VL;

ll POS(ll x) { if (x > 0)  return x; else return 0; }

int ones(int n) { return n ? 1 + ones(n & (n - 1)) : 0; }

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

template < class T >
inline ostream& operator << (ostream& os, const vector<T>& v){
	for (vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
		os << *ii << " ";
	os << '\b';
	return os;
}

template < class T >
inline istream& operator>> (istream& os, vector<T>& v){
	for (vector<T>::iterator ii = v.begin(); ii != v.end(); ++ii)
		os >> (*ii);
	return os;
}
#define all(vtr) (vtr).begin(),(vtr).end()
int func(int no_of_elements,vector<double> naomi,vector<double>ken){
	int j = 0;
	int cnt = 0;
	rep(i, 0, no_of_elements){
		for (j; j < no_of_elements; j++){
			if (naomi[i] < ken[j]){
				cnt++;
				j++;
				break;
			}
		}
	}
	return cnt;
}
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t;i++){
		int no_of_elements;
		cin >> no_of_elements;
		vector<double> naomi, ken;
		double p;
		for (int i = 0; i < no_of_elements; i++){
			cin >> p;
			naomi.push_back(p);
		}
		for (int i = 0; i < no_of_elements; i++){
			cin >> p;
			ken.push_back(p);
		}
		stable_sort(all(naomi));
		stable_sort(all(ken));
		int val1 = no_of_elements-func(no_of_elements,naomi,ken);
		int val2 = func(no_of_elements, ken, naomi);
		cout << "Case #" << i << ": " << val2 << " " << val1 << endl;
	}
	return 0;
}