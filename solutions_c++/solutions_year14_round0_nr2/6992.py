#include <cstdio>
#include <iostream>
using namespace std;
double get_minimum_time(double C,double F,double X){
  double initial_time = X/2;
  double ret_time = 0.0;
  double final_time=0.0;
  double latest_earnings = 2;
  while(true){
    final_time  = ret_time+((C/latest_earnings)+(X/(latest_earnings+F)));
    if(final_time<initial_time){
      ret_time += C/latest_earnings;
      initial_time = final_time;
      latest_earnings += F;
    }else{
      ret_time += (X/latest_earnings);
      break;
    }
  }
  return initial_time;
}

int main(){
  int tt;
  cin>>tt;
  for(int test_case=1;test_case<=tt;test_case++){
    double C,F,X;
    cin>>C;
    cin>>F;
    cin>>X;
    double min_pos = get_minimum_time(C,F,X);
    printf("Case #%d: %.07lf\n",test_case,min_pos);
  }
  return 0;
}
