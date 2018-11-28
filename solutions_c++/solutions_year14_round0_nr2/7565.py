#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

int main()
{
  double C, F, X;
  double f[100010];
  int t;
  cin >> t;
  for(int k=1; k<=t; k++){
    cin >> C >> F >> X;
    for(int i=0; i<100010; i++)
      f[i] = C*1.0/(2 + i*F);
    for(int i=1; i<100010; i++)
      f[i] += f[i-1];
    for(int i=0; i<100010; i++)
      f[i] += X*1.0/(2+(i+1)*F);
    double ans = (X*1.0)/(2);
    for(int i=0; i<100010; i++)
      ans = min(ans, f[i]);
    cout << "Case #"<< k << ": " << setprecision (7) << fixed << ans << endl;
  }
}
