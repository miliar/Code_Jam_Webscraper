#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<limits>
#include<map>
#include<string>

using namespace std;

bool palindrome(int x) {
  if (x < 0) return false;
  int div = 1;
  while (x / div >= 10) {
    div *= 10;
  }        
  while (x != 0) {
    int l = x / div;
    int r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}

int main() {
  int T;
  cin >> T;
  int a[100], n = 0; 
  
  for (int i = 1; i < 32; i++) {
    if (palindrome(i)) {
      if (palindrome(i*i)) {
        a[n] = i*i;
        n++;
      }
    }
  }
  
  for (int i = 0; i < T; i++) {
    int A, B, s = -1, e = -1;
    cin >> A >> B;
    for (int j = 0; j < n; j++) {
      if ((a[j] >= A) && (s == -1)) s = j;
      if (a[j] > B) {
        e = j;
        break;
      }
    }
    int c;
    c = e - s;
    if ((s == 0) && (e == 0)) c = 0;
    if ((s == -1) && (e == -1)) c = 0;
    if ((s != -1) && (e == -1)) c = n - s;
    
    cout << "Case #" << i + 1 << ": " << c << endl;
  }
  return 0;
}


