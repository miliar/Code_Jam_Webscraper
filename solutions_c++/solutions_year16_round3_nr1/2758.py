#include <iostream>
#include <vector>

using namespace std;

int findMax(vector<int>& data) {
   int x = 0;
   for (int i = 0; i < data.size(); ++i)
      if (data[i] > data[x]) x = i;
   return x;
}

void check(vector<int>& data) {
   int count = 0;
   for (int i = 0; i < data.size(); ++i) count += data[i];
   for (int i = 0; i < data.size(); ++i)
      if (count < (2 * data[i])) cout << "ERR @ i = " << data[i] << ", count = " << count << endl;
}

void solve(vector<int> data) {
   int count = 0;
   for (int i = 0; i < data.size(); ++i) count += data[i];
   while (count > 2) {
      int i, x = findMax(data); --count; --data[x];
      for (i = 0; i < data.size(); ++i) if (count < (2 * data[i])) break;
      if (i < data.size()) {
         --count; --data[i];
         cout << " " << (char)('A' + x) << (char)('A' + i);
      }
      else cout << " " << (char)('A' + x);
      check(data);
   }
   cout << " ";
   for (int i = 0; i < data.size(); ++i)
      if (data[i]) cout << (char)('A' + i);
}

int main() {
   int T; cin >> T;
   for (int i = 1; i <= T; ++i) {
      int N; cin >> N;
      vector<int> data(N, 0);
      for (int j = 0; j < N; ++j) cin >> data[j];
      cout << "Case #" << i << ":";
      solve(data);
      cout << endl;
   }
   return 0;
}

