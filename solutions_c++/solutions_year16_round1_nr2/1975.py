#include <map>
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <sstream>
#define forn(n) for(int i=0;i<n;i++)
#define SIZE 2010
typedef long long LL;
using namespace std;
int row_number ;
map<int, int> hight_data;
vector<int> odd_soldier;
bool key_in_map(int key){
  return ! (hight_data.find(key) == hight_data.end());
}

void get_hight_to_map() {
  int c;
  vector<int> cl;
  std::string line;
  std::getline(cin, line);
  std::istringstream iss(line);
  while ( iss >> c) {
    if (key_in_map(c)){
      hight_data[c]++;
      hight_data[c] = hight_data[c]%2;
    }else{
      hight_data[c] = 1;
    }
  }
  return;
}

void init(){
  odd_soldier.clear();
  hight_data.clear();
  int i;
  for (i=1;i<=2*row_number-1;i++)
    get_hight_to_map();
}

int solve(int case_num){
  scanf("%d\n", &row_number);
  init();
  map<int, int>::iterator it;
  for(it=hight_data.begin();  it!=hight_data.end(); ++it){
    if (it->second == 1){
      odd_soldier.push_back(it->first);
    }
  }
  sort(odd_soldier.begin(), odd_soldier.end());
  vector<int>::iterator it_of_result;
  printf("Case #%d: ", case_num);
  for(it_of_result=odd_soldier.begin();  it_of_result!=odd_soldier.end(); ++it_of_result){
    cout << *it_of_result << " ";
  }
  cout <<endl;
  return 0;
}

int main(){
  int T, i;
  scanf("%d", &T);
  for (i = 1; i<=T; ++i )
    solve(i);
  return 0;
}
