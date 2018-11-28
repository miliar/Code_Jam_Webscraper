
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

int main() {
	LL n, m, l;
	int t;
	cin >> t;
	int x = 1;
	while (t--){
		int ans1=0, ans2=0;
		int n;
		cin >> n;
		vector<double> vn(n);
		for (int i = 0; i < n; i++){
			cin >> vn[i];
		}
		sort(vn.begin(), vn.end());
		vector<double> vk(n);
		for (int i = 0; i < n; i++){
			cin >> vk[i];
		}
		sort(vk.begin(), vk.end());
		int j=0;
		for (int i = 0; i<n; i++){
			for (j;j<n;j++){
				if (vn[i] < vk[j]){
					//cout << i << " " << j << endl;
					//cout << vn[i] << " " << vk[j] << endl;
					ans2++;
					j++;
					break;
				}
			}
		}
		j = 0;
		for (int i = 0; i<n; i++){
			for (j; j<n; j++){
				if (vk[i] <vn[j]){
					//cout << i << " " << j << endl;
					//cout << vn[i] << " " << vk[j] << endl;
					ans1++;
					j++;
					break;
				}
			}
		}
		cout << "Case #" << x << ": ";
		cout << ans1<<" "<<n-ans2;
		cout << endl;
		x++;
	}

	return 0;
}