#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <list>
#include <iostream>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;

int main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("saida.out","w", stdout);
  int tt = 1;
  int T;
  scanf("%d", &T);
  while (T--) {
    int first_guess;
    scanf("%d", &first_guess);
    vector < int > result_set;
    vector < int > first_set, second_set;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++) {
	int va;
	scanf("%d", &va);
	if (i == first_guess - 1)
	  first_set.pb(va);
      }
    int second_guess;
    scanf("%d", &second_guess);
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++) {
	int va;
	scanf("%d", &va);
	if (i == second_guess - 1)
	  second_set.pb(va);
      }
    sort(first_set.begin(), first_set.end());
    sort(second_set.begin(), second_set.end());
    set_intersection(first_set.begin(), first_set.end(), second_set.begin(), second_set.end(), back_inserter(result_set));
    printf("Case #%d: ", tt++);
    if (result_set.size() == 0)
      printf("Volunteer cheated!\n");
    else if (result_set.size() == 1)
      printf("%d\n", result_set[0]);
    else
      printf("Bad magician!\n");
  }
  return 0;
}
