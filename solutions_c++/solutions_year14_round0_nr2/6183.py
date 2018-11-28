#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
  int N = 0;
  int caseNum = 0;
  cin >> N;
  while(N-->0) {
    caseNum++;
    double memo[1000000] = {0};
    double  F;
    double  C;
    double  X;
    cin >> C;
    cin >> F;
    cin >> X;
    vector<double> v;;
    double sum = 0 ;
    v.push_back(X/2.0);
    double temp = X/2.0;
    for(double f = 2.0; 1 ; f+=F) {
       sum += (C/f);
       double t = X/(f+F);
       double m = sum + t;
       if(temp < m)
        break;
       v.push_back(m);
       temp = m;
//       printf("%d %f %f\n",i,f,g);
    }
      printf("Case #%d: %.7f\n",caseNum,*min_element(v.begin(),v.end()));
 }

return 0;
}
