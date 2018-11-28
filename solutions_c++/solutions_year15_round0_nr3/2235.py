#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool isneg(string a) {
  return a[0] == '-';
}

bool ispos(string a) {
  return !isneg(a);
}

string rmsign(string a) {
  if(ispos(a)) return a;
  else return a.substr(1);
}

string qprod(string a, string b) {
  bool negative = ((isneg(a) && ispos(b)) ||
                   (ispos(a) && isneg(b)));

  a = rmsign(a);
  b = rmsign(b);

  string res;

  if     (a == "1" && b == "1") res = "1";
  else if(a == "1" && b == "i") res = "i";
  else if(a == "1" && b == "j") res = "j";
  else if(a == "1" && b == "k") res = "k";

  else if(a == "i" && b == "1") res = "i";
  else if(a == "i" && b == "i") res = "-1";
  else if(a == "i" && b == "j") res = "k";
  else if(a == "i" && b == "k") res = "-j";

  else if(a == "j" && b == "1") res = "j";
  else if(a == "j" && b == "i") res = "-k";
  else if(a == "j" && b == "j") res = "-1";
  else if(a == "j" && b == "k") res = "i";

  else if(a == "k" && b == "1") res = "k";
  else if(a == "k" && b == "i") res = "j";
  else if(a == "k" && b == "j") res = "-i";
  else if(a == "k" && b == "k") res = "-1";

  if(negative) {
    if(isneg(res)) {
      res = rmsign(res);
    } else {
      res = "-" + res;
    }
  }

  return res;
}

bool solve(long long L, long long X, const string &chars) {
  if(X > 16) X = 16 + (X % 4);

  string real_chars;
  for(long long i = 0; i < X; i++) {
    real_chars += chars;
  }

  if(real_chars.length() < 3) return false;

  // cout << real_chars << endl;

  vector<string> left_qprods(real_chars.length());
  left_qprods[0] = real_chars.substr(0, 1);
  for(long long i = 1; i < real_chars.length(); i++) {
    string a = left_qprods[i - 1];
    string b = real_chars.substr(i, 1);
    left_qprods[i] = qprod(a, b);
  }

  vector<string> right_qprods(real_chars.length());
  right_qprods[real_chars.length() - 1] =
    real_chars.substr(real_chars.length() - 1, 1);
  for(long long i = real_chars.length() - 2; i >= 0; i--) {
    string a = real_chars.substr(i, 1);
    string b = right_qprods[i + 1];
    right_qprods[i] = qprod(a, b);

    // cout << "a: " << a << "; b: " << b << "; prod: " << qprod(a, b) << endl;
  }

  // cout << "left_qprods: ";
  // for(auto s : left_qprods) cout << s;
  // cout << endl;
  //
  // cout << "right_qprods: ";
  // for(auto s : right_qprods) cout << s;
  // cout << endl;

  for(long long i = 0; i < real_chars.length() - 2; i++) {
    if(left_qprods[i] == "i" && right_qprods[i + 1] == "i") {
      // cout << "found i candidate at " << i << endl;
      for(long long j = real_chars.length() - 1; j > i + 1; j--) {
        if(right_qprods[j] == "k") {
          // cout << "found k candidate at " << j << endl;
          string prod = real_chars.substr(i + 1, 1);
          for(long long k = i + 2; k < j; k++) {
            prod = qprod(prod, real_chars.substr(k, 1));
          }
          // cout << "product between (" << i << ", " << j << "): "
          //      << prod << endl;
          if(prod == "j") return true;
        }
      }
    }
  }

  return false;
}

int main() {
  long long T;
  cin >> T;

  for(long long t = 1; t <= T; t++) {
    long long L, X;
    cin >> L >> X;

    string chars;
    cin >> chars;

    bool sol = solve(L, X, chars);

    cout << "Case #" << t << ": " << (sol ? "YES" : "NO") << endl;
  }

  return 0;
}
