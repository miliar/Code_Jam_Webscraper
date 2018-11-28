#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;

void testCase()
{
  vector<int> li;
  for (int i = 1; i <= 16; i++)
    li.push_back(i);

  for (int tries = 0; tries < 2; tries++)
  {
    int p[4], row;
    scanf("%d", &row);
    for (int y = 1; y <= 4; y++)
    {
      for (int x = 0; x < 4; x++)
        cin >> p[x];
      if (y == row)
      {
        sort(p, p + 4);
        vector<int> res;
        set_intersection(p, p + 4, li.begin(), li.end(), back_inserter(res));
        li.swap(res);
      }
    }
  }
  if (sz(li) == 0)
    printf("Volunteer cheated!\n");
  else if (sz(li) > 1)
    printf("Bad magician!\n");
  else
    printf("%d\n", li[0]);
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
//    cout << "Case #" << t << ": ";
    printf("Case #%d: ", t);
    testCase();
  }
  return 0;
}
