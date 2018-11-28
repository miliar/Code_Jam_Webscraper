#include <iostream>
#include <cstdio>
#include <bitset>
#include <cstring>

using namespace std;

const char* INSOMNIA = "INSOMNIA";

int numDigits(int number)
{
  int digits = 0;
  if (number <= 0) digits = 1;
  while (number) {
    number /= 10;
    digits++;
  }
  return digits;
}

void solve(int &P)
{
  if (P == 0) {
    cout << INSOMNIA;
    return;
  }
  int C = 1;
  bitset<10> hash;
  bitset<10> oracle;
  oracle.set();
  while(true)
  {
    int v = C*P;
    int n = numDigits(v);
    for (int i = 1; i <= n; i++) 
    {
      hash.set(v % 10);
      v /= 10;
    }
    if (hash == oracle) {
      cout << (C*P);
      break;
    }
    C++;
  }
}


int main(int argc, char *args[]) 
{
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
  int N, P;
  cin >> N;
  for (int i = 1; i <= N; i++)
  {
    cin >> P;
    printf("Case #%d: ", i);
    solve(P); 
    cout << endl;
  }
}