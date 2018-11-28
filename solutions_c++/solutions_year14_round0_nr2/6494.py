#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;


int main(){
  int N, i, j, k, m, n;
  cin >> N;
  for ( i = 0; i < N; i++) {
    double c, f, x;
    cin >> c >> f >> x;
    

    double lowest = 10000000000;
    double time = 0;
    double already = 0;
    double s = 2;

    bool stop = false;
    
    while(stop != true) {
      double t = time + ((x - already) / s); 
      if (t < lowest) {
        lowest = t;
      }
      double xt = (c/f) + time;
      if (xt >= t){
        stop = true;
      }
      time += c / s; 
      s += f;
    }

    printf("Case #%d: %.7f\n", (i+1), lowest); 
    //cout << "Case #" << (i+1) << ": " << lowest << "\n";

    /*
    if (same == 0) {
      cout << "Case #" << (i+1) << ": " << "Volunteer cheated!\n";
    } else if (same == 1) {
      cout << "Case #" << (i+1) << ": " << result << "\n";
    } else {
      cout << "Case #" << (i+1) << ": " << "Bad magician!\n";
    } 
    */
    
  }
  return 0;
}
