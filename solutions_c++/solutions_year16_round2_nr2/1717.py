#include<iostream>
#include<unordered_map>
#include<vector>


using namespace std;

void inc(string& i) {
  for(int a = i.length() - 1; a >= 0; --a) {
    if(i[a] != '9') {
      i[a]++;
      return;
    } else {
      i[a] = '0';
    }
  }
  i[0] = '1';
  i.push_back('0');
}

bool check(string& s1, string& s2) {
  for(int i = 0 ; i < s1.length(); ++i) {
    if(s2[i] == '?') continue;
    if(s2[i] != s1[i]) return false;
  }
  return true;
}

string solve(string input , string input2) {
  int len = input.length();
  int minDiff = INT_MAX;
  string result1;
  string result2;
  //cout<<len<<endl;
  string start(len, '0');
  //cout<<start<<endl;
  for(string i = start; i.length() < len + 1; inc(i)) {
    //cout<<i<<endl;
    if(!check(i, input)) continue;
    for(string b = start; b.length() < len + 1; inc(b)) {
      if(!check(b, input2)) continue;
      if(minDiff > abs(stoi(i,NULL) - stoi(b, NULL))) {
        minDiff = abs(stoi(i,NULL) - stoi(b, NULL));
        result1 = i;
        result2 = b;
      }
    }
  }
  return result1 + " " + result2;
}


int main() {
  int T;
  cin >> T;
  for(int t=0;t < T; ++t) {

    string input;
    string input2;
    cin >> input >> input2;
    string result = solve(input, input2);
    cout<<"Case #" << t + 1 << ": " << result <<endl;
  }
}
