
#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

void pv(vector<int> v){
  for(int i=0; i<v.size(); i++){
    cout << v[i] << " ";
  }
  cout << endl;
}

void pv(vector<char> v){
  for(int i=0; i<v.size(); i++){
    cout << v[i] << " ";
  }
  cout << endl;
}

vector<char> rf(vector<char> v){ // reverse and flip
  reverse(v.begin(), v.end());
  for(int i=0; i<v.size(); i++){
    if( v[i] == '+' ){
      v[i] = '-';
    }else{
      v[i] = '+';
    }
  }
  return v;
}

bool check(vector<char> v){
  for(int i=0; i<v.size(); i++){
    if(v[i] != '+'){
      //cout << "check rtns false" << endl;
      return false;
    }
  }
  //cout << "check rtns true" << endl;
  return true;
}

int main(){
  int T;
  cin >> T;
  vector<char> c;
  for(int t=1; t<=T; t++){
    string st;
    cin >> st;
    //cout << "st: " << st << endl;

    vector<char> c(st.begin(), st.end());

    //cout << "c: ";
    //pv(c);

    int flips = 0;
    while(!check(c)){

      // ensure top is down, if not flip as many as possible at once
      //cout << "top equal to: " << c[0] << endl;
      if(c[0] == '+'){
        flips += 1;
        for(int i=0; i<c.size(); i++){
          if(c[i] == '-'){ // break on first down facing
            break;
          }else{
            c[i] = '-';
          }
        }
      }

      if(check(c)){ break; }

      // find the deepest down facing and flip all above
      for(int i=c.size()-1; i>=0; i--){
        if(c[i] == '-'){

          //cout << "deepest is " << i << endl;

          vector<char> cc(c.begin(), c.begin()+i+1);
          //cout << "pass rf: ";
          //pv(cc);
          cc = rf(cc);
          //cout << "rf rtns: ";
          //pv(cc);
          for(int j=0; j<cc.size(); j++){
            c[j] = cc[j];
          }
          flips += 1;
          break;
        }
      }
    }
    cout << "Case #" << t << ": " << flips << endl;

  }
  return 0;
}

/*
5
-
-+
+-
+++
--+-
*/
