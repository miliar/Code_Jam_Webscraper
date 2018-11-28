#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <iostream>
#include <iterator>
#include <cmath>

using namespace std;

#define cerr if (0) cerr

// N log N
int solve_war(vector<double> naomi,
	      vector<double> ken)
{
  const int N = naomi.size();

  int point_n = 0;

  cerr << "\t" << "solve by war-optimally." << endl;

  for (int i = 0; i < N; ++i) {
    double choose_n = naomi.front();
    naomi.erase(naomi.begin());
    vector<double>::iterator choose_k_it = lower_bound(ken.begin(), ken.end(), choose_n);

    cerr << "\t" << choose_n << " vs " << *choose_k_it << endl;
    
    if (choose_k_it == ken.end()) {
      point_n++; // naomi win!
      choose_k_it = --ken.end();
    }
    ken.erase(choose_k_it);
  }

  return point_n;
}

int solve_deceitfulwar(vector<double> naomi,
		       vector<double> ken)
{
  const int N = naomi.size();

  int point_n = 0;

  cerr << "\t" << "solve by deceitful-war-optimally." << endl;

  for (int i = 0; i < N; ++i) {
    if (naomi.front() < ken.front() ||
	naomi.back() < ken.back()) {
      naomi.erase(naomi.begin());
      ken.erase(--ken.end());
    } else {
      naomi.erase(naomi.begin());
      ken.erase(ken.begin());
      point_n++;
    }
  }

  return point_n;
}

int main()
{
  int T;
  cin >> T;

  for (int cs = 1; cs <= T; ++cs) {
    int N;
    cin >> N;
    vector<double> naomi(N), ken(N);
    for (int i = 0; i < N; ++i) cin >> naomi[i];
    for (int i = 0; i < N; ++i) cin >> ken[i];

    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    
    cerr << "N:";
    for (int i = 0; i < N; ++i) cerr << " " << naomi[i]; cerr << endl;
    cerr << "K:";
    for (int i = 0; i < N; ++i) cerr << " " << ken[i]; cerr << endl;


    int ans_war = solve_war(naomi, ken);
    int ans_deceitfulwar = solve_deceitfulwar(naomi, ken);
    cout << "Case #" << cs << ": " << ans_deceitfulwar << " " << ans_war << endl;
  }

  return 0;
}
