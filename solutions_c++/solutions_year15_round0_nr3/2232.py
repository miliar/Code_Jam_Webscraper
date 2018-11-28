#include <iostream>
#include <cassert>

using namespace std;

// Let I = 1, J = 2, K = 3, and 1 = 0
const pair<char, bool> rule[4][4] = {
   { make_pair(0, 0), make_pair(1, 0), make_pair(2, 0), make_pair(3, 0) },
   { make_pair(1, 0), make_pair(0, 1), make_pair(3, 0), make_pair(2, 1) },
   { make_pair(2, 0), make_pair(3, 1), make_pair(0, 1), make_pair(1, 0) },
   { make_pair(3, 0), make_pair(2, 0), make_pair(1, 1), make_pair(0, 1) }
};

string str(const pair<char, bool>& a) {
   string s = ((1 == a.first) ? "i" : (2 == a.first) ? "j" : (3 == a.first) ? "k" : "1");
   if (a.second) s = "-" + s; return s;
}

string str(const string& a) {
   string s = "";
   for (int i = 0; i < a.size(); ++i)
      s += ((1 == a[i]) ? "i" : (2 == a[i]) ? "j" : (3 == a[i]) ? "k" : "1");
   return s;
}

pair<char, bool>* DB = 0;

bool decodeAll(const string& code, int start, int startX, int X) {
   if (start >= code.size()) { start = 0; ++startX; }
   if (startX >= X) return false;
   pair<char, bool> temp, result;
   if (!DB) {
      //cout << "Code = " << str(code) << endl;
      DB = new pair<char, bool>[code.size()];
      result = make_pair(0, 0);
      for (int i = code.size() - 1; i >= 0; --i) {
         temp = rule[code[i]][result.first];
         result.first = temp.first;
         result.second ^= temp.second;
         DB[i] = result;
         //cout << "DB[" << i << "] = " << str(DB[i]) << endl;
      }
   }
   result = make_pair(0, 0);
   for (int i = startX, j = start; i < X; ++i) {
      temp = rule[result.first][DB[j].first];
      result.first = temp.first;
      result.second ^= (temp.second ^ DB[j].second);
      j = 0;
   }
   return (3 == result.first && !result.second);
}

bool decode(const char& s, const string& code, int start, int startX, int X) {
   //cout << "Code = " << str(code) << ", found(" << (int)(s) << ")" << str(make_pair(s, 0))
   //     << " at (" << start << ", " << startX << ")" << endl;
   if (s == 3) return decodeAll(code, start, startX, X);
   // start from code[start] in the startX copy, find s up to the X copy
   pair<char, bool> temp, result = make_pair(0, 0);
   for (int i = startX, j = start; i < X; ++i) {
      for (; j < code.size(); ++j) {
         //cout << "Prev = " << str(result) << ", code = " << str(make_pair(code[j], 0));
         temp = rule[result.first][code[j]];
         result.first = temp.first;
         result.second ^= temp.second;
         //cout << " Result = " << str(result) << endl;
         if (s == result.first && !result.second) {
            if (decode(s + 1, code, 1 + j, i, X)) return true;
         }
      }
      j = 0;
   }
   return false;
}

void solve(int index, const string& code, int X) {
   if (DB) { delete [] DB; DB = 0; }
   if (decode(1, code, 0, 0, X)) cout << "Case #" << index << ": " << "YES" << endl;
   else cout << "Case #" << index << ": " << "NO" << endl;
}

int main() {
   // parse T
   int T; cin >> T; if (T <= 0) return 0;
   // parse L, X
   for (int i = 0; i < T; ++i) {
      int L, X; cin >> L >> X;
      string code = ""; cin >> code;
      assert (L == code.size());
      for (int j = 0; j < L; ++j)
         code[j] = ('i' == code[j]) ? 1 : ('j' == code[j]) ? 2 : 3;
      solve(1 + i, code, X);
   }
   return 0;
}

