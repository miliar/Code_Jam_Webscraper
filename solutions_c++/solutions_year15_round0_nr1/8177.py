#include <iostream>
#include <string>

using namespace std;

int main()
{
  int in;
  cin >> in;
  int z = 0;
  while(z < in)
  {
  int x;

  cin >> x;

  std::string input;
  int count = 0;
  int sum = 0;
  int res = 0;
  cin >> input;
  while(count < x+1)
    {
      //cout << "sum = " << sum << ", count = " << count << ", res = " << res << endl;
      if(sum < count)
      {
        ++res;
        ++sum;
      }

      int y = input[count] - '0';
      sum += y;

      ++count;
    }

  cout << "Case #" << z+1 <<": " << res << "\n";
  ++z;
  }
  return 0;
}

