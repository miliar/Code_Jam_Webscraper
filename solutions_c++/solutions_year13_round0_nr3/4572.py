#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<cstring>
#include<cstdlib>

using namespace std;

void find(double, double);
bool ispal(int);

int main(int argv, char **argc) {
  double t;
  vector<string> board;

  cin >> t;

  for (int i = 0; i < t; ++i) {
    double a, b;
    cin >> a;
    cin >> b;
    cout << "Case #" << i + 1 << ": ";
    find(a, b);
  }

  return 0;
}

void find(double a, double b) {
  double s = sqrt(a);
  double e = sqrt(b);
  int count = 0;

  int start = (int) s;
  if (start < s) start++;
  int end = (int) e;
  for (int i = start; i <= end; ++i) {
    if (ispal(i) && ispal(i*i)) {
      count++;
    }
  }

  cout << count << endl;
}

bool ispal(int x) {
  string s;
  int y = x ;
  while (y > 0) {
    s.push_back(48 + y%10);
    y = y/10;
  }

  int i = 0; 
  int j = s.size() -1;
  while (i <= j) {
    if (s[i] != s[j]) {
      return false;
    }
    i++;
    j--;
  }

  return true;
}
