#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<cmath>
using namespace std;

int main(){
  long long t=0, x=0, c=0, r=0;
  cin >> t;
  for(int i=0; i<t; i++){
    cin >> x >> r >> c;
    if((r*c)%x!=0){
      cout << "Case #" << i+1 << ": RICHARD\n";
    }
    else{
      if(x<=2){
	cout << "Case #" << i+1 << ": GABRIEL\n";
      }
      else{
	if(r*c == 6 || r*c == 9 || r*c == 12 || r*c == 16){
	  cout << "Case #" << i+1 << ": GABRIEL\n";
	}
	else{
	  cout << "Case #" << i+1 << ": RICHARD\n";
	}
      }
    }
  }
  return 0;
}