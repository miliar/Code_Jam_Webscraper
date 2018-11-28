#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <map>
#include <sstream>
#include <string>
// www.boost.org
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/utility/binary.hpp>
#include <unordered_map>
using namespace std;
using namespace boost::multiprecision;

bool canMakeStr(unordered_map<char, int> charCounts, string engRep) {
  for (int i = 0; i < engRep.size(); i++) {
    char ch = engRep[i];
    if (charCounts[ch] == 0) {
      return false;
    }
    charCounts[ch]--;
  }

  return true;
}

void updateCharCounts(unordered_map<char, int> &charCounts, string engRep) {
  for (int i = 0; i < engRep.size(); i++) {
    char ch = engRep[i];
    charCounts[ch]--;
  }
}

void decodeNumber(string coded) {
  int counts[10];
  memset(counts, 0, sizeof(int) * 10);
  const char *engRepsArr[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
  vector<string> engReps(engRepsArr, engRepsArr + 10);
  int safeVisitOrder[10] = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};
  unordered_map<char, int> charCounts;
  for (char ch = 'A'; ch <= 'Z'; ch++) {
    charCounts[ch] = 0;
  }

  for (int i = 0; i < coded.size(); i++) {
    charCounts[coded[i]]++;
  }
  
  for (int i = 0; i < 10; i++) {
    int digit = safeVisitOrder[i];
    string engRep = engReps[digit];

    while (canMakeStr(charCounts, engRep)) {
      updateCharCounts(charCounts, engRep);
      counts[digit]++;
    }
  }

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < counts[i]; j++) {
      cout << i;
    }
  }
}

int main() {
  int t;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; i++) {
    string coded;
    cin >> coded;

    cout << "Case #" << i << ": ";

    decodeNumber(coded);

    cout << endl;
  }
}
