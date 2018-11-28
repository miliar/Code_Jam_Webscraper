#include <iostream>
#include <string>

using namespace std;

int main()
{
  int nb_tests = 0;
  cin >> nb_tests;
  for (int i = 0; i < nb_tests; ++i)
  {
    int s_max = 0;
    string row;
    cin >> s_max;
    cin >> row;

    int tot_nb = 0;
    int nb_friends = 0;
    for (int j = 0; j <= s_max; ++j)
    {
      int s_i = row[j] - '0';
      if (tot_nb < j)
      {
        int invite = j - tot_nb;
        nb_friends += invite;
        tot_nb += invite;
      }
      tot_nb += s_i;
    }

    cout << "Case #" << i+1 << ": " << nb_friends << endl;
  }

  return 0;
}
