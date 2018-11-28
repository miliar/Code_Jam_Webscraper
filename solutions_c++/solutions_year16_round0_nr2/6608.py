#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
  string s;
  int i, t, c, counter;
  ifstream fin;
  ofstream fout;
  
  fin.open("input.txt");
  fout.open("output.txt");
  fin >> t;
  for (c = 0; c < t; ++c) {
    fin >> s;
    const char *pt = s.c_str();
    vector<bool> pancake;
    for (i = 0; i < s.length(); ++i) {
      if (*pt == '+') pancake.push_back(true);
      else pancake.push_back(false);
      pt++;
    }
    counter = 0;
    if (s.length() == 1) {
      if (pancake[0]) {
	cout << "Case #" << c + 1 << ": " << counter << endl;
	fout << "Case #" << c + 1 << ": " << counter << endl;
      }
      else {
	cout << "Case #" << c + 1 << ": " << counter + 1 << endl;
	fout << "Case #" << c + 1 << ": " << counter + 1 << endl;
      }
    }
    else {
      for (i = 0; i < s.length() - 1; ++i) {
	if (pancake[i] != pancake[i+1]) counter++;
      }
      if (!pancake[i]) counter++;
      cout << "Case #" << c + 1 << ": " << counter << endl;
      fout << "Case #" << c + 1 << ": " << counter << endl;
    }
  }

  fin.close();
  fout.close();
  return 0;
}
