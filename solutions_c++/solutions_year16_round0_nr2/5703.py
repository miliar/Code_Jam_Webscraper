#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

string S;
int endOk;

bool isOk();
void flip(int);

main()
{
  int T;

  // INPUT
  scanf("%d", &T);

  for (int i = 1; i <= T; ++i) {
    int count = 0;
    cin >> S;
    endOk = S.length()-1;
    while (!isOk()) {
      int j = 1, len = S.length();
      while (j < len) {
        if (S[j] != S[0])
          break;
        ++j;
      }
      flip(--j);
      ++count;
    }
    cout << "Case #" << i << ": " << count << endl;
  }
}

bool isOk()
{
  for (int i = endOk; i >= 0; --i) {
    if (S[i] == '-')
      return false;
    else
      endOk = i;
  }
  return true;
}

void flip(int k)
{
  for (int i = 0, j = k; i <= j; ++i, --j) {
    S[i] = S[i] == '+' ? '-' : '+';
    if (i != j)
      S[j] = S[j] == '+' ? '-' : '+';
  }
}
