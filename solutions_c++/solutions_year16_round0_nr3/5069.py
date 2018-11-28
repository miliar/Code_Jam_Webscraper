#include <iostream>
#include <cmath>
#include <map>
#include <vector>
#include <set>

using namespace std;

vector<vector<unsigned long long> > pows;

int N, J;
vector<string> jc;
vector<vector<unsigned long long> > divs;

void precompute_pows() {
  for (unsigned long long i = 2; i <= 10; i++) {
    vector<unsigned long long> cur;
    unsigned long long x = 1;
    for (int j = 0; j <= N; j++) {
      cur.push_back(x);
      x *= i;
    }
    pows.push_back(cur);

    /*for (int j = 0; j < cur.size(); j++) {
      cout << cur[j] << " ";
    }
    cout << endl;*/
  }
}

unsigned long long check_prime(unsigned long long x) {
  if (x <= 1) return 0;
  for (int i = 2; i * i <= x; i++) {
    if (x % i == 0) {
      return i; // non-prime number
    }
  }
  return 0; // prime
}

unsigned long long to_radix(unsigned long long x, int radix) {
  unsigned long long res = 0;
  int idx = 0;
  while (x > 0) {
    res += (x & 1) * pows[radix - 2][idx++];
    x >>= 1;
  }
  return res;
}

//bool ok(unsigned long long x, vector<unsigned long long> &res) {
bool ok(unsigned long long x, vector<unsigned long long> &res) {
  for (int i = 2; i <= 10; i++) {
    //cout << "radix:" << i << endl;
    unsigned long long cur = to_radix(x, i);
    int ret = check_prime(cur);
    if (ret == 0) { // prime
      return false;
    }
    //cout << " ret:" << ret << endl;
    res.push_back(ret);
  }
  //cout << "res.size():" << res.size() << endl;
  return true;
}

string tostr(unsigned long long x) {
  //cout << "tostr..";
  string ret = "";
  while (x > 0) {
    ret = char(48 + (x % 2)) + ret;
    x /= 2;
  }
  //cout << "finish tostr...";
  return ret;
}

unsigned long long get_N(unsigned long long N) {
  unsigned long long p1 = N / 2;
  unsigned long long p2 = N - p1;
  unsigned long long  res = 1 << p1;
  res = res << p2;
  return res;
}

void search() {
  int limit = 1 << (N - 2);
  for (unsigned long long xx = 0; xx < limit; xx++) {
    unsigned long long x = xx;
    x <<= 1;
    x |= 1;
    x |= get_N(N - 1);
      //cout << "checking:" << x << endl;
    vector<unsigned long long> res;
    //int res[9];
    if (ok(x, res)) {
      //cout << "found: " << x << endl;
      string s_tmp = tostr(x);
      jc.push_back(s_tmp);
      divs.push_back(res);
      if (divs.size() == J) {
        return;
      }
    }
  }
}

int main() {
  int NT;
  cin >> NT;
  for (int nt = 0; nt < NT; nt++) {
    cin >> N >> J;

    precompute_pows();

    search();

    cout << "Case #" << (nt + 1) << ":" << endl;
    for (int i = 0; i < J; i++) {
      cout << jc[i];
      for (int j = 0; j < 9; j++) {
        cout << " " << divs[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}
