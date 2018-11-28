#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

void doproblem(int testcase){
  int n;
  cin >> n;
  map<int,int> m1;
  for(int i=0; i<4; i++){
    for(int j=0; j<4; j++){
      int temp;
      cin >> temp;
      if(i+1==n) m1[temp] = 0;
    }
  }
  cin >> n;
  map<int,int> m2;
  for(int i=0; i<4; i++){
    for(int j=0; j<4; j++){
      int temp;
      cin >> temp;
      if(i+1==n) m2[temp] = 0;
    }
  }
  vector<int> solutions;
  for(map<int,int>::iterator it=m1.begin(); it!=m1.end(); it++){
    if(m2.count(it->first) == 1) solutions.push_back(it->first);
  }
  cout << "Case #" << testcase << ": ";
  if(solutions.size() == 0){
    cout << "Volunteer cheated!" << endl;
  }
  if(solutions.size() == 1){
    cout << solutions[0] << endl;
  }
  if(solutions.size() > 1){
    cout << "Bad magician!" << endl;
  }
}

int main(){
  int n;
  cin >> n;
  for(int i=0; i<n; i++){
    doproblem(i+1);
  }
}
