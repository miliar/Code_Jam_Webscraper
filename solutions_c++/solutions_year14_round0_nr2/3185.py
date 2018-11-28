#include <iostream>
#include <set>

#define REPEAT 100000
using namespace std;
typedef set<int> S;

int main(){
  int T = 0;
  cin >> T;

  for(int t = 0; t < T; ++t){
    double cost[REPEAT];
    double C = 0;
    double F = 0;
    double X = 0;
    cin >> C;
    cin >> F;
    cin >> X;
    double time = X/2.0;
    cost[0] = 0;
    for(int i = 1; i < REPEAT; ++i){
      cost[i] = cost[i-1];
      double nf = 2 + F*(i-1);
      cost[i] += C/nf;
      double nt = cost[i] + (X/(nf+F));
      if(time > nt){
        time = nt;
      }else{
        break;
      }
    }
    printf("Case #%d: %.7lf\n", (t+1), time);
  }
}
