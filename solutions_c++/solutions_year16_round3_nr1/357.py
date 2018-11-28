#include<bits/stdc++.h>

using namespace std;

typedef pair<int, char> pi;
typedef vector<pi> vpi;

int main() {
  int t;
  cin >> t;
  for (int cas = 1; cas <= t; ++cas) {
    int n;
    cin >> n;
    vpi V(n);
    for (int i = 0; i < n; ++i) {
      cin >> V[i].first;
      V[i].second = char('A' + i);
    }
    sort(V.begin(), V.end());
    cout << "Case #" << cas << ":";
    int k = V.size();
    while (V[k - 1].first > V[k - 2].first) {
      --V[k - 1].first;
      cout << ' ' << V[k - 1].second;
    }
    for (int i = 0; i < k - 2; ++i) {
      while (V[i].first) {
	--V[i].first;
	cout << ' ' << V[i].second;
      }
    }
    while (V[k - 1].first) {
      --V[k - 1].first;
      cout << ' ' << V[k - 1].second << V[k - 2].second;
    }
    cout << endl;
  }
}