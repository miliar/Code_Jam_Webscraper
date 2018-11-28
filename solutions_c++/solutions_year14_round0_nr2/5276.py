#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iomanip>
using namespace std;

#define rep(i,m,n) for(int i = m; i < n; i++)
#define bitrep(S, m, n) for(int S = m; S < (1 << n); S++)
#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())
#define x first
#define y second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int, int> PII;


int main(){
  int loop;
  double c, f, x;
  ifstream ifs("B-large.in");
  ofstream ofs("ans.txt");
  ifs >> loop;
  rep(l, 1, loop+1){
    ifs >> c >> f >> x;
    double ans = 0.0, cookie = 0.0;
    double rate = 2.0;
    while(cookie < x){
      ans += c / rate;
      if((x - c)/rate >= x / (rate+f)){
	rate += f;
	cookie = 0.0;
      }else{
	ans += (x-c)/rate;
	cookie = x;
      }
    }
    ofs.setf(std::ios_base::fixed,std::ios_base::floatfield);
    ofs << setprecision(7) << "Case #" << l << ": " << ans;
    ofs << endl;
  }
  return 0;
}
