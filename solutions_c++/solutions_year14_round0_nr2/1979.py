#include<iostream>
#include<cmath>
#include<iomanip>

using namespace std;

int main(){
  int n;
  cin >> n;
  for(int i = 1; i <= n; i++){
    double c, f, x;
    cin >> c >> f >> x;
    double sum = 0;
    double cookie = 2.0;
    double maxtime = x/cookie;
    double ans = maxtime;
    double temp;
    double ftime;
    while(1){
      ftime = c/cookie;
      sum += ftime;
      cookie += f;
      temp = x/cookie;
      sum += temp;
      if(sum < ans){
	ans = sum;
	sum -= temp;
      }else{
	break;
      }
    }
    cout << "Case #" << fixed << setprecision(7) << i << ": " << ans << endl;
  }
  return 0;
}
