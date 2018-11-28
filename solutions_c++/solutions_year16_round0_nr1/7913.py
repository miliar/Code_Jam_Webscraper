#include<iostream>
#include<cstdio>
using namespace std;

int cnt[15] = {0};

bool check(long long n) {
  while ( n ) {
    cnt[n % 10] = 1;
    n /= 10;
  }
  for ( int i = 0 ; i < 10 ; i++ ) {
    if ( !cnt[i] ) return false;
  }
  return true;
}

int mx = 0;

int solve(long long num) {
  memset(cnt, 0, sizeof(cnt));
  int res = 1;
  long long n = num;
  while ( !check(n)  ) {
    if ( res == 100 ) return -1;
    if ( num) mx = max(mx, res);
    res++;
    n += num;
    //printf("n = %lld\n", n);
  }
  return n;
}

int main() {
  //freopen("input1.txt", "r", stdin);
  //freopen("output1.txt", "w", stdout);
  int T, kase = 1;

  cin >> T;
  while ( T-- ) {
  //for ( int i = 0 ; i <= 201 ; i++ ) {
    long long n;
    cin >> n;
    //n = i;
    int res = solve(n);
    if ( res == -1 ) cout << "Case #" << kase++ << ": " << "INSOMNIA" << endl;
    else cout << "Case #" << kase++ << ": " << res << endl;
  }
  //cout << "mx : " << mx << endl;

  return 0;
}
