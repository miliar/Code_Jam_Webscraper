#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <fstream>
using namespace std;

// Shortcuts for common data types in contests
typedef long long         ll;
typedef vector<int>       vi;
typedef pair<int, int>    ii;
typedef vector<ii>        vii;
typedef set<int>          si;
typedef map<string, int>  msi;

// To simplify repetitions/loops
#define REP(i, a, b) \
  for (int i = int(a); i <= int(b); i++) // a to b and variable i is local
#define TRvi(c, it) \
  for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
  for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi (c, it) \
  for (msi::iterator it = (c).begin(); it != (c).end(); it++)

#define INF 2000000000  // 2 billion
#define MEMSET_INF 127  // about 2B
#define MEMSET_HALF_INF 63  // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers

int main () {
  int t, people_present, shy_string, invite = 0;
  int sum = 0;
  int it = 0;
  ifstream in ("A-small-attempt1.in");
  ofstream out;
  out.open ("out.txt");
  in >> t;
  vi shyness;

  while (t--) {
    it++;
    invite = 0;
    sum = 0;
    in >> people_present;
    shyness.resize(people_present + 1);
    in >> shy_string;

    for (int i = people_present; i >= 0; i--) {
      shyness[i] = shy_string % 10;
      shy_string /= 10;
    }
    for(int i = 0; i <= people_present; i++) {
      if ((i > sum)) {
        invite += (i - sum);
        sum += (i - sum);
      }
      sum += shyness[i];
    }

    out << "Case #" << it <<": " << invite << endl;
  }
  out.close();
  return 0;
}
