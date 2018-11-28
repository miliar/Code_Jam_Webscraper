#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<cmath>
using namespace std;

int main(){
  long long t, standing=0, needfriends=0, maxppl=0, getnumber=0;
  string ppl;
  cin >> t;
  for(int i=0; i<t; i++){
    standing=0;
    needfriends=0;
    cin >> maxppl >> ppl;
    for(int j=0; j<=maxppl; j++){
      getnumber=ppl[j]-'0';
//       cout << getnumber << " ";
//       cout << "uz stoji " << standing << " ludi. Potrebujeme aby stalo " << j << endl; 
      if(standing>=j){
	standing+=getnumber;
      }
      else{
	if(getnumber!=0){
// 	  cout << "pozyvam " << j-standing << " priatelov\n";
	  needfriends+=j-standing;
	  standing=j+getnumber;
	}
      }
    }
    cout << "Case #" << i+1 <<": " << needfriends << endl;
  }
  return 0;
}