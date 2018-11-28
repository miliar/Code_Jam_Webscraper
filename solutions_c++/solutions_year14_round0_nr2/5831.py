#include <iostream>
#include <iomanip>
using namespace std;

void solve(double c, double f, double x);

int main(){
 int n;
 cin >> n;
 cout << std::setprecision(7) << std::fixed;
 for (int i = 1; i <= n; ++i){
  double c, f, x;
  cin >> c >> f >> x;
  cout << "Case #" << i << ": ";
  solve(c, f, x);
 }
}

void solve(double c, double f, double x){
 double last = 0.0;
 double next = x/2.0;
 double cur_rate = 2.0;
 double total = 0.0;
 do {
  last = next;
  total += c/cur_rate;
  cur_rate += f;
  next = x/cur_rate;
  next += total;
 } while (last >= next);
 cout << last << endl;
}
