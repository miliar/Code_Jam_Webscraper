#include <iostream>
#include <fstream>
using namespace std;

const char* fi = "A-large.in";
const char* fo = "output-large.txt";
const int maxn = 30;

ifstream fin;
ofstream fout;

int a[maxn];
int n;

void ReadFile();
void Solvee();

int main(int argc, const char * argv[]) {
  fin.open(fi);
  fout.open(fo);
  
  int nTest;
  fin >> nTest;
  for (int i = 1; i <= nTest; i++) {
    ReadFile();
    fout << "Case #" << i << ": ";
    Solvee();
    fout << endl;
  }
  
  fin.close();
  fout.close();
  return 0;
}

void ReadFile() {
  fin >> n;
  for (int i = 0; i < n; i++) {
    fin >> a[i];
  }
}

void Solvee() {
  int maxxx = 0;
  int maxx = -1;
  int max = -1;
  
  // Find largest.
  for (int i = 0; i < n; i++) {
    if (a[i] > a[maxxx]) { maxxx = i; }
  }
  
  // Find 2nd largest.
  for (int i = 0; i < n; i++) {
    if (i != maxxx && a[i] > a[maxx] && a[i] <= a[maxxx]) { maxx = i; }
  }
  
  // Find 3rd largest.
  for (int i = 0; i < n; i++) {
    if (i != maxxx && i != maxx && a[i] > a[max] && a[i] <= a[maxx]) { max = i; }
  }

  // Make a[maxxx] == a[maxx]
  while (maxx != -1 && a[maxxx] > a[maxx]) {
    if (a[maxxx] - a[maxx] % 2 != 0) {
      a[maxxx] -= 1;
      fout << char(maxxx + 65) << " ";
    } else {
      a[maxxx] -= 2;
      fout << char(maxxx + 65) << char(maxxx +65) << " ";
    }
  }
  
  // Make a[maxxx] == a[maxx] == a[max]
  while (max != -1 && a[maxx] > a[max]) {
    a[maxx] -= 1;
    a[maxxx] -= 1;
    fout << char(maxxx + 65) << char(maxx + 65) << " ";
  }
  
  for (int i = 0; i < n; i++) {
    if (i != max && i != maxx && i != maxxx) {
      while (a[i] > 0) {
        if (a[i] % 2 != 0) {
          a[i] -= 1;
          fout << char(i + 65) << " ";
        } else {
          a[i] -= 2;
          fout << char(i + 65) << char(i + 65) << " ";
        }
      }
    }
  }
  
  while (max != -1 && a[max] > 0) {
    if (a[max] % 2 != 0) {
      a[max] -= 1;
      fout << char(max + 65) << " ";
    } else {
      a[max] -= 2;
      fout << char(max + 65) << char(max + 65) << " ";
    }
  }
  
  while (a[maxxx] > 0) {
    a[maxxx] -= 1;
    a[maxx] -= 1;
    fout << char(maxxx + 65) << char(maxx + 65) << " ";
  }
}
