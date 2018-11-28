#include<iostream>
#include<cstdio>

using namespace std;

#define FOR1(i, n) for (int i=1; i<=n; ++i)
#define FOR0(i, n) for (int i=0; i<n; ++i)

double testcase(){
  double c, f, x;
  cin >> c >> f >> x;
  double rate = 2, duration = 0;
  while (true){
    if (x / rate < (c / rate + x / (rate + f)))
      return duration + x / rate;
    else {
      duration += c / rate;
      rate += f;
    }
  }
}

int main(){
  int ntc;
  cin >> ntc;
  FOR1(tc, ntc){
    printf("Case #%d: %.7lf\n", tc, testcase());
  }
}
