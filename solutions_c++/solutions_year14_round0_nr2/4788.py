#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int K_maxfarms=11111;
double build_farm[K_maxfarms];
double C,F,X;

void solve(){
  int farms=0;
  build_farm[farms]=0;
  double current=2.0;
  double t_curr,t_next;
  t_curr=t_next=X/current;
  do{
    t_curr = t_next;
    build_farm[farms+1]=build_farm[farms]+ C/current;
    current += F;
    ++farms;
    t_next = build_farm[farms]+X/current;
  }while (t_curr>=t_next);
  printf("%.8lf",t_curr);

}
int main(){
  int T;
  cin>>T;
  for (int i=1; i<=T; ++i){
    printf("Case #%d: ", i);
    cin>>C>>F>>X;
    solve();
    cout<<endl;
  }

}
