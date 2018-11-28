#include <iostream>
#include <vector>

using namespace std;

const int maxN = 100001;

int arr[maxN] = {0};

int n = 0;

int FindNextIndex(int index)
{
  for (size_t i = index; i <= n; ++i)
  {
    if (arr[i] != 0)
      return i;
  }

  return -1;
}

int main()
{
  int t;

  cin >> t;

  for (size_t k = 0; k < t; ++k)
  {
    cin >> n;

    string s;
    cin >> s;

    int additional = 0;
    int counter = 0;

    for (size_t i = 0; i < s.size(); ++i)
      arr[i] = s[i] - '0';

    int i = 0;

    while(1)
    {

      int number = arr[i];
      counter += number;
      arr[i] = 0;

      if (counter >= n)
        break;

      int oldCounter = counter;

      for (int j = min(counter, n); j >= 0; --j)
      {
        counter += arr[j];
        arr[j] = 0;
      }

      if (oldCounter == counter)
      {
        int ind = FindNextIndex(min(counter, n));
       
        if (ind == -1)
          break;

        additional += ind - counter;
        counter = ind;
      }

      i = counter;
    }

    cout << "Case #" << k + 1 << ": " << additional << endl;
  }

  return 0;
}