#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
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

ll solve(ll n, ll top) {
  ll k = 0;
  ll sum = 0;
  ll nn = 1 << (n-1);
  while (top > 0) {
    top -= nn;
    nn /= 2;
    sum += 1 << k;
    k++;
  }
  return sum - 1;
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
                ll n, p;
                fin >> n >> p;
                if (p == (1 << n)) {
                  fout << "Case #" << tind << ": " << p-1 << ' ' << p-1 << endl;
                } else {
                  fout << "Case #" << tind << ": "
                       << solve(n, p) << ' '
                       << (1<<n)-2-solve(n, (1<<n)-p) << endl;
                }
	}
	return 0;
}
