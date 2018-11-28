#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
  int t;
  cin >> t;
  for (int delta = 1; delta <= t; ++ delta)
  {
    double c,f,x, cur=0, ans;
    cin >> c >> f >> x;
    ans = x/2.0;
    for(int l=0;l<500000;l+=1)
    {
      cur += c/(l*f+2);
      if(cur + x/(2+f+l*f) < ans)
        ans = cur + x/(2+f+l*f);
    }
    cout << "Case #" << delta << ": ";
    cout << setprecision(7) << fixed << ans << endl;
  }
  return 0;
}
