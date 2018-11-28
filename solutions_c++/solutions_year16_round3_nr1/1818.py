#include<iostream>
#include<unordered_map>
#include<vector>


using namespace std;

bool isValid(vector<int> &pi) {
  int size = pi.size();
  int sum = 0;
  for(int i = 0; i < size; ++i) {
    sum += pi[i];
  }
  for(int i = 0; i < size; ++i) {
    if(pi[i] * 2 > sum) {
      return false;
    }
  }

  return true;
}

/*
void trim1(string& str)
{
  string::size_type pos1 = str.find_first_not_of(' ');
  string::size_type pos2 = str.find_last_not_of(' ');
  str = str.substr(pos1 == string::npos ? 0 : pos1, 
    pos2 == string::npos ? str.length() - 1 : pos2 - pos1 + 1);
}
*/
string solve(vector<int> &pi) {
  int size = pi.size();
  string result;
  while(1) {
    int top1_idx = -1;
    int top2_idx = -1;

    for(int i = 0; i < size; ++i) {
      if(pi[i] == 0) continue;
      if(top1_idx == -1) {
        top1_idx = i;
        continue;
      }
      if(pi[top1_idx] <= pi[i]) {
        top2_idx = top1_idx;
        top1_idx = i;
      }
    }
    if(top1_idx == -1) {
      break;
    }
    //cout<<top1_idx << " " << top2_idx<< endl;

    pi[top1_idx]--;
    if(isValid(pi) ) {
      result.push_back('A' + top1_idx);
      result.push_back(' ');
      continue;
    }
    pi[top2_idx]--;
    if(isValid(pi)) {
      result.push_back('A' + top1_idx);
      result.push_back('A' + top2_idx);
      result.push_back(' ');
    } else {
      cout<<"Bug"<<endl;
    }
  }
  result.pop_back();
  return result;
}

int main() {
  int T;
  cin >> T;
  for(int t=0;t < T; ++t) {

    int N;
    vector<int> Pi;
    cin >> N;
    for(int i = 0; i < N; ++i) {
      int t = 0;
      cin >> t;
      Pi.push_back(t);
    }
    string result = solve(Pi);
    cout<<"Case #" << t + 1 << ": " << result <<endl;
  }
}
