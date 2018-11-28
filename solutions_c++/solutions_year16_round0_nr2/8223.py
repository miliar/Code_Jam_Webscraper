#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main() {

  ifstream fin;
  fin.open("B-large.in");
  ofstream fout;
  fout.open("out.txt");

  int t, n, count;
  fin >> t;
  string str;

  for (int k = 0; k < t; k++) {
    fin >> str;
    
    n = str.length();
    count = 0;
    while (n-1 >= 0) {

      if (count % 2 == 1) {
        str[n-1] = (str[n-1] == '+' ? '-' : '+');
      }

      if (str[n-1] == '-') {
        count += 1;
      }
      n -= 1;
    }

    fout << "Case #" << k+1 << ": " << count << endl;
  }

  return 0;

}
