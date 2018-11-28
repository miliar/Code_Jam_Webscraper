#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <sstream>

using namespace std;

void flip(string *s, int pos);

int happyP(string *s){
  string::iterator itp;
  int flipNum = 0;
  int pos = s->size();
  for(itp = --s->end(); itp != s->begin(); itp--){
    if(*itp == '-'){
      flip(s, pos);
      ++flipNum;
    }
    --pos;
  }

  if(pos == 1){
    itp = s->begin();
    if(*itp == '-'){
      flip(s, pos);
      ++flipNum;
    }
  }
  return flipNum;
}

void flip(string *s, int pos){
  string::iterator it = s->begin();
  for(int i = 0; i <= pos; i++){
    (*it == '-') ? *it = '+' : *it = '-';
    ++it;
  }
}

int main(){
  int T = 0, flips = 0;
  string *panc;
  cin >> T;

  for(int i = 1; i <= T; i++){
    string test;
    cin >> test;
    panc = &test;
    cout << "Case #" << i << ": ";
    flips = happyP(panc);
    cout << flips << endl;
  }

  exit(0);
}
