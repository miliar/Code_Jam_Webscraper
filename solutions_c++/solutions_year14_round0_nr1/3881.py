#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<cmath>
#include<set>
using namespace std;

int main(){
  long long testcases=0, row=0, same=0, i=0, j=0, k=0, pomocnapremenna=0, whichnumber=0;
  set<int> numbers;
  cin >> testcases;
  for(i=0; i<testcases; i++){
    pomocnapremenna=0;
    same=0;
    whichnumber=0;
    row=0;
    numbers.clear();
    cin >> row;
    for(j=0; j<4; j++){
      if(row-1!=j){
	cin >> pomocnapremenna >> pomocnapremenna >> pomocnapremenna >> pomocnapremenna;
      }
      else{
	for(k=0; k<4; k++){
	  cin >> pomocnapremenna;
	  numbers.insert(pomocnapremenna);
// 	  cout << pomocnapremenna << " ";
	}
      }
    }
    cin >> row;
    for(j=0; j<4; j++){
      if(row-1!=j){
	cin >> pomocnapremenna >> pomocnapremenna >> pomocnapremenna >> pomocnapremenna;
      }
      else{
	for(k=0; k<4; k++){
	  cin >> pomocnapremenna;
	  if(numbers.count(pomocnapremenna)==1){
	    same++;
	    whichnumber=pomocnapremenna;
	  }
// 	  cout << pomocnapremenna << " ";
	}
      }
    }
    if(same==0){
      cout << "Case #" << i+1 << ": "<< "Volunteer cheated!\n";
    }
    if(same==1){
      cout << "Case #" << i+1 << ": " << whichnumber << endl;
    }
    if(same>1){
      cout << "Case #" << i+1 << ": " << "Bad magician!\n";
    }
  }
  return 0;
}