#include <cstdio>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <string>
#include <set>
#include <stack>
#define pb push_back

#define mp make_pair
#define f first
#define s second
#define ll long long

using namespace std;


vector<int> decomp(ll x) {

  vector<int> freq(10, 0);
  while(x > 0) {
    int dig = x % 10;
    freq[dig] += 1;
    x /= 10;
  }
  return freq;
}

void add(vector<int>&ret, const vector<int>&to_add) {
  for (size_t i = 0; i < ret.size(); ++i) {
    ret[i] += to_add[i];
  }
}
bool check(const vector<int>& v) {
  for (int i = 0; i < 10; ++i) {
    if (v[i] == 0) {
      return false;
    }
  }
  return true;
}
vector<ll> preproc() {

  int LIM = 1e6 + 1;
  vector<ll> answer(LIM, 0);
  for (int i = 1; i < LIM; ++i) {

    ll p = i, idx = 1;
    vector<int> digs = decomp(i);
    while(!check(digs)) {
      idx++;
      p = i * idx;
      add(digs, decomp(p));
    }
    answer[i] = p;
  }

  return answer;
}
int main() {
  ifstream cin("test.in");
  ofstream cout("test.out");

  vector<ll> answer = preproc();
  int T; cin >> T;

  for (int tc = 1; tc <= T; ++tc) {
    int N; cin >> N;
    if (N == 0) {
      cout << "Case #" << tc << ": " << "INSOMNIA" << "\n";
    } else {
      cout << "Case #" << tc << ": " << answer[N] << "\n";
    }
  }

  return 0;
}
