#include<iostream>
#include<string>
#include<vector>

using namespace std;


long long count(long long r, long long t) {
  long long remain = t;
  long long rad = r;
  long long count = 0;  

  while (remain > 0) {
    remain -= 2*r + 1;
    
    if (remain >=0) count++;
    
    r += 2;
  }

  return count;
}

int main(int argv, char **argc) {
  int t;
  vector<string> board;

  cin >> t;

  for (int i = 0; i < t; ++i) {
    long long r;
    long long t;
    cin >> r;
    cin >> t;
    long long n = count(r, t);
    cout << "Case #" << i+1 << ": " << n << endl;
  }

  return 0;
}
