#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>
using namespace std;

int dwar(vector<pair<double,int> > v){
  int ken = 0, attack=0;
  for(int i=0; i<v.size(); i++){
    if(v[i].second == 1){
      ken++;
    }
    if(v[i].second == 0){
      if(ken >0){
        attack++;
        ken--;
      }
    }
  }
  return attack;
}

int war(vector<pair<double,int> > v){
  int naomi = 0, attack=0;
  for(int i=0; i<v.size(); i++){
    if(v[i].second == 0){
      naomi++;
    }
    if(v[i].second == 1){
      if(naomi >0){
        attack++;
        naomi--;
      }
    }
  }
  return v.size()/2 - attack;
}

void doproblem(int testcase){
  int n;
  cin >> n;
  vector<pair<double,int> > v;
  for(int i=0; i<n; i++){
    double temp;
    cin >> temp;
    v.push_back(make_pair(temp,0));
  }
  for(int i=0; i<n; i++){
    double temp;
    cin >> temp;
    v.push_back(make_pair(temp,1));
  }
  sort(v.begin(), v.end());
  printf("Case #%d: %d %d\n", testcase, dwar(v), war(v));
}

int main(){
  int n;
  cin >> n;
  for(int i=0; i<n; i++){
    doproblem(i+1);
  }
}
