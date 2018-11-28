#include<iostream>
using namespace std;

int dig[10];

bool check(){
  for (int i = 0; i < 10; i++) {
    if (dig[i] == 0) return false;
  }
  return true;
} 

void save(int N) {
  while (N) {
    dig[N % 10]++;
    N /= 10;
  }
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    memset(dig, 0, sizeof(dig));
    long long N;
    cin >> N;
    if (N == 0) {
      cout << "Case #" << i + 1 << ": INSOMNIA\n"; 
      continue;
    }
    long long temp = N;
    while (true) {
      save(temp);
      if (check()) break;
      temp = temp + N;
    }
    cout << "Case #" << i + 1 << ": " << temp << endl;
  }
}
