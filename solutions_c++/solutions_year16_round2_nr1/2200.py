#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  int i, j, k, n, ca, t, count[10];
  string s;
  ifstream fin;
  ofstream fout;
  
  fin.open("input.txt");
  fout.open("output.txt");
  fin >> t;
  for (ca = 1; ca <= t; ++ca) {
    cout << "Case #" << ca << ": ";
    fout << "Case #" << ca << ": ";
    fin >> s;
    for (i = 0; i < 10; ++i) {
      count[i] = 0;
    }
    for (i = 0; i < s.size(); ++i) {
      if (s[i] == 'Z') count[0]++;  // u
      if (s[i] == 'O') count[1]++;  // u
      if (s[i] == 'W') count[2]++;  // u
      if (s[i] == 'H') count[3]++;
      if (s[i] == 'U') count[4]++;  // u
      if (s[i] == 'F') count[5]++;
      if (s[i] == 'X') count[6]++;  // u
      if (s[i] == 'V') count[7]++;
      if (s[i] == 'G') count[8]++;  // u
      if (s[i] == 'N') count[9]++;
    }
    count[3] -= count[8];
    count[5] -= count[4];
    count[7] -= count[5];
    count[1] = count[1] - count[0] - count[2] - count[4];
    count[9] = count[9] - count[1] - count[7];
    count[9] /= 2;
    for (i = 0; i < 10; ++i) {
      while (count[i] > 0) {
	cout << i;
	fout << i;
	count[i]--;
      }
    }
    cout << endl;
    fout << endl;
  }
  fin.close();
  fout.close();
  
  return 0;
}
