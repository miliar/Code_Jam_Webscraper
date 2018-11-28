#include <bits/stdc++.h>
using namespace std;

const int L = (1 << 27);
int B[L/32+1];
vector<int> primes;

void getPrimes() {
  int i, j;
  for (i = 2; i < L; ++i) {
    if (B[i >> 5] & (1 << (i % 32)))
      continue;
    primes.push_back(i);
    if (i < L / i)
      for (j = i * i; j < L; j += i)
        B[j >> 5] |= (1 << (j % 32));  
  }
}

int notPrime(const long long& n) {
  for (auto& p : primes) {
    if (p >= n) break;
    else if (n % p == 0) return p;
  }
  return -1;
}

bool check(const vector<int>& bin, vector<int>& res) {
  for (int base=2; base<=10; base++) {
    long long p = 1LL, v=0LL;

    for (int i=0; i<bin.size(); i++) {
      v += p * bin[i];
      p *= base;
    }

    int prime = notPrime(v);
    if (prime == -1 ) return false;
    res[base] = prime;
  }
  return true;
}

int ans16[50][11];
void solve16(int J) {
  int sol_nr = 0;
  cout << "Case #1:\n";
  for (int i=0; i<(1<<14); i++) {
    vector<int> bin(16), res(11);
    int v = 1 + i + (1<<15);
    for (int q=i, j=1; q>0; q>>=1, ++j)
      if (q&1) bin[j]=1;

    bin[0] = bin[15] = 1;
    if (check(bin, res)) {
      ans16[sol_nr][0] = v;
      for (int j=15; j>=0; --j) cout<<bin[j]; cout<<" ";
      //cout << "Sol[" << sol_nr << "]=" << v << endl;
      for (int j=2; j<=10; j++) {
        ans16[sol_nr][j]=res[j];  
        cout << res[j] << " ";
      }
      cout << endl;
      ++sol_nr;  
    }
    if (sol_nr == J) break;
  }
}


void solve(int t) {
  int N, J;
  cin >> N >> J;
  if (N==16)
    solve16(J);
}

int main(void) {
  // setup
  getPrimes();

	int T; cin >> T;
  for (int t=1; t<=T; t++) solve(t);  
}
