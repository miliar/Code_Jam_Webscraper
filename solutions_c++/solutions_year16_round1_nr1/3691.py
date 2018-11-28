//The last Word

#include <vector>
#include <iostream>

using std::string;
using std::vector;
using std::endl;
using std::cin;
using std::cout;

void placeFront(string &s, char c){
  s.insert(s.begin(), c);
  return;
}

void placeBack(string &s, char c){
  s.insert(s.end(), c);
  return;
}

string logic(string s){
  string ans;
  ans.push_back(s[0]);
  if(s.size() == 1){
    return ans;
  }
  for(int i = 1; i < s.size(); i++){
    if(ans[0] > s[i]){
      placeBack(ans, s[i]);
    }
    else{
      placeFront(ans, s[i]);
    }
  }
  return ans;
}

vector<string> runTest(vector<string> vec){
  vector<string> ans;
  for(string s : vec){
    ans.push_back(logic(s));
  }
  return ans;
}

int main(int argc, char** argv){
  int numTests;
  string tests;
  cin >> numTests;
  vector<string> testVec;
  for(int i = 0; i < numTests; i++){
    cin >>tests;
    testVec.push_back(tests);
  }

  vector<string> ans = runTest(testVec);
  for(int i = 0; i < ans.size(); i++){
    cout<<"Case #" << i+1 << ": "<<ans[i]<<endl;
  }
  return 0;
}
