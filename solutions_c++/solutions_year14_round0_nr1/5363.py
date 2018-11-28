/* Written by Filip Hlasek 2014 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

#define MAX 16
bool possible[MAX];

int main(int argc, char *argv[]) {
  int T, row, a;
  scanf("%d", &T);
  REP(t, T) {

    REP(i, MAX) possible[i] = true;

    scanf("%d", &row);
    REP(i, 4) REP(j, 4) { scanf("%d", &a); if (row - 1 != i) possible[a - 1] = false; }

    scanf("%d", &row);
    REP(i, 4) REP(j, 4) { scanf("%d", &a); if (row - 1 != i) possible[a - 1] = false; }

    vector<int> options;
    REP(i, 16) if (possible[i]) options.push_back(i + 1);

    printf("Case #%d: ", t + 1);
    if (options.size() == 1) printf("%d", options[0]);
    else if (options.size() > 1) printf("Bad magician!");
    else printf("Volunteer cheated!");

    printf("\n");
  }
  return 0;
}
