#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>

using std::ifstream;
using std::ofstream;
using std::vector;
using std::string;
using std::set;
using std::endl;

bool f[10] = {0};

int main() {
  ifstream fin("a_in.txt");
  ofstream fout("a_out.txt");
  int T = 0;
  fin >> T;
  for (int i = 0; i<T; i++) {
    int n = 0, ans = 0;
    fin >> n;
    if (n==0) {
      fout << "CASE #"<<i+1<<": INSOMNIA"<<endl;
      continue;
    }
    int m = n;
    for (int j=0; j<10; j++) f[j] = false;
    int cnt = 0;
    while (true) {
      int tmp = m;
      while (tmp>0) {
	if (f[tmp%10]==false) {
	  f[tmp%10] = true;
	  cnt++;
	}
	tmp /= 10;
      }
      if (cnt==10) break;
      m += n;
    }
    fout << "CASE #"<<i+1<<": "<<m<<endl;
  }
  return 0;
}
