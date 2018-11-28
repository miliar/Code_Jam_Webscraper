#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

void print_p(int* p, int n) {
  for (int i = 0; i < n; ++i) cout << p[i] << " ";
  cout << "\n";
}

void solve() {
  int n;
  int p[26];
  int sum = 0;

  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> p[i];
    sum += p[i];
  }

  string resp = "";
  while (sum > 0) {

    int max = 0;  
    for (int i = 0; i < n; ++i) {
      if (p[i] > p[max]) max = i;
    }

    resp += (char)(max + 'A');
    --p[max];
    --sum;

    if (sum % 2 == 0) {
      resp += " ";
      continue;
    }

    max = 0;
    for (int i = 0; i < n; ++i) {
      if (p[i] > p[max]) max = i;
    }

    resp += (char)(max + 'A');
    --p[max];
    --sum;

    resp += " ";
  }

  cout << resp;
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve(); 
    cout << "\n";
  }
}