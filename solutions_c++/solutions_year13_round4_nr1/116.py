#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

const ll MM = 1000002013;
ll n, m;
vector<int> s;
vector<long long> f;
map<int, int> rs;

ll save(ll dis) {
  return dis * (dis - 1) / 2 % MM;
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		int i,j;
		//istringstream strin();
                fin >> n >> m;
                int o[1010], e[1010], p[1010];
                vector<int> a;
                for (i = 0; i < m; ++i) {
                  fin >> o[i] >> e[i] >> p[i];
                  a.push_back(o[i]);
                  a.push_back(e[i]);
                }
                sort(a.begin(), a.end());
                s.clear();
                rs.clear();
                f.clear();
                for (i = 0; i < a.size(); ++i)
                  if (i == 0 || a[i] > a[i-1]) {
                    s.push_back(a[i]);
                    f.push_back(0);
                    rs[a[i]] = s.size() - 1;
                  }
		ll ans = 0;
                for (i = 0; i < m; ++i) {
                  int r1 = rs[o[i]];
                  int r2 = rs[e[i]];
                  for (j = r1; j < r2; ++j) f[j] += p[i];
                  ans = ((save(e[i] - o[i]) * p[i] % MM) + ans) % MM;
                }
                ans = (MM - ans) % MM;
                i = 0;
                while (i < f.size()) {
                  while (i < f.size() && f[i] == 0) i++;
                  if (i >= f.size()) break;
                  ll mp = f[i];
                  j = i;
                  while (j < f.size() && f[j] > 0) {
                    if (f[j] < mp) mp = f[j];
                    j++;
                  }
                  ans = ((save(s[j] - s[i]) * (mp%MM) % MM) + ans) % MM;
                  for (int k = i; k < j; ++k) f[k] -= mp;
                }
		fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
