#include <algorithm>
#include <iterator>
#include <vector>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <string>
#include <set>
using namespace std;

ofstream out("output.txt");

void solve(double C, double F, double X){
  vector<double> total_cost;
  vector<double> cost;
  vector<double> cost2;
  double rate = 2.0;
  double sum = 0;
  int count = 0;
  double div;

  for(int i=0; i<3; i++){
    cost.push_back(X/rate);
    cost2.push_back((X-C)/rate);
    sum += (C/rate);
    total_cost.push_back(sum);
    rate += F;
  }

  if(cost[count] <= total_cost[count]){ 
    out << fixed << setprecision(7) << cost[count] << endl; 
    return;
  }

  while(true){
    if((total_cost[count]+cost2[count]) <= (total_cost[count]+cost[count+1])){
      out << fixed << setprecision(7) << (total_cost[count]+cost2[count]) << endl;
      break;
    }
    
    cost.push_back(X/rate);
    cost2.push_back((X-C)/rate);
    sum += (C/rate);
    total_cost.push_back(sum);
    rate += F;
    count++;
  }    
}



int main(int argc, char** argv){
  if(argc < 2){
    cout <<"Enter input file name" << endl;
    exit(1);
  }

  double T, C, F, X;
  ifstream in(argv[1]);

  in >> T;

  for(int i=1; i<=T; i++){
    in >> C; in >> F; in >> X;
    out << "Case #" << i << ": "; 
    solve(C, F, X);
  }

  
  return 0;
}
