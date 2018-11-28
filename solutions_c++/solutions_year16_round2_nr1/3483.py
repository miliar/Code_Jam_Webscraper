#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 100030;    // Change as necessary
const ll  MODD = 1000000009; //

const string let[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int curr[3000];

bool f(int amt[],int tot,int lvl){
  if(tot == 0){
    for(int i=0;i<lvl;i++)
      cout << curr[i];
    cout << endl;
    return true;
  }
  
  for(int i=(lvl ? curr[lvl-1] : 0);i<10;i++){
    bool okay = true;
    for(int j=0;j<let[i].size();j++)
      if(--amt[let[i][j]-'A'] < 0)
        okay = false;
    curr[lvl] = i;
    if(okay)
      if(f(amt,tot-let[i].size(),lvl+1))
        return true;
    for(int j=0;j<let[i].size();j++)
      ++amt[let[i][j]-'A'];
  }
  return false;
}

void do_case(){
  string s; cin >> s;
  int amt[26] = {0};
  for(int i=0;i<s.length();i++)
    amt[s[i]-'A']++;
  f(amt,s.length(),0);
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  
  int T,C=1; cin >> T;
  
  while(T--){
    cout << "Case #" << C++ << ": ";
    do_case();
  }
  
  return 0;
}
