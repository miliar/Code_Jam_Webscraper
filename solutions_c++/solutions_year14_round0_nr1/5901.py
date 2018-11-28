#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>


using namespace std;

enum {

  CHEAT = -1,
  MAGIC = -2,
  BAD   = -3,
};

int nsame_cards (int lhs[4], int rhs[4])
{
  vector<int> v(4, 0);
  vector<int>::iterator it;

  it = std::set_intersection (lhs, lhs+4, rhs, rhs+4, v.begin ());

  int count = std::distance (v.begin (), it);

  if (count == 0) return CHEAT;
  else if (count == 1) return v.at (0);
  else return BAD;
}


int main ()
{
  unsigned long long int T = 0;
  cin >> T;

  for (unsigned long long int i = 0; i < T; ++i)
  {
    int grid1[4][4] = {0};
    int grid2[4][4] = {0};
    int ans1 = 0;
    int ans2 = 0;

    cin >> ans1;
    ans1 -= 1;

    for (int j = 0; j < 4; ++j)
      for (int k = 0; k < 4; ++k)
        cin >> grid1[j][k];

    cin >> ans2;
    ans2 -= 1;

    for (int j = 0; j < 4; ++j)
     for (int k = 0; k < 4; ++k)
       cin >> grid2[j][k];

    std::sort (&grid1[ans1][0], &grid1[ans1][0] + 4);
    std::sort (&grid2[ans2][0], &grid2[ans2][0] + 4);
    int n = nsame_cards (grid1[ans1], grid2[ans2]);

    cout << "case #" << i + 1 << ": ";
    switch (n) {
      case CHEAT : cout << "Volunteer cheated!"; break;
      case BAD   : cout << "Bad magician!";      break;
      default    : cout << n;                    break;
    }
    cout << endl;
  }
   
  return 0;
}
