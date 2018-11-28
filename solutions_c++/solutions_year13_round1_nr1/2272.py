#include<stdio.h>
#include<fstream>
#include<iostream>
#define Long long long
using namespace std;

int main() {
  ifstream fin;
  ofstream fout;
  fin.open("in.txt");
  fout.open("out.txt");
  int T, p = 0;
  Long r, t, count;
  fin >> T;
  while (T--) {
    p++;
    count = 0;
    fin >> r >> t;
    while (t >= 0) {
      t = t - ((r + 1)*(r + 1) - r * r);
      r += 2;
      count++;
    }
    fout << "Case #" << p << ": " << count - 1 << endl;
  }
  fin.close();
  fout.close();
  return 0;
}