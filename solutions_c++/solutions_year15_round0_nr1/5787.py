#include <iostream>
#include <sstream>

#include <cstring>
#include <cstdint>

using namespace std;

uint32_t audience[1001];

int main(int, char**)
{
  string s;
  uint32_t T = 0;
  getline(cin, s);
  stringstream ts(s);
  ts >> T;

  for (uint32_t t = 1; t <= T; t++) {
    string s1, s2;
    uint32_t friends = 0;
    uint32_t standing = 0;
    uint32_t S = 0;
    
    getline(cin, s1, ' ');
    getline(cin, s2);
    stringstream ss(s1);
    ss >> S;
    
    for (uint32_t i = 0; i <= S; i++) {
      audience[i] = ((uint32_t) s2.at(i)) - 48;
    }

    for (uint32_t i = 0; i <= S; i++) {
      if (audience[i] > 0) {
	if (standing >= i) {
	  standing += audience[i];
	}
	else {
	  uint32_t diff = i - standing;
	  friends += diff;
	  standing += (diff + audience[i]);
	}
      }
    }

    cout << "Case #" << t << ": " << friends << endl;
  }

  return 0;
}
