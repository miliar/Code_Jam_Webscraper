#include <iostream>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
  int aux;
  int T, N;
  string s;
  vector<int> resp;
  map<char, int> ch;

  cin >> T;
  for( int i=0; i<T; i++ ){
    cin >> s;
    cout << "Case #" << i+1 << ": ";

    ch.clear();
    for( int j=0; j<s.size(); j++){
      ch[s[j]]++;
    }

    resp.clear();
    for(int j=0; j < ch['Z']; j++){
      ch['E']--;
      ch['R']--;
      ch['O']--;
      resp.push_back(0);
    }
    for(int j=0; j < ch['W']; j++){
      ch['T']--;
      ch['O']--;
      resp.push_back(2);
    }
    for(int j=0; j<ch['X']; j++){
      ch['S']--;
      ch['I']--;
      resp.push_back(6);
    }
    for(int j=0; j<ch['U']; j++){
      ch['F']--;
      ch['O']--;
      ch['R']--;
      resp.push_back(4);
    }
    for(int j=0; j<ch['F']; j++){
      ch['I']--;
      ch['V']--;
      ch['E']--;
      resp.push_back(5);
    }
    for(int j=0; j<ch['V']; j++){
      ch['S']--;
      ch['E']--;
      ch['E']--;
      ch['N']--;
      resp.push_back(7);
    }
    for(int j=0; j<ch['G']; j++){
      ch['E']--;
      ch['I']--;
      ch['H']--;
      ch['T']--;
      resp.push_back(8);
    }
    for(int j=0; j<ch['H']; j++){
      ch['T']--;
      ch['R']--;
      ch['E']--;
      resp.push_back(3);
    }
    for(int j=0; j<ch['I']; j++){
      ch['N']--;
      ch['N']--;
      ch['E']--;
      resp.push_back(9);
    }
    for(int j=0; j<ch['O']; j++){
      resp.push_back(1);
    }
    sort(resp.begin(),resp.end());
    for(int j=0; j<resp.size(); j++){
      cout << resp[j];
    }
    cout<<endl;
  }
  return 0;
}
