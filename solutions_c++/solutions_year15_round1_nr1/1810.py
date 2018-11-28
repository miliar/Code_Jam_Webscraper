#include <iostream>
#include <fstream>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::vector;

int first(vector<int> &list){
  int result = 0;
  for(unsigned long i = 0; i < list.size() - 1; i++){
    if(list[i] > list[i+1]){
      result += (list[i]-list[i+1]);
    }
  }
  return result;
}

int second(vector<int> &list){
  int result = 0;
  int max = 0;
  for(unsigned long i = 0; i < list.size() - 1; i++){
    if(list[i] - list[i+1] > max){
      max = list[i] - list[i+1];
    }
  }
  for(unsigned long i = 0; i < list.size() - 1; i++){
    if(max > list[i]){
      result += list[i];
    }
    else{
      result += max;
    }
  }
  return result;
}

int main(){
  ifstream inFile("A-large.in");
  ofstream outFile("output.txt", std::ios::out);
  int cases;
  int N;
  vector<int> list;

  inFile >> cases;
  for(int j = 1; j <= cases; j++){
    inFile >> N;
    list.resize(N);
    for(int i = 0; i < N; i++){
      inFile >> list[i];
    }
    outFile << "Case #" << j << ": " <<  first(list) << " " << second(list) << endl;
    
  }
  
  return 0;
}
