#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
using namespace std;

int findMax(vector<int> vec){
  auto it = max_element(vec.begin(), vec.end());
  return *it;
}

int lowerMaxTo(vector<int> diners, int threshold){
  int special_minutes = 0;

  for(int pancakes : diners){
    int cur_pancakes = pancakes;

    while(cur_pancakes > threshold){
      cur_pancakes -= threshold;
      ++special_minutes;
    }
  }
  return special_minutes + threshold;
}

int calculateMinutesNeeded(vector<int> diners){
  int max = findMax(diners); //initially, max is the max pancakes.
  for(int i = 1; i < max; ++i) {
    int cost = lowerMaxTo(diners, i);
    if(cost < max) {
      max = cost;
    }
  }
  return max;
}


int main(){
  vector<int> diners;
  string line;
  int T, D, P_j;
  int case_no = 1;
  ifstream inputf ("input-large.txt");
  if (inputf.is_open())
  {
    //test numbers
    getline (inputf,line);
    T = stoi(line);
    for (int i = 0; i < T; ++i){
      getline (inputf, line);
      D = stoi(line);

      getline(inputf, line); //take in P
      istringstream iss(line); //parse P to add to diners
      for (int j = 0; j < D; ++j){
        iss >> P_j;
        diners.push_back(P_j);
      }
      cout << "Case #" << case_no << ": " << calculateMinutesNeeded(diners) <<
        endl;

      diners.clear();
      ++case_no;
    }
  }
  inputf.close();

  return 1;
}
