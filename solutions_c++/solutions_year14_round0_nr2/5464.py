#include<iostream>
#include<cstdio>
using namespace std; 

int T;

double func(){
  double C,F,X,ret,up;
  cin >> C >> F >> X;
  ret = 0.0;
  up = 2.0;  
  while(1){
    double a = X/up;
    double b = (C/up + X/(up+F));
    if(a > b){
      ret += C/up;
      up += F;
    }
    else {
      ret += a;
      break;
    }
  }
  return ret;
}

int main(){
  cin >> T;
  for(int i = 0 ; i < T ; i++){
    cout << "Case #" << i+1 << ": ";
    printf("%.7f\n",func());
  }
  return 0;
}
