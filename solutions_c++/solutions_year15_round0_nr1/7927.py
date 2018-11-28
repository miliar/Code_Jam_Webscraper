#include <cstdlib>
#include <cstring>
#include <iostream>
#include <fstream>
#include <string>
#include <stack>
using namespace std;



int minFriends(string input, int len){
  int minFriends = 0;
  int subTotal = 0;
  int val;

  if(len>=0) subTotal += input[0] - '0';

  for(int i=1; i<=len; i++){
    val = input[i] - '0';

    if(subTotal < i){
      minFriends += (i-subTotal);
      subTotal += (i-subTotal);
    } 
    
    subTotal += val;
  }


  //cout << "subtotal " << subTotal << endl;
  return minFriends;
}



void run(){
  ifstream in("in");
  ofstream out("out");
  int tc, len;
  string input;

  in >> tc;

  for(int i=0; i<tc; i++){
    in >> len;
    in >> input;

    out << "Case #" << i+1 << ": " << minFriends(input, len) << endl;
  }
}


int main(){
  run();
  //cout << minFriends("6000008", 6) << endl;;
  return 0;
}
