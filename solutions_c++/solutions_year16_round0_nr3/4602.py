#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

bool isPrime(ull);

queue<ull> q;

main()
{
  int T, N, J;

  // INPUT
  scanf("%d", &T);
  scanf("%d%d", &N, &J);

  string base ("1");
  vector<ull> baseNums (9, 1);
  vector<vector<ull> > digNums (9);
  for (ll i = 1, j = 0; i < N-1 || j < 9; ++i, ++j) {
    if (j < 9) {
      digNums[j] = vector<ull> (N-2);
      for (ll k = 0, base = 2+j; k < N-2; ++k) {
        digNums[j][k] = base;
        base *= (2+j);
      }
      baseNums[j] += pow(2+j, N-1);
    }
    if (i < N-1)
      base += '0';
  }
  base += '1';
  for (int i = 1; i <= T; ++i) {
    int count = 0;
    printf("Case #%d:\n", i);
    for (int j = N-2; j >= 0 && count < J; --j) {
      string newS (base);
      bool isOk = true;
      newS.replace(j, 1, 1, '1');
      vector<ull> baseTmp (9);
      while (!q.empty())
          q.pop();
      for (int l = 0; l < 9; ++l) {
        baseTmp[l] = baseNums[l] + digNums[l][N-2-j];
        if (isPrime(baseTmp[l]))
          isOk = false;
      }
      if (isOk) {
        cout << newS;
        while (!q.empty()) {
          ll tmp = q.front();
          q.pop();
          cout << " " << tmp;
        }
        cout << endl;
        ++count;
      }
      for (int k = j-1; k > 0 && count < J; --k) {
        while (!q.empty())
          q.pop();
        newS.replace(k, 1, 1, '1');
        isOk = true;
        for (int m = 0; m < 9; ++m) {
          baseTmp[m] += digNums[m][N-2-k];
          if (isPrime(baseTmp[m]))
            isOk = false;
        }
        if (isOk) {
          cout << newS;
          while (!q.empty()) {
            ull tmp = q.front();
            q.pop();
            cout << " " << tmp;
          }
          cout << endl;
          ++count;
        }
      }
    }
  }
}

bool isPrime(ull n)
{
  if (n <= 1)
    return false;
  else if (n <= 3)
    return true;
  else if (n % 2 == 0 || n % 3 == 0) {
    q.push(n % 2 == 0 ? 2 : 3);
    return false;
  }
  ull i = 5;
  while (i*i <= n && i > 4) {
    if (n % i == 0 || n % (i+2) == 0) {
      q.push(n % i == 0 ? i : i+2);
      return false;
    }
    i += 6;
  }
  return true;
}
