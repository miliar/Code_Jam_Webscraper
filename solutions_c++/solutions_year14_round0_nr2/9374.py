#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using std::cin;
using std::vector;
using std::sort;

double calc_time(double c, double f, double x, int n){
   double time = 0;
   double divisor = 2;
   for(int i = 0; i < n; i++){
      time += c/divisor;
      divisor += f;
   }
   time += x/divisor;
   return time;
}

int main(){
   vector<float> times;
   int cases;
   int num_farms;
   double c,f,x;
   double next_time;
   cin >> cases;

   for(int i = 0; i < cases; i++){
      int num_farms = 0;
      cin >> c;
      cin >> f;
      cin >> x;
      times.push_back(calc_time(c,f,x,num_farms));
      num_farms++;
      next_time = calc_time(c,f,x,num_farms);
      while(next_time < times[times.size() - 1]){
         times.push_back(next_time);
         num_farms++;
         next_time = calc_time(c,f,x,num_farms);
      }

      sort(times.begin(), times.end());
      printf("Case #%i: %.7f\n", i+1, times[0]);
      times.clear();
   }
   return 0;
}
