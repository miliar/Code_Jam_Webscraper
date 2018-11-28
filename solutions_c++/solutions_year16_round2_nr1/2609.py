#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int t;
  cin >> t;
  string s;
  getline(cin, s);
  for(int i = 0; i < t; i++) {
    getline(cin, s);
    vector<char> letters;
    istringstream iss(s);
    char c;
    while(iss >> c) {
      letters.push_back(c);
    }
    sort(letters.begin(), letters.end());
    int freqs[26];
    for(int j = 0; j < 26; j++) {
      freqs[j] = 0;
    }
    for(int j = 0; j < letters.size(); j++) {
      freqs[letters[j]-'A']++;
    }
    /*for(int j = 0; j < 26; j++) {
      cerr << freqs[j];
    }
    cerr << endl;*/
    int result[10];
    for(int j = 0; j < 10; j++) {
      result[j] = 0;
    }
    while(freqs[25] != 0) {
      //cerr << 0 << endl;
      freqs[25]--; //z
      freqs[4]--;  //e
      freqs[14]--; //o
      freqs[17]--; //r
      result[0]++;
    }
    while(freqs[14] != 0) {
      if(freqs[22] != 0) {
        //cerr << 2 << endl;
        freqs[19]--; //t
        freqs[14]--;
        freqs[22]--; //w
        result[2]++;
      }else if(freqs[20] != 0) {
        //cerr << 4 << endl;
        freqs[5]--;  //f
        freqs[20]--; //u
        freqs[14]--;
        freqs[17]--;
        result[4]++;
      }else {
        freqs[14]--;
        freqs[13]--;
        freqs[4]--;
        result[1]++;
      }
    }
    while(freqs[17] != 0) {
      //cerr << 3 << endl;
      freqs[17]--;
      freqs[19]--;
      freqs[7]--;
      freqs[4] = freqs[4] - 2;
      result[3]++;
    }
    while(freqs[5] != 0) {
      //cerr << 5 << endl;
      freqs[5]--;
      freqs[21]--; //v
      freqs[4]--;
      freqs[8]--; //i
      result[5]++;
    }
    while(freqs[23] != 0) {
      //cerr << 6 << endl;
      freqs[23]--;
      freqs[8]--;
      freqs[18]--; //s
      result[6]++;
    }
    while(freqs[21] > 0) {
      //cerr << 7 << endl;
      freqs[21]--;
      freqs[18]--;
      freqs[13]--;
      freqs[4] = freqs[4] - 2;
      result[7]++;
    }
    while(freqs[6] != 0) {
      //cerr << 8 << endl;
      freqs[6]--;
      freqs[7]--;
      freqs[8]--;
      freqs[4]--;
      freqs[19]--;
      result[8]++;
    }
    while(freqs[8] > 0) {
      //cerr << 9 << endl;
      freqs[8]--;
      freqs[13] = freqs[13] - 2;
      freqs[4]--;
      result[9]++;
    }
    cout << "Case #" << i+1 << ": ";
    for(int j = 0; j < 10; j++) {
      for(int k = 0; k < result[j]; k++) {
        cout << j;
      }
    }
    cout << endl;
  }
}
