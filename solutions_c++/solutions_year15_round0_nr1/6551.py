#include<iostream>
#include<string>


using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++)
  {
    int S_max;
    cin >> S_max;

    std::string input;
    cin >> input;
    int result = 0;
    int t = 0;
    for (int j = 0; j < input.length(); j++)
    {
      int count = input[j] - '0';
      if (count != 0 && j > t)
      {
        result += j-t;
        t += j-t;
      }
      t += count;
    }
    cout << "Case #" << i+1 << ": " << result << endl;
  }
}
