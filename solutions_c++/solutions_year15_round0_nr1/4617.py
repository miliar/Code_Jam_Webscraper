#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int ctoi(char c)
{
  return c - '0';
}

int main()
{
  int N;
  cin >> N;
  getchar();

  int sn;
  char *sa = new char[2000], *sp;

  for (int n = 0; n < N; ++n)
  {
    cin >> sn >> sa;
    sp = sa;
    
    int friends = 0;
    int have = ctoi(*(sp++));
    int need;
    for (int i = 0; i < sn; i++, sp++)
    {
      need = i + 1 - have - friends;
      if (need > 0)
      {
        friends += need;
      }
      have += ctoi(*sp);
    }
    cout << "Case #" << n + 1 << ": " << friends;

    cout << endl;
  }
  delete[] sa;

  return 0;
}