#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;



void flip(string &x, long long start, long long end){
  for(long long i = start; i < end; i++){
    if(x[i] == '-') x[i] = '+';
    else x[i] = '-';
  }
  reverse(x.begin() + start, x.begin() + end);
}

bool all_happy(string x){
  for(auto it = x.begin(); it != x.end(); it++){
    if(*it != '+') return false;
  }
  return true;
}

int main(){

  int total_tests;
  cin >> total_tests;
  for(int i = 1; i <= total_tests; i++){
    string input;
    int n;
    long long index = 0;
    cin >> input;
    long long count = 0;

    while(!all_happy(input)){
      auto it = input.begin();
      index = 0;
      count++;
      if(*it == '-'){
        while(it != input.end() && *it != '+'){
          if(*(it+1) == '+' || (it+1) == input.end()){
            flip(input,0,index+1);
            break;
          }
          it++;
          index++;
        }
      }
      else if(*it == '+'){
        while(it != input.end() && *it != '-'){
          if(*(it+1) == '-' || (it+1) == input.end()){
            flip(input,0,index+1);
            break;
          }
          it++;
          index++;
        }
      }

    }



    cout<<"Case #"<<i<<": "<<count<<endl;

   
  }


  return 0;
}