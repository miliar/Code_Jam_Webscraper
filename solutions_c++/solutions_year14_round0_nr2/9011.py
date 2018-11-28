#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <iomanip>
using namespace std;

int main(){
  int T;
  cin>>T;

  for(int t=1;t<=T;t++){
    double C; //Cost of cookie farm
    double F; //Cookie farm bonus
    double X; //Cookies to win
    cin>>C>>F>>X;

    double cookies_per_second = 2;
    double time               = 0;
    while(true){
      double time_to_win             = X/cookies_per_second;
      double time_to_get_cookie_farm = C/cookies_per_second;
      double time_to_win_with_farm   = X/(cookies_per_second+F);
      cerr<<time<<" "<<cookies_per_second<<endl;
      if( time_to_win<=time_to_get_cookie_farm+time_to_win_with_farm){
        time += time_to_win;
        break;
      } else {
        time               += time_to_get_cookie_farm;
        cookies_per_second += F;
      }
    }

    cout<<"Case #"<<setprecision(10)<<t<<": "<<time<<endl;
  }
}