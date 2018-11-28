

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>


using namespace std;  // since cin and cout are both in namespace std, this saves some text


//0-based idx
string flip(string str, int idx){ 
  string s;
  for (int i = 0; i <= idx; i++){
    if(str[i]=='+'){
      s+='-';
    } else {
      s+='+';
    }
  }
  std::reverse(s.begin(), s.end());
  return s + str.substr(idx+1);
}

bool AllHappy(string str){
  for(char &c : str) {
    if(c=='-'){
      return false;
    }
  }
  return true;
}

int getMin(string p){
  
  int fi,li;
  int flips =0;
  while(!AllHappy(p)){
    fi = -1;
    li = 101;
    for(int i=p.length()-1; i>=0; i--){
      if(p[i]=='-'){
        if(i>fi){
          fi = i;
        }
        if(i<li){
          li = i ;
        }
      }else if(p[i]=='+' && fi!=-1 && li!=101){
        break;
      }
    }
    if(li==0){
      p = flip(p, fi);
    }else if (AllHappy(p.substr(0,li-1))){
      p = flip(p, li-1);
    }else if (!(AllHappy(p.substr(0,li-1))))
    {
      for(int j=fi; j>0; j--){
        if(p[j]==p[0]){
          fi = j;
          break;
        }
      }
      p = flip(p, fi);
    }
    flips++;

    
  }
  return flips;
}

int main() {
  string pan;
  int t, index;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> pan;  // read n and then m.
    cout << "Case #" << i << ": " << getMin(pan) << endl;
    //cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}

