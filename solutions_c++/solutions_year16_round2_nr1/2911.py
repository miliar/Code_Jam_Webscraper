#include<iostream>
#include<string>
#include<map>
using namespace std;
int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    string s;
    cin >> s;
    //cout << s;
    int dig[10] = {0};
    map<char, int> nmap;
    for(int j = 0; j < s.length(); j++) {
        if ( nmap.find(s[j]) != nmap.end()) {
            nmap[s[j]] += 1;
        }
        else {
            nmap[s[j]] = 1;
        }
    }


    if (nmap.find('Z') != nmap.end() && nmap['Z'] > 0) {
        dig[0] = nmap['Z'];
        nmap['E'] -= dig[0];
        nmap['R'] -= dig[0];
        nmap['O'] -= dig[0];
    }
    if (nmap.find('X') != nmap.end() && nmap['X'] > 0) {
        dig[6] = nmap['X'];
        nmap['S'] -= dig[6];
        nmap['I'] -= dig[6];

    }
    if (nmap.find('U') != nmap.end() && nmap['U'] > 0) {
        dig[4] = nmap['U'];
        nmap['F'] -= dig[4];
        nmap['O'] -= dig[4];
        nmap['R'] -= dig[4];
    }
    if (nmap.find('W') != nmap.end() && nmap['W'] > 0) {
        dig[2] = nmap['W'];
        nmap['T'] -= dig[2];
        nmap['O'] -= dig[2];
    }
    if (nmap.find('O') != nmap.end() && nmap['O'] > 0) {
        dig[1] = nmap['O'];
        nmap['N'] -= dig[1];
        nmap['E'] -= dig[1];
    }
    if (nmap.find('R') != nmap.end() && nmap['R'] > 0) {
        dig[3] = nmap['R'];
        nmap['T'] -= dig[3];
        nmap['H'] -= dig[3];
        nmap['E'] -= dig[3] * 2;
    }
    if (nmap.find('G') != nmap.end() && nmap['G'] > 0) {
        dig[8] = nmap['G'];
        nmap['E'] -= dig[8];
        nmap['I'] -= dig[8];
        nmap['H'] -= dig[8];
        nmap['T'] -= dig[8];
    }
    if (nmap.find('S') != nmap.end() && nmap['S'] > 0) {
        dig[7] = nmap['S'];
        nmap['E'] -= dig[7] * 2;
        nmap['V'] -= dig[7];
        nmap['N'] -= dig[7];
    }
    if (nmap.find('F') != nmap.end() && nmap['F'] > 0) {
        dig[5] = nmap['F'];
        nmap['I'] -= dig[5];
        nmap['V'] -= dig[5];
        nmap['E'] -= dig[5];
    }
    if (nmap.find('N') != nmap.end() && nmap['N'] > 0) {
    dig[9] = nmap['N']/2;
    }


    //cout<< "0:" << dig[0]<<endl;
    cout << "Case #" << i <<": ";
    for (int k = 0; k < 10; k++) {
        for (int m = 0; m < dig[k]; m++)
            cout <<k;
    }
    cout << endl;

  }
}
