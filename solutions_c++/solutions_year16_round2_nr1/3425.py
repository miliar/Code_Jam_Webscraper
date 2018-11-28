#include<iostream>
#include<unordered_map>
#include<vector>


using namespace std;

vector<string>tab2;
bool check(string& s, vector<int> &t) {
  for(auto c : s) {
    if(t[c - 'A'] <= 0) {
      return false;
    }
  }
  for(auto c : s) {
    t[c-'A']--;
  }
  return true;
}

bool check2(vector<int> &t) {
  for(int i =0 ; i < 26; ++i) {
    if(t[i] != 0) {
      //cout<<"Bug!!"<<endl;
      return false;
    }
  }
  return true;
}
void recover( string& s, vector<int> &t) {
  for(auto c: s) {
    t[c - 'A']++;
  }
}

string helper(int start, vector<int> &tab) {
  for(int i = start; i <= 9; ++i) {
    if(check(tab2[i], tab) ) {
      string subResult = helper(i, tab);
      if(check2(tab)){
        return to_string(i) + subResult;
      }else {
        recover(tab2[i], tab);
      }

    }
  }
  return "";
}

string solve(string input) {
  vector<int> tab(26, 0);
  for(auto a : input) {
    tab[a-'A']++;
  }
  return helper(0, tab);
}

void initTab2(){
  tab2.push_back("ZERO");
  tab2.push_back("ONE");
  tab2.push_back("TWO");
  tab2.push_back("THREE");
  tab2.push_back("FOUR");
  tab2.push_back("FIVE");
  tab2.push_back("SIX");
  tab2.push_back("SEVEN");
  tab2.push_back("EIGHT");
  tab2.push_back("NINE");
}

int main() {
  int T;
  cin >> T;
  initTab2();
  for(int t=0;t < T; ++t) {

    string input;
    cin >> input;
    string result = solve(input);
    cout<<"Case #" << t + 1 << ": " << result <<endl;
  }
}
