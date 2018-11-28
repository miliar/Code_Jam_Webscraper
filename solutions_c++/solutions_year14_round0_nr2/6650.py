#include <iostream>

using namespace std;

int main() {
  long T, m;
  double C, F, X, time1, time2, cost, temp, prev;
  
  cin>>T;
  
  m = 1;
  while(T--) {
    cin>>C>>F>>X;
   
    cost = 2;
    prev = C / cost;
    time1 = X / cost;
    time2 = prev + X / (cost + F);

    while(time1 > time2) {
      temp = time2;
      cost = cost + F;
      prev = prev + C / cost;
      time2 = prev + X / (cost + F);
      time1 = temp;
    }

    cout.precision(15);
    cout<<"Case #"<<m<<": "<<time1<<endl;
    m++;
  }
  return 0;
}
      

