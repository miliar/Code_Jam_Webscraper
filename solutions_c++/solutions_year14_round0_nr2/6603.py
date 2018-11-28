#include <iostream>
#include <set>
#include <vector>
#include <cstdlib>
#include <sstream>
#include <algorithm>

using namespace std;

void solve(int i){
  double C, F, X;
  cin >> C >> F >> X;
  // greedy run
  vector<double> goalTime;
  double sumCookie = 0;
  double curTime = 0;
  double vel = 2;
  while(true){
    double timeFinish = X/vel + curTime;
    if(goalTime.size() > 0 && timeFinish > goalTime[goalTime.size()-1]){
      printf("Case #%d: %.7f\n", i, goalTime[goalTime.size()-1]);
      return;
    }       
    goalTime.push_back(timeFinish);
    curTime += C / vel;
    vel += F;
  }
}

int main(){
  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    solve(i+1);
    //cout << "Case #" << i+1 << ": " << solve() << endl;
  }
}
