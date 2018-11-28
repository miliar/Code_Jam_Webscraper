#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

int bad_pancakes(vector<bool> pancakes) {
  int ret = 0;
  for (vector<bool>::iterator it = pancakes.begin(); it != pancakes.end(); it++)
    if (!*it) ret++;
  return ret;
}

vector<bool> flip_first(vector<bool> &pancakes, int until)
{
  vector<bool> p = vector<bool>(pancakes);
  for (int i = 0; i < until; i++) {
    p.insert(p.begin() + until - 1 - i, !pancakes.at(i));
    p.erase(p.begin() + until - i);
  }
  return p;
}

vector<bool> turn_all_pancakes(vector<bool> &pancakes)
{
  return flip_first(pancakes, pancakes.size());
}

int number_repeat_pancakes(vector<bool> p)
{
  int ret = 1;
  bool first_item = p.at(0);
  for (vector<bool>::iterator it = p.begin() + 1; it != p.end(); it++) {
    if (*it != first_item) break;
    ret++;
  }
  return ret;
}
int weigth_of(vector<bool> &p)
{
  int w = 0, current_w = 0;
  bool current_value = p.at(0);

  for (vector<bool>::iterator it = p.begin() + 1; it != p.end(); it++) {
    if (*it == current_value) {
      current_w++;
    } else {
      if (current_w > w) w = current_w;
      current_w = 1;
      current_value = *it;
    }
  }
  if (current_w > w) w = current_w;
  return w;
}

int solve(vector<bool> pancakes) {
  int moves = 0;
  vector<bool> p = pancakes;
  while (bad_pancakes(p) > 0) {
    int n_bad = bad_pancakes(p);
    if (n_bad == p.size()) {
      moves++;
      break;
    }

    vector<bool> p1 = turn_all_pancakes(p);
    int w1 = weigth_of(p1);
    vector<bool> p2 = flip_first(p, number_repeat_pancakes(p));
    int w2 = weigth_of(p2);

    p = w1 > w2 ? p1:p2;

    moves++;
  }

  return moves;
}

int main (int argc, char **argv) {
  int n_test_cases;
  if (scanf("%d", &n_test_cases) != 1) return 1;

  for (int i = 1; i <= n_test_cases; i++) {
    int n;
    char s[101] = {0};
    if (scanf("%s", s) != 1) return 2;
    vector<bool> pancakes;
    for (int j = 0; j < strlen(s); j++)
      pancakes.push_back(s[j] == '-' ? 0 : 1);
    cout << "Case #" << i << ": " << solve(pancakes) << endl;
  }
}

