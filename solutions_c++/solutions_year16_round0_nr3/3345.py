#include <iostream>
#include <fstream>
#include <deque>
#include <vector>
#include <string>
#include <cmath>

using std::ifstream;
using std::ofstream;
using std::deque;
using std::string;
using std::vector;
using std::endl;
using std::cout;
int cap = 0;
int ex;
void is_tp(unsigned int num, ofstream& fout) {
  deque<int> x;
  vector<long long> ans;
  int tmp = num;

  for (int i=0; i<ex; i++) {
    x.push_front(tmp%2);
    tmp /= 2;
  }
  for (int i=2; i<=10; i++) {
    long long mul = 1;
    long long target = 0;
    for (int j = x.size()-1; j>=0; j--) {
      target = target + (long long)mul*x[j];
      mul *= i;
    }
    bool is_prime = true;
    long long co = 0;
    for (long long k = 2; k<=(int)sqrt(target+1e-4); k++)
      if (target%k==0) {
	is_prime = false;
	co = k;
	break;
      }
    if (is_prime) return;
    ans.push_back(co);
  }
  for (auto i : x) fout<<i;
  for (auto i : ans) fout << ' ' << i;
  cap ++;
  fout << endl;
}
int main() {
  ifstream fin("b_in.txt");
  ofstream fout("b_out.txt");
  int T = 0;
  fin >> T;
  fout << "CASE #1:" << endl;
  for (int i = 0; i<T; i++) {
    int n = 0; int j = 0;
    fin >> n >> j;
    ex = n;
    for (unsigned int k=((1<<(n-1))+1); k<=((1<<n)-1); k+= 2) {
      is_tp(k, fout);
      if (cap==j) break;
    }
  }
  return 0;
}
