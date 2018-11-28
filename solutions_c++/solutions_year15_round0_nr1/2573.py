#include <iostream>
#include <cassert>

using namespace std;

void solve(const int index, const string& list) {
   int num, accum = 0, add = 0;
   for (int i = 0; i < list.size(); ++i) {
      num = (int)(list[i]) - 48;
      if (!num) continue;
      if (accum < i) {
         add += i - accum;
         accum = i;
      }
      accum += num;
   }
   cout << "Case #" << (1 + index) << ": " << add << endl;
}

int main() {
   // parse N, number of cases
   int N; cin >> N; if (N <= 0) return 0;
   string* list = new string[N];
   // parse Si, max shyness, and the array of shyness of audiences
   for (int i = 0; i < N; ++i) {
      int temp; cin >> temp >> list[i];
      assert ((1 + temp) == list[i].size());
   }
   // solve each cases
   for (int i = 0; i < N; ++i) solve(i, list[i]);
   return 0;
}

