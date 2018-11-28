#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

void buyaform( double &c,  double &f,  double &p,  double &tt) {
   tt += c/p;
   p += f;
}

//bool buymore(double &c, double &f, double &p, double &x) {
bool buymore( double c,  double f,  double p, double x) {
    double t1 = x/p;
    double t2 = c/p;
    double p2 = p+f;
    double tn = x/p2;
   if(t1 > t2+tn) return true;
   return false;
}

int main() {
   int t,n(1);
   double c,f,x,p(2);
   cin >> t;
   double tt(0);
   while(t--) {
      cin >>c >>f >>x;
      while(true) {
     //    cout << tt << endl;
         if(!buymore(c, f, p, x)) {
            tt += x/p;
            break;
         }
         buyaform(c,f,p,tt);
      }
      cout << "Case #" << n++ <<": " << std::fixed << std::setprecision(7) << tt << endl;
      tt = 0;
      p = 2;
   }
   return 0;
}
