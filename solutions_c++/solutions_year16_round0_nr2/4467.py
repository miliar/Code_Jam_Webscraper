#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;
int main(){
  int T;
  string cakes;
  scanf("%d", &T);
  for(int i=1; i<=T; i++){
    cin >> cakes;
    int len = cakes.length();
    vector<bool> origin(len);
    vector<bool> inter(len);
    for(int j=0; j<len; j++){
      if(cakes.substr(j, 1).compare("+") == 0)
        origin[j] = true;
      else origin[j] = false;
    }
    int lastplus = len; // if origin[0] == false, flip from 0 to lastplus-1
    int firstplus = 0; // to count '+' if origin[0] == true
    int cnt = 0; // contains the answer
    for(int j=len-1; j >= 0; j--){
      if(!origin[j]){
        lastplus = j + 1;
        break;
      }
      else if(j == 0)
        lastplus = 0;
    }
    while(lastplus > 0){
      if(origin[0]){
        for(int j=1; j<lastplus; j++){
          if(!origin[j]){
            firstplus = j-1;
            break;
          }
        }
        for(int j=0; j<=firstplus; j++){
          inter[firstplus-j] = !origin[j];
        }
        for(int j=0; j<=firstplus; j++){
          origin[j] = inter[j];
        }
        cnt++;
      }
      else{
        for(int j=0; j<lastplus; j++){
          inter[lastplus-j-1] = !origin[j];
        }
        for(int j=0; j<lastplus; j++){
          origin[j] = inter[j];
        }
        int tmplast = lastplus;
        for(int j = tmplast-1; j >= 0; j--){
          if(!origin[j]){
            lastplus = j + 1;
            break;
          }
          else if(j == 0)
            lastplus = 0;
        }
        cnt++;
      }
    }
    printf("Case #%d: %d\n", i, cnt);
  }
  return 0;
}
