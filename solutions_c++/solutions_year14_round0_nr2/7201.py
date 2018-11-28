#include<iostream>
#include<iomanip>
#include<stdio.h>
#include<vector>
#include <limits>
#include <math.h>
using namespace std;
const double DOUBLE_MAX = std::numeric_limits<double>::max();

void testcase(int t);

double time_to_get_n(int n, double c, double f, vector<double>& cache){
    if (n==0) return 0;
    if (cache[n] != -1) return cache [n];
    double rate = 2 + (n-1) * f;
    cache[n] =  c/rate + time_to_get_n(n-1,c,f, cache);
    return cache[n];
}



int main(void){
    std::ios_base::sync_with_stdio(false);
    
    std::cout << std::setiosflags(std::ios::fixed) << std::setprecision(7);
    int t;
    cin >> t;
    for (int i=1; i<=t; ++i)testcase(i); 
    return 0;    
}

void testcase(int t){
 double c,f,x;
 cin >> c >> f >> x;
 int n = 0;
 double min_time = DOUBLE_MAX;
 int max_n = int(ceil(x));
 vector<double> cache(max_n, -1);
 while (true){
     double current_rate = 2 + n*f;
     double time_taken = x/current_rate + time_to_get_n(n,c,f,cache);
     if (time_taken > min_time) break;   
     else {
         n+=1;
         min_time =time_taken;
     }
 }
 cout <<"Case #" << t << ": " << min_time << endl;
}

