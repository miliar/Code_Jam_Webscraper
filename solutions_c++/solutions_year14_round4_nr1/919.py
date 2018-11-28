/*
ID: Plagapong
LANG: C++
TASK: A
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#define INF 999999999

using namespace std;
int n, s[1000], disc;

void preprocess() {
  // Preprocess
  
}

void clearVars() {
  // Clear variables
  for (int i = 0; i < 1000; i++) s[i] = 0;
}

void process() {
  // Code here!
  cin >> n >> disc;
  for (int i = 0; i < n; i++) cin >> s[i];
  sort(s, s + n);
  //for (int i = 0; i < n; i++) cout << s[i] << " ";
  int cnt = 0;
  for (int i = n-1; i >= 0; i--) {
    if (s[i] != 0) {
      // Find the best pairing thing
      for (int j = i-1; j >= 0; j--) {
        if (s[j] != 0 && s[j] <= disc - s[i]) {
          s[j] = 0;
          break;
        }
      }
      s[i] = 0;
      cnt++;
    }
  }
  cout << cnt;
}

int main() {
  preprocess();
  int times;
  cin >> times;
  for (int i = 1; i <= times; i++) {
	cout << "Case #" << i << ": ";
	clearVars();
	process();
	cout << endl;
  }
  return 0;
}
