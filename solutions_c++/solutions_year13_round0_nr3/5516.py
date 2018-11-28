#include <stdio.h>
#include <string.h>
#include <cmath>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>

using namespace std;

#define MAX 10001

int t, c, a, b, i, counter, fairsquare[MAX];
vector<int> squares;

void generate()
{
  memset(fairsquare, 0, sizeof fairsquare);

  stringstream number_stream;
  for (i = 0; i < (int) ceil(sqrt(MAX)); i++)
  {
    number_stream.str(string());
    number_stream.clear();
    number_stream << i;
    string number_str = number_stream.str();
    string number_str_copy = number_str;
    reverse(number_str.begin(), number_str.end());

    if (number_str == number_str_copy)
    {
      squares.push_back(i * i);
    }
  }

  for (i = 0; i < (int) squares.size(); i++)
  {
    number_stream.str(string());
    number_stream.clear();
    number_stream << squares[i];
    string number_str = number_stream.str();
    string number_str_copy = number_str;
    reverse(number_str.begin(), number_str.end());

    //cout << number_str << " " << squares[i] << endl;
    
    if (number_str == number_str_copy)
    {
      //printf("%d\n", squares[i]);
      
      fairsquare[squares[i]] = 1;
    }
  }

  //printf("%d\n", (int) squares.size());
}

int main()
{
  generate();

  scanf("%d", &t);

  for (c = 0; c < t; c++)
  {
    scanf("%d %d", &a, &b);
    counter = 0;

    for (i = a; i <= b; i++)
    {
      if (fairsquare[i])
      {
        counter++;
      }
    }

    printf("Case #%d: %d\n", c + 1, counter);
  }

  return 0;
}
