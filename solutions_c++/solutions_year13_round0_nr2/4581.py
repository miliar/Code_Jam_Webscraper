#include <iostream>
#include <algorithm>

using namespace std;

int N; // Rows
int M; // Cols
int table[100][100];
bool fbr[100];
bool fbc[100];

void readTable()
{
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> table[i][j];
    }
  }
}

bool isPossible()
{
  std::fill(fbr, fbr+100, false);
  std::fill(fbc, fbc+100, false);

  for(int num = 100; num >= 1; num--)
  {
    bool nfbr[N];
    bool nfbc[N];
    std::fill(nfbr, nfbr+100, false);
    std::fill(nfbc, nfbc+100, false);

    for (int i = 0; i < N; i++)
      for (int j = 0; j < M; j++)
        if (table[i][j]==num)
        {
          if (fbr[i] && fbc[j]) return false;
          nfbr[i] = true;
          nfbc[j] = true;
        }
    for (int i = 0; i < 100; i++) {
      fbr[i] |= nfbr[i];
      fbc[i] |= nfbc[i];
    }
  }
  return true;
}


int main(int argc, const char *argv[])
{
  int T;

  cin >> T;
  for (int it = 1; it <= T; it++) {

    cout << "Case #" << it << ": ";
    readTable();
    if (isPossible())
    {
      cout << "YES" << std::endl;
    }
    else
    {
      cout << "NO" << std::endl;
    }
  }

  return 0;
}
