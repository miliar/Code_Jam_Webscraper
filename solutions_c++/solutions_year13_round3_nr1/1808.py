#include <iostream>

using namespace std;

string input;
int n;

int solve(int begin, int end)
{
  int next = begin +1;
  if (next == end)
  {
    return 0;
  }
}

bool hasN(int start, int end)
{
  cout << input.substr(start, end - start) << ":";
  int c =0;
  for (int i = start; i < end; i++)
  {
    switch (input[i])
    {
      case 'a':
      case 'e':
      case 'i':
      case 'o':
      case 'u':
        c = 0;
        break;
      default:
        c++;
        if (c >= n)
        {
          cout << "yes" << endl;
          return true;
        }
    }
  }
  cout << "no" << endl;
  return false;
}

int main()
{
  int T;
  cin >> T;
  int counter;
  for (int i=0; i < T; i++)
  {
    counter = 0;
    cin >> input;
    cin >> n;
    for (int j=0; j < input.length(); j++)
    {
      for (int k=j+1; k < input.length() + 1; k++)
      {
        if (hasN(j,k))
          counter++;
      }
    }
    cout << "Case #" << i+1 << ": " << counter << endl;
  }
}
