#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int quat[4][4] = {{1, 2, 3, 4},
                {2, -1, 4, -3},
                {3, -4, -1, 2},
                {4, 3, -2, -1}};

int signum(int n) {
  return (n<0?-1:1);
}

string code(int n) {
  if (abs(n) == 1) {
    return to_string(n);
  }
  string r = (n<0 ? "-":"");
  if (n==2) {
    r+='i';
  } else if (n==3) {
    r+='j';

  } else {
    r+='k';

  }
  return r;
}

int multiply(string str) {
  // cout << "multiply " << str << "\n";
  int r=1;
  for (int i=0; i<int(str.length()); i++) {
    r = signum(r) * quat[abs(r)-1][int(str[i]) + 1 - 'i'];
  }
  return r;
}

int multiply(int l, int r) {
  //cout << "l*r " << code(l) << ", " << code(r) << " : " << code(signum(l)*signum(r)*quat[abs(l)-1][abs(r)-1]) << "\n";
  return signum(l)*signum(r)*quat[abs(l)-1][abs(r)-1];
}



bool solve(string str){
  int total = multiply(str);
  string left="", middle, right="";
  int left_i, right_i, middle_i;
  //cout << "total " << code(total) << "\n";

  left_i = 1;

  middle_i = total;
  for (int l=0; l<int(str.length()); l++) {
    right_i = 1;

    //middle_i = -1*multiply(str[l]-'i'+2, middle_i);

    left_i = multiply(left_i, str[l]-'i'+2);
    middle_i = -1*multiply(left_i, total);

    //cout << "left_i " << code(left_i) << "\n";
    //cout << "temp middle_i " << code(middle_i) << "\n\n";

    if (left_i == 2) {
      //cout << "l " << l << "\n";
      //cout << "left_i " << left_i << "\n";
      //cout << "*left_i " << code(left_i) << "\n";
      //cout << "*temp middle_i " << code(middle_i) << "\n";

      for (int r=str.length()-1; r>l+1; r--) {

        right_i = multiply(str[r]-'i'+2, right_i);
        middle_i = -1*multiply(middle_i, str[r]-'i'+2);
        //cout << "r " << r << "\n";
        //cout << "middle_i " << code(middle_i) << "\n";
        //cout << "right_i " << code(right_i) << "\n";

        if (right_i == 4 &&
            middle_i == 3) {
          return true;
        }
      }
    }
  }
  return false;
}

int main() {
  vector<string> result;

  int X, L, T;
  string str_diff;

  cin >> T;

  for (int t=0; t<T; t++) {
    cin >> L >> X >> str_diff;

    string str = "";
    for (int i=0; i<X; i++) {
      str+=str_diff;
    }
    //cout << "string " << str << "\n";
    if (solve(str)) {
      result.push_back("YES");
    } else {
      result.push_back("NO");
    }
  }

  for (int i=0; i<int(result.size()); i++) {
    cout << "Case #" << i+1 << ": " << result[i] << "\n";
  }
  return 0;
}
