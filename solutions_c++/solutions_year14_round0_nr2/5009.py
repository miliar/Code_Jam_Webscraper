#include<iostream>
#include<cstdio>

using namespace std;

double solve(double C, double F, double X){
  double ans = 1e100;
  double add = 2.0;
  double now = 0;
  while(1){
    bool update = false;
    double goal = now + X/add;
    if(ans > goal){
      ans = goal;
      update = true;
    }
    now += C/add;
    add += F;
    if(!update) break;
  }
  return ans;
}

int main(){
  int T;
  cin >> T;
  for(int tc = 0; tc < T; tc++){
    double C,F,X;
    cin >> C >> F >> X;
    printf("Case #%d: %.7f\n",tc+1, solve(C,F,X));
  }
  return 0;
}
