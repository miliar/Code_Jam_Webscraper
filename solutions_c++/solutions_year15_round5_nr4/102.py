#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

typedef long long int64;

const int oo = 0x3f3f3f3f;

inline int GetBit(const int mask, const int bit) {
  return (mask >> bit) & 1;
}

int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int testCount;
    cin >> testCount;
    for (int test = 1; test <= testCount; ++test) {
      int size, powerSize;
      cin >> size;
      vector<int> distinctValues = vector<int>(size);
      for (int i = 0; i < size; ++i)
        cin >> distinctValues[i];
      vector<int> S;
      unordered_map<int, int> powerS;
      size = powerSize = 0;
      for (int i = 0; i < int(distinctValues.size()); ++i) {
        int frequence;
        cin >> frequence;
        powerS[distinctValues[i]] = frequence;
        powerSize += frequence;
      }
      for (; (1 << size) < powerSize; ++size);
      powerS[0]--;
      for (int i = 0; i < int(distinctValues.size()); ++i) {
        int value = distinctValues[i];
        while (powerS[value] > 0) {
          for (int mask = 0; mask < (1 << int(S.size())); ++mask) {
            int sum = 0;
            for (int bit = 0; bit < int(S.size()); ++bit)
              if (GetBit(mask, bit))
                sum += S[bit];
            --powerS[sum + value];
          }
          S.push_back(value);
        }
      }
      cout << "Case #" << test << ":";
      for (int i = 0; i < size; ++i)
        cout << " " << S[i];
      cout << "\n";
    }
    cin.close();
    cout.close();
    return 0;
}
