#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>
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

int low[1000000];
int high[1000000];
vector<pair<int, int> > a;

int main()
{
  int tcase = 0;
  ifstream fin("z.in");
  ofstream fout("z.out");
  fin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    //istringstream strin();
    int N, D;
    ll s0, as, cs, rs;
    ll m0, am, cm, rm;
    fin >> N >> D;
    fin >> s0 >> as >> cs >> rs;
    fin >> m0 >> am >> cm >> rm;
    low[0] = high[0] = s0;
    ll lastm = m0;
    ll lasts = s0;
    a.clear();
    a.reserve(N * 2);
    for (int i = 1; i < N; i++) {
      ll curm = (lastm * am + cm) % rm;
      lastm = curm;
      curm = curm % i;
      ll curs = (lasts * as + cs) % rs;
      lasts = curs;
      low[i] = high[i] = curs;
      if (low[curm] < low[i]) low[i] = low[curm];
      if (high[curm] > high[i]) high[i] = high[curm];
      //cerr << i << ' ' << curm << ' ' << curs << ' ' << low[i] << ' ' << high[i]
      //     << endl;
      if (high[i] - low[i] > D) continue;
      if (abs(s0 - low[i]) > D) continue;
      if (abs(s0 - high[i]) > D) continue;
      a.push_back(make_pair(high[i] - D, -i));
      a.push_back(make_pair(low[i], i));
      //cerr << i << ' ' << high[i] - D << " in" << endl;
      //cerr << i << ' ' << low[i] << " out" << endl;
    }
    sort(a.begin(), a.end());
    int k = 1;
    int ans = 1;
    for (int i = 0; i < a.size(); i++) {
      if (a[i].second < 0) k++;
      if (a[i].second > 0) k--;
      if (k > ans) ans = k;
    }
    fout << "Case #" << tind << ": " << ans << endl;
  }
  return 0;
}
