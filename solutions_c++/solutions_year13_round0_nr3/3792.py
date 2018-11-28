#include <iostream>
#include <cmath>
#include <string>
using namespace std;
bool faire(int num){
  string num_str = to_string(num);
  int n = num_str.size();
  for(int i=0;i<n/2;i++){
    if(num_str[i] != num_str[n-1-i]){
      return false;
    }
  }
  return true;
}
bool square(int num){
  double sq = sqrt(num);
  if(sq == (int)sq){
    return faire((int)sq);
  }
  return false;
}
int main(){
  int testcases;
  cin >> testcases;
  //cin.ignore()
  for(int i=1;i<=testcases;i++){
    int A, B;
    cin >> A >> B;
    int count = 0;
    for(int test = A; test<=B; test++){
      if(faire(test) && square(test)){
        //cout << test << endl;
        count++;
      }
    }
    cout << "Case #" << i << ": " << count << endl; 
  }
}