#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <cctype>

#define FOR(i,n) for(long long int i=0; i<n; i++)
#define MP(a,b) make_pair(a,b)
#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(), a.end())
#define REV(a) reverse(a.begin(), a.end())

#define COND(p,t,f) ((p)?(t):(f))

#define PI 3.14159265

using namespace std;
typedef long long int lint;
typedef unsigned long long int ulint;



int main() {
  int T;
  cin >> T;
  FOR(t,T) {
    int N;
    cin >> N;
    set <double> nao,ken;
    FOR(i,N) {
      double x;
      cin >> x;
      nao.insert(x);
    }
    FOR(i,N) {
      double x;
      cin >> x;
      ken.insert(x);
    }
    int y = 0, z=0;
    set<double> n1(nao), k1(ken);
    FOR(i,N) {
      double n = *(n1.begin());
      double k;
      if (k1.lower_bound(n)!=k1.end()) {
	k = *(k1.lower_bound(n));
      }
      else k = *(k1.begin());
      n1.erase(n);
      k1.erase(k);
      if (n>k) z++;
      
      n = *(nao.begin());
      k = *(ken.begin());
      if (n<k) {
	ken.erase(*(ken.rbegin()));
      }
      else {
	y++;
	ken.erase(k);
      }
      nao.erase(n);
    }
    cout << "Case #" << t+1 << ": " <<y<< " " << z << endl;

  }
  
}