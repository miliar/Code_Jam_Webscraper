#include <iostream>
#include <string>



using namespace std;

string getTheLastWord(string&);

int main() {
  int T;
  string S,last;
  cin >> T;
  int t = T;
  while (t--) {
    cin >> S;
    cout << "Case #" << T-t <<": " << getTheLastWord(S) << endl;
  }
  return 0;
}

string getTheLastWord(string &S){
  string t;
  for(string::iterator r = S.begin();r!=S.end();++r){
    if(t.length()==0){
      t.push_back(*r);
    }else if(t[0]>*r){
      t.push_back(*r);
    }else{
      t=*r+t;
    }
  }
  return t;
}
