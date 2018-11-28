#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <set>
#include <sstream>
using namespace std;

fstream in, out;

int T;
int N;
string ans;
set<double> naomi_masses;
set<double> ken_masses;
set<double> all_masses;

set<int> naomi_ranks;
set<int> ken_ranks;

int normal_war;
int deceit_war;


int main() {
  in.open("D-large.in", fstream::in);
  out.open("probd-large.out", fstream::out);

  in >> T;
  for (int i = 0; i < T; i++) {
    in >> N;
    naomi_masses.clear();
    ken_masses.clear();
    all_masses.clear();
    naomi_ranks.clear();
    ken_ranks.clear();
    for (int j = 0; j < N; ++j) {
      double mass;
      in >> mass;
      naomi_masses.insert(mass);
      all_masses.insert(mass);
    }
    for (int j = 0; j < N; ++j) {
      double mass;
      in >> mass;
      ken_masses.insert(mass);
      all_masses.insert(mass);
    }
    int count = 0;
    for (double mass : all_masses) {
      ++count;
      if (naomi_masses.count(mass) > 0) {
        naomi_ranks.insert(count);
      } else {
        ken_ranks.insert(count);
      }
    }

    normal_war = 0;
    set<int>::reverse_iterator nitr = naomi_ranks.rbegin();
    set<int>::reverse_iterator kitr = ken_ranks.rbegin();
    while (nitr != naomi_ranks.rend()) {
      if (*kitr < *nitr) {
        ++normal_war;
      } else {
        ++kitr;
      }
      ++nitr;
    }

    deceit_war = 0;
    set<int>::iterator nfitr = naomi_ranks.begin();
    set<int>::reverse_iterator nritr = naomi_ranks.rbegin();
    set<int>::iterator kfitr = ken_ranks.begin();
    set<int>::reverse_iterator kritr = ken_ranks.rbegin();
    while (nfitr != naomi_ranks.end()) {
      if (*nfitr > *kfitr) {
        ++deceit_war;
        ++kfitr;
        ++nfitr;
      } else {
        ++nfitr;
        ++kritr;
      }
    }

    std::stringstream ss;
    ss << deceit_war << " " << normal_war;
    ans = ss.str();

    out << "Case #" << i + 1 << ": " << ans << endl;
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
    
  in.close();
  out.close();
  return 0;
}
