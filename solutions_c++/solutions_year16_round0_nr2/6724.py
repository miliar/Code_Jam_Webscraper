// Revenge of the Pancakes
#include <vector>
#include <iostream>

using std::string;
using std::vector;
using std::endl;
using std::cin;
using std::cout;

char flipChar(char &c){
  if(c == '-'){
    return c = '+';
  }
  else{
    return c = '-';
  }
}

// flip string s, n char from the left
// n starts at 0
void flip(string &s, int n){
    char temp;
    for(int i = 0; i < (n+1)/2; i++){

        temp = s[i];
        s[i] = flipChar(s[n - i]);
        s[n-i] = flipChar(temp);

    }
    if((n+1)%2==1){
      s[n/2] = flipChar(s[n/2]);
    }
}

bool correct(string s){
  for(int i = 0; i < s.size(); i++){
    if(s[i] == '-'){
      return false;
    }
  }
  return true;
}

int logic(string &s, int flips){
  if(correct(s)){
    return flips;
  }

  if(s.size() == 1){
    flip(s,0);
    flips++;
    return logic(s,1);
  }
  //cout<<s<<endl;    ///
  for(int i = 1; i < s.size(); i++){
    if(s[0] != s[i]){
      flip(s,i-1);
      flips++;
      return logic(s,flips);
    }
  }
  flip(s,s.size()-1);
  flips++;
  return logic(s,flips);
}

vector<int> runTest(vector<string> vec){
  vector<int> ans;
  for(string s : vec){
    ans.push_back(logic(s,0));
  }
  return ans;
}


int main(int argc, char** argv){
  int s;
  string tests;
  cin >> s;
  vector<string> testVec;
  for(int i = 0; i < s; i++){
    cin >> tests;
    testVec.push_back(tests);
  }

  vector<int> ans = runTest(testVec);
  for(int i = 0; i < ans.size(); i++){
    cout<<"Case #" << i+1 << ": "<<ans[i]<<endl;
  }
  return 0;
}
