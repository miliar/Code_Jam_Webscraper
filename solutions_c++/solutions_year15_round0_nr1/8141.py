#include "iostream"
#include "fstream"
#include "vector"
using namespace std;

int main() {
  int Tcase = 0;
  ifstream ifs("A-large.txt");
  ofstream ofs("qa.txt");
  //
  ifs >> Tcase;
  for (int t = 1; t <= Tcase; ++t) {
    int smax = 0;
    ifs >> smax;
    vector<int> s;
    char c;
    for (int i = 0; i <= smax; ++i) {
      ifs >> c;
      s.push_back(c - '0');
    }
    int count = 0;
    int sum = 0;
    for (int i = 0; i < s.size(); ++i) {
      if (i <= sum) {
        sum += s[i];
      } else {
        count += i - sum;
        sum += s[i] + i - sum;
      }
    }
    ofs << "Case #" << t << ": " << count << endl;
  }
  //
  ifs.close();
  ofs.close();
  return 0;
}