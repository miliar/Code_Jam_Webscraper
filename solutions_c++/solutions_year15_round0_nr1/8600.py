/*
 * author: Marwan Osman
 * email : lordm2005@gmail.com
 *
 * Code Jam 2015
 * Qualification Round
 * Problem A
 * 
 */
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main(){
  ifstream in("a.in");
  ofstream out("a.out");

  int n,maxshy;
  string line;
  in >> n;
  
  for(int i=0;i<n;i++){
    int minnum = 0;
    int sum = -1;
    in >> maxshy;
    in >> line;
    for(int j=0;j< maxshy;j++){
      int Si = line[j] - '0';
      sum += Si;
      if(sum < j){
        minnum = minnum + j - sum;
        sum = sum +j -sum;
      }
    }
    out <<"Case #" << (i+1) <<": " << minnum << endl;
  }

  return 0;
}
