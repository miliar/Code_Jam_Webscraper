#include<iostream>
#include <vector>
using namespace std;

int main(){

  int t;
  cin >>t;

  for(int cas = 0; cas < t; cas++){
    string s;
    cin >> s;
    vector<int> lets(100,0);
    for(int i = 0; i < s.length(); i++){
      lets[s[i]] ++;
    }
    vector<int> count(10,0);
    count[0] = lets['Z'];
    lets['Z'] -= count[0];
    lets['E'] -= count[0];
    lets['R'] -= count[0];
    lets['O'] -= count[0];
    count[2] = lets['W'];
    lets['T'] -= count[2];
    lets['W'] -= count[2];
    lets['O'] -= count[2];
    count[4] = lets['U'];
    lets['F'] -= count[4];
    lets['O'] -= count[4];
    lets['U'] -= count[4];
    lets['R'] -= count[4];
    count[6] = lets['X'];
    lets['S'] -= count[6];
    lets['I'] -= count[6];
    lets['X'] -= count[6];
    count[8] = lets['G'];
    lets['E'] -= count[8];
    lets['I'] -= count[8];
    lets['G'] -= count[8];
    lets['H'] -= count[8];
    lets['T'] -= count[8];
    count[1] = lets['O'];
    lets['O'] -= count[1];
    lets['N'] -= count[1];
    lets['E'] -= count[1];
    count[5] = lets['F'];
    lets['F'] -= count[5];
    lets['I'] -= count[5];
    lets['V'] -= count[5];
    lets['E'] -= count[5];
    count[7] = lets['V'];
    lets['S'] -= count[7];
    lets['E'] -= count[7];
    lets['V'] -= count[7];
    lets['E'] -= count[7];
    lets['N'] -= count[7];
    count[3] = lets['H'];
    lets['T'] -= count[3];
    lets['H'] -= count[3];
    lets['R'] -= count[3];
    lets['E'] -= count[3];
    lets['E'] -= count[3];
    count[9] = lets['I'];
    lets['N'] -= count[9];
    lets['I'] -= count[9];
    lets['N'] -= count[9];
    lets['E'] -= count[9];
    cout << "Case #" << (cas+1) << ": ";
    for(int i = 0; i < 10; i++){
      for(int j = 0; j < count[i]; j++){
        cout << i;
      }
    }
    cout << endl;
  }
  return 0;
}
