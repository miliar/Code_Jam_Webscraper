#include <bits/stdc++.h>
using namespace std;

void count_digits(long long n, vector<int>& counter) {
  for (; n>0; n/=10) ++counter[n%10];
}

bool check_digits(const vector<int>& counter) {
  for (auto& c : counter)
    if (!c) return false;
  return true;
}

void calc(long long N, int t) {
  long long n = N;
  vector<int> counter(10);
  
  for (;; n+=N) {
    count_digits(n, counter);
    if (check_digits(counter)) break;
  }

  printf("Case #%d: %lld\n", t, n);
}

void solve(int t) {
  long long N;
  cin >> N;
  if (!N)
    printf("Case #%d: INSOMNIA\n", t);
  else
    calc(N, t);
}

int main(void) {
	int T; cin >> T;
  for (int t=1; t<=T; t++) solve(t);  
}
