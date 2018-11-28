#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

std::vector<int> getGuess(int row_mode)
{
  int guess_row;
  cin >> guess_row;
  guess_row --;
  std::vector<int> guess_numbers;
  for (int i = 0; i < 4; ++i)
  {
    for (int j = 0; j < 4; ++j)
    {
      int number;
      cin >> number;
      if (row_mode)
      {
        if (j == guess_row)
        {
          guess_numbers.push_back(number);
        }
      }
      else
      {
        if (i == guess_row)
        {
          guess_numbers.push_back(number);
        }
      }
    }
  }
  return guess_numbers;
}
vector<int> getSameNumbers(std::vector<int>& lhv, std::vector<int>& rhv) {
  int li = 0, ri = 0;
  std::vector<int> same_numbers;
  while(li < lhv.size() && ri < rhv.size())
  {
    int lv = lhv[li];
    int rv = rhv[ri];
    if (lv < rv)
    {
      li ++;
    }
    else if(lv > rv)
    {
      ri ++;
    }
    else
    {
      same_numbers.push_back(lv);
      li ++;
      ri ++;
    }
  }
  return same_numbers;
}
void solve()
{
  vector<int> guess_1 = getGuess(0);
  vector<int> guess_2 = getGuess(0);
  sort(guess_1.begin(), guess_1.end());
  sort(guess_2.begin(), guess_2.end());
  vector<int> same_numbers = getSameNumbers(guess_1, guess_2);
  if (same_numbers.size() == 0)
  {
    cout << "Volunteer cheated!";
  }
  else if (same_numbers.size() == 1)
  {
    cout << same_numbers[0];
  }
  else
  {
    cout << "Bad magician!";
  }
  cout << endl;
}
int main(int argc, char const *argv[])
{
  int casn;
  cin >> casn;
  for (int i = 0; i < casn; ++i)
  {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
