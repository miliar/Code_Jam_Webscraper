#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

bool valid(string& P)
{
  for (int i = 0; i < P.length(); i++)
  {
    if (P[i] == '-') {
      return false;
    }
  }
  return true;
}

void reverse(string &P, int v)
{
  for (int i = 0; i <= v; i++) {
    if (P[i] == '-') {
      P[i] = '+';
    } else{
      P[i] = '-';
    }
  }
}

// flip once!!
void flip(string &P)
{
  int last = P.length() - 1;
  while (P[last] == '+')
  {
    last--;
  }
  // flip the whole thing to negative
  if (last == (P.length() - 1)) {
    while (P[last] == '-')
    {
      last--;
    }
    if (last < 0) {
      last = P.length() - 1;
    }
  }
  // reverse P[0...last]
  reverse(P, last);
}

void solve(string &P)
{
  int count = 0;
  while (!valid(P)) {
    flip(P);
    count++;
  }
  cout << count;
}

int main(int argc, char *args[]) {
  if (argc == 2 && strcmp(args[1], "small") == 0) {
    freopen("small.in", "rt", stdin);
    freopen("small.out", "wt", stdout);
  }
  else if (argc == 2 && strcmp(args[1], "large") == 0) {
    freopen("large.in", "rt", stdin);
    freopen("large.out", "wt", stdout);
  }
  else {
    freopen(args[1], "rt", stdin);
    freopen("a.out", "wt", stdout);
  }
  int N;
  string P;
  cin >> N;
  for (int i = 1; i <= N; i++)
  {
    cin >> P;
    printf("Case #%d: ", i);
    solve(P);
    cout << endl;
  }
}