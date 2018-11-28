#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

map<int, bool> DissectNumber(int _number);

int main()
{
  ifstream input("A-large.in");
  ofstream output("A-large.out");
  string line = "";

  getline(input, line);
  int num_cases = atoi(line.c_str());

  for (int i = 0; i < num_cases; ++i)
  {
    output << "Case #" << i + 1 << ": ";
    getline(input, line);
    int old = -1, base = atoi(line.c_str()), n = base, counter = 1;

    map<int, bool> cache;
    while (true)
    {
      if (n == old)
      {
        output << "INSOMNIA" << endl;
        break;
      }

      map<int, bool> temp = DissectNumber(n);
      cache.insert(temp.begin(), temp.end());

      if (cache.size() == 10)
      {
        output << n << endl;
        break;
      }
      else
      {
        old = n;
        n = base * ++counter;
      }
    }
  }

  output.close();
  input.close();
  return 0;
}

map<int, bool> DissectNumber(int _number)
{
  map<int, bool> temp;
  string str = to_string(_number);
  for (int i = 0; i < str.size(); ++i)
    temp[str[i]] = true;
  return temp;
}
