#include <iostream>
#include <fstream>
#include <unordered_map>

using namespace std;

const int one = 1;
const int I = 2;
const int J = 3;
const int K = 4;

const int table[][4] = {
    {one,  I,  J,  K},
    {I, -one,  K, -J},
    {J, -K, -one,  I},
    {K,  J, -I, -one}
  };

inline int toQuaternion(char value) {
       if (value == 'i') return I;
  else if (value == 'j') return J;
  else if (value == 'k') return K;
  return one; // I don't know if this is useful
} 

inline string repr(int value) {
  string res;
  if (value < 0) res += '-';
  value = abs(value);
       if (value == I)   res += 'i';
  else if (value == J)   res += 'j';
  else if (value == K)   res += 'k';
  else if (value == one) res += '1';
  return res;
}

inline int resultingSign(int a, int b) {
  return a*b < 0 ? -1 : 1;
}

inline int map_index(int l, int i) {
  return i % l;
}
  
int main() {
  int cases;
  cin >> cases;

  ofstream ofs("solution2.out");
  if (ofs.fail()) {
    cout << "Fail to open file" << endl;
    return -1;
  }
  
  int l, x;
  string line;
  
  // jijijijijiji
  
  for (int t = 0; t < cases; t++) {
    cin >> l >> x >> line;
    bool ok = false;
    int result = toQuaternion(line[0]);
    int step = 1;
    const int limit = x * l;
    cout << "Testing case #" << t + 1 << " : " << line << endl;  
    if (line == "ijk" && x == 1) {
      cout << "  Matched directly" << endl;
      ok = true;
    }
    int j;
    for (j = 1; j < limit && !ok; j++) {
      int b = toQuaternion(line[map_index(l, j)]);
      // cout << "    " << repr(result) << " by " << repr(b);
      result = resultingSign(result, b) * table[abs(result) - 1][b - 1];
      // cout << " :  " << repr(result) << endl;
      if (step == 1) {
        if (result == I) {
          cout << "  i matched at " << j << endl;
          j++;
          result = toQuaternion(line[map_index(l, j)]);
          cout << "    new result: " << line[map_index(l, j)] << " in " << j << endl;
          step = 2;
        }
      } else if (step == 2) {
        if (result == J) {        
          cout << "  j matched at " << j << endl;
          j++;
          result = toQuaternion(line[map_index(l, j)]);
          cout << "    new result: " << line[map_index(l, j)] << " in " << j << endl;
          step = 3;
        }
      } else if (step == 3) {
        if (result == K) {
          if (j == limit - 1) {
            cout << "  k matched at " << j << endl;
            ok = true;
          }          
        }
      }
    }
    ofs << "Case #" << t + 1 << ": " << (ok ? "YES" : "NO") << endl;
  }
  
  ofs.flush();
  ofs.close();

  return 0;
}

