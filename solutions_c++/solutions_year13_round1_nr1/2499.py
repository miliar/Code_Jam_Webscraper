#define _USE_MATH_DEFINES
#include <iostream>

#include <cmath>



using namespace std;

unsigned long long solve(unsigned long long r, unsigned long long t){
  unsigned long long ret = 0;

  double a = 2;
  double b = (2 * r - 1);
  double c = t;

  double root = b * b + (4 * a * c);

  
  root = sqrt (root);
  //cout << "root : " << root << endl;

  double ue = root - b;
  double temp = ue / (2 * a);

  ret = (unsigned long long)temp;

  return ret;
}
int main(){
  int testcase = 0;
  cin >> testcase;
  for(int i = 1; i <= testcase; i++){
    unsigned long long  r = 0;
    unsigned long long  t = 0;
    cin >> r;
    cin >> t;

    //cout << "r : " << r << ", t : " << t << endl;

    unsigned long long  ans = solve(r,t); 
    std::cout << "Case #" << i << ": " << ans << std::endl;
  }
  return 0;

}
