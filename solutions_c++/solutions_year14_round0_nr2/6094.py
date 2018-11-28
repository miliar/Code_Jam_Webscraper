#include <iostream>
using namespace std;

int main(void){
  long double t, c, f, x;
  cin >> t;
  for(long long i=1; i <= t; i++){
    cin >> c >> f >> x;
    long double last = 0;

    long double realSeconds;
    if (x == 2.0f){ realSeconds = 1.0f; } else
    for(long long n=0; true; n++){
      long double seconds = 0, cps = 2.0,farms;
      #pragma omp parallel for
      for(farms=0; farms < n; farms++){
        seconds += c / cps;
        cps += f;
      }
      seconds += x / cps;

      if (last == 0){ }
      else if (seconds > last){
        realSeconds = last;
        break;
      } 
      last = seconds;
    }

    printf("Case #%lld: %0.9Lf\n", i, realSeconds);
  }
}
