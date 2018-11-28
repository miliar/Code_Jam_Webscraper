
//IamAwesome
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <iterator>
#include <set>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <list>
#include <sstream>
#include <ctype.h>
#include <utility>
#include <cstdlib>
#include <functional>
#include <numeric>
#include <iomanip>


using namespace std;

#define LL long long
#define linf 998877665544332211ll
#define inf 987654321ll
#define MOD 1000000007ll
#define ADD(v) accumulate(v.begin(),v.end(), 0)
#define PRO(v) accumulate(v.begin(),v.end(), 1,multiplies <int>())
LL POS(LL x) { if (x > 0)  return x; else return 0; }
#define maxe(v) max_element(v.begin(),v.end())
#define mine(v) min_element(v.begin(),v.end())
#define rep(k,a,b) for(int k=(a); k < (b); ++k)
#define per(k,a,b) for(int k=(b-1); k >= (a); --k)
#define repg(k,ctnr) for(auto k=ctnr.begin();k!=ctnr.end();k++)
#define all(ctnr) (ctnr).begin(),(ctnr).end()

struct ysh {
	long long z, y, x;
	ysh() {}
	ysh(long long z, long long y, long long x) : z(z), y(y), x(x) {}
	ysh operator + (const ysh &p) const { return ysh(z + p.z, y + p.y, x + p.x); }
	ysh operator - (const ysh &p)  const { return ysh(z - p.z, y - p.y, x - p.x); }
	ysh operator * (long long con)     const { return ysh(z*con, y*con, x*con); }
	ysh operator / (long long con)     const { return ysh(z / con, y / con, x / con); }
	bool operator<(const ysh &rhs) const { return make_pair(z, make_pair(y, x)) < make_pair(rhs.z, make_pair(rhs.y, rhs.x)); }
	bool operator==(const ysh &rhs) const { return make_pair(z, make_pair(y, x)) == make_pair(rhs.z, make_pair(rhs.y, rhs.x)); }
};
int dx[] = { 1, 0, -1, 0, 1, 1, -1, -1 };
int dy[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

vector<long  double> dp(1000000, -1);
long double find(long double c, long double f, long double tr,long double i){
	long double ans = tr / i, tmp = c / i;
	//if (dp[i]>=0)return dp[i];
	if (ans < 1)
		return ans;
	ans=min(ans, tmp + find(c, f, tr, i+f));
	dp[i] = ans;
	return ans;
}
int main() {
	LL n, m, l;
	int t;
	cin >> t;
	long double i;
	int x = 1;
	long double t_taken = 0;
	long double c, f, tr;
	while (t--){
		t_taken = 0;
		cin >> c >> f >> tr;
	/*	dp = vector<long double>(1000000, -1.0);
		find(c, f, tr, 2);
		cout << "Case #" << x << ": ";
		printf("%0.7llf", find(c, f, tr, 2));
		cout << endl;*/
		/*for (i = 2; (tr / i) > t_taken + ((c / i) + (tr / (i + f))); i += f){
			t_taken = t_taken + (c / i);
		}
		t_taken += tr / i;*/
		long double t1=0,t2=0;
		i = 2;
		for (i = 2, t1 = 0, t2 = 0;; i += f){
			t1 =t2+(tr / i);
			t2 += (c / i);
			if (t1 <= t2+(tr/(i+f))){
				t_taken += tr / i;
				cout << "Case #" << x << ": ";
				printf("%0.7llf", t_taken);
				cout << endl;
				break;
			}
			t_taken += c / i;
		}
		x++;
	}

	return 0;
}