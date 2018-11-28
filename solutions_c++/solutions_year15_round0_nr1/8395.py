#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int Smax;
string S;

int Solve(){
  scanf("%d", &Smax);
  cin>>S;

  int curr = 0;
  int ret = 0;
  for (int i = 0; i <= Smax; i++){
    int r = (int)S[i] - (int)'0';

    if (curr < i){
      ret += i - curr;
      curr = i;
    } 

    curr += r;
  }

  return ret;
}

int main(){
  int test;
  scanf("%d", &test);
  for (int i = 0; i < test; i++){
    printf("Case #%d: %d\n", i + 1, Solve());
  }
  return 0;
}
