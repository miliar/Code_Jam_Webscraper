#include <iostream>  
#include <string>
using namespace std;

string pNum(string phone){
  int numbers[10] = {0};
  int numLen = phone.length();
  string::iterator it;
  int i = 0;
  char c;
  for ( it = phone.begin() ; it < phone.end(); it++ ,i++)
  {
    c = phone[i];
    if(c == 'Z'){
      numbers[0]++; 
    }
    if(c == 'W'){
      numbers[2]++; 
    }
    if(c == 'U'){
      numbers[4]++; 
    }
    if(c == 'X'){
      numbers[6]++; 
    }
    if(c == 'G'){
      numbers[8]++; 
    }
    if(c == 'O'){
      numbers[1]++; 
    }
    if(c == 'R'){
      numbers[3]++; 
    }
    if(c == 'F'){
      numbers[5]++; 
    }
    if(c == 'S'){
      numbers[7]++; 
    }
    if(c == 'N'){
      numbers[9]++; 
    }
  }
  numbers[1] = numbers[1]-numbers[0]-numbers[2]-numbers[4];
  numbers[3] = numbers[3]-numbers[4]-numbers[0];
  numbers[5] = numbers[5]-numbers[4];
  numbers[7] = numbers[7]-numbers[6];
  numbers[9] = (numbers[9]-numbers[7]-numbers[1])/2;
  string phonenumber;
  for(int k = 0; k<10; k++){
    int val = numbers[k];
    for(int j = 0; j<val; j++){
      phonenumber += std::to_string(k);
    }
  }
  return(phonenumber);
}

int main() {
  int t;
  string number;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> number;  // read n and then m.
    
    cout << "Case #" << i << ": " << pNum(number) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}
