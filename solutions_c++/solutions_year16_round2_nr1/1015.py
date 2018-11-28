#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

void eliminate(int* counts, int* ar, string val, int ind, int num) {
  int ptr = val[ind]-'A';
  int torem = ar[ptr];
  counts[num] += torem;
  for(int i = 0; i < val.size(); i++) {
    int ptr2 = val[i]-'A';
    ar[ptr2] -= torem;
  }
}

int main() {
  int total_cases;
  cin >> total_cases;

  for(int caseno = 1; caseno <= total_cases; caseno++) {
    string cur;
    int ar[50];
    int counts[10];
    cin >> cur;
    for(int i=  0; i < 50; i++) ar[i] = 0;
    for(int j = 0; j < cur.size(); j++) ar[cur[j]-'A']++;
    for(int i = 0; i < 10; i++) counts[i] = 0;

    eliminate(counts, ar, "ZERO", 0, 0);
    eliminate(counts, ar, "TWO", 1, 2);
    eliminate(counts, ar, "FOUR", 2, 4);
    eliminate(counts, ar, "EIGHT", 2, 8);
    eliminate(counts, ar, "SIX", 2, 6);
    eliminate(counts, ar, "THREE", 1, 3);
    eliminate(counts, ar, "ONE", 0, 1);
    eliminate(counts, ar, "FIVE", 0, 5);
    eliminate(counts, ar, "SEVEN", 2, 7);
    eliminate(counts, ar, "NINE", 1, 9);
    cout << "Case #" << caseno << ": ";
    for(int i = 0; i < 10; i++) {
      for(int j = 0; j < counts[i]; j++) {
	cout << (char)('0'+i);
      }
    }
    cout << endl;
  }
  return 0;
}
