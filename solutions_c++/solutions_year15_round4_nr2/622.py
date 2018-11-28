#include <algorithm>
typedef long long ll;

#include <cstdlib>
#include <cmath>
#include <queue>

#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }
inline double getDouble(){
  double s;
  scanf("%lf", &s);
  return s;
}

#include <set>

using namespace std;

struct data{
  double v;
  double r;
  double a;

  data(double v, double r) : v(v), r(r), a(v * r > 0 ? v * r : - v * r){}
  data(){}
};

bool operator < (const data &lhs, const data &rhs){
  return lhs.a < rhs.a;
}

int main(){
  const int T = getInt();

  REP(t,T){
    const int n = getInt();
    vector<double> v(n);
    vector<double> r(n);

    const double x = getDouble();
    const double c = getDouble();

    vector<data> pvr;
    vector<data> nvr;
    vector<data> zvr;

    REP(i,n){
      v[i] = getDouble();
      r[i] = getDouble() - c;
      const double a = v[i] * r[i];
      if(a == 0) zvr.push_back(data(v[i], r[i]));
      else if(a > 0) pvr.push_back(data(v[i], r[i]));
      else nvr.push_back(data(v[i], r[i]));
    }

    printf("Case #%d: ", t + 1);
    if(zvr.size() == 0 && (pvr.size() == 0 || nvr.size() == 0)){
      puts("IMPOSSIBLE");
    }else{
      double ans = 0;

      double pvrs = 0;
      double nvrs = 0;
      double pvs = 0;
      double nvs = 0;
      double prs = 0;
      double nrs = 0;
      double vrs = 0;

      double vs = 0;

      for(const auto d : pvr){ pvrs += d.a; pvs += d.v; prs += d.r; }
      for(const auto d : nvr){ nvrs += d.a; nvs += d.v; nrs += d.r; }
      for(const auto d : v) vs += d;

      if(pvrs < nvrs){
	swap(pvrs, nvrs);
	swap(prs, nrs);
	swap(pvs, nvs);
      }

      vrs = pvrs - nvrs;

      double low = 0;
      double high = x / vs;
      REP(i,1000){
	double med = (low + high) / 2;
	const double amount = vs * med;
	const double rest = x - amount;
	const double restT = rest / (vs - pvs);
	ans = med + restT;

	double t = 0;
	t += vrs * med;
	t -= nvrs * restT;

	if(t > 0) high = med;
	else low = med;
      }

      printf("%.10f\n", ans);
    }
  }

  return 0;
}











