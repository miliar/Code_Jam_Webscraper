#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

double calc(double r1)
{
  return r1*r1; // *M_PI;
}

int main()
{
  int n;
  double t, r, s, u;

  cin >> n;

  for(int cs = 1; cs <= n; ++cs){
    cin >> r >> t;
    int cnt = 0;
    u = r;
    while((s = t-(calc(r+1)-calc(r))) >= 0){
      // cout << "calc1: " << calc(r+u) << endl;  
      // cout << "calc2: " << calc(r) << endl;  
      // cout << s << endl;
      t = s;
      cnt++;
      r += 2;
    }

    cout << "Case #" << cs << ": " << cnt << endl;
  }


  return 0;
}
