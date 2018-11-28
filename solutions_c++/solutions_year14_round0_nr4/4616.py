#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

vector<double> Naomi;
vector<double> Ken;
int N;

int dewar(){
  int p1s,p2s,p1e,p2e;
  p1s = p2s=0;
  p1e = p2e=N-1;
  int result =0;
  while (p1s<= p1e){
    if (Naomi[p1e]>Ken[p2e]){
      ++result;
      --p1e; --p2e;
    }
    else{
      ++p1s;--p2e;
    }
  }
  return result;
}


int realwar(){
  int p1s=0,p2s=0;
  int result =0;
  while (p2s<N){
    if (Ken[p2s]<Naomi[p1s]){
      ++result;
    }
    else
      ++p1s;
    ++p2s;
  }
  return result;
}
int main(){
  int tc;
  cin>>tc;
  for (int i=1; i<=tc; ++i){
    cin>>N;
    Naomi.clear();
    Ken.clear();
    double mass;
    for (int i=0; i<N; ++i) {cin>>mass; Naomi.push_back(mass);}
    for (int i=0; i<N; ++i) {cin>>mass; Ken.push_back(mass);}
    sort(Naomi.begin(),Naomi.end());
    sort(Ken.begin(),Ken.end());
    printf("Case #%d: %d %d\n",i, dewar(),realwar());
  }

}
