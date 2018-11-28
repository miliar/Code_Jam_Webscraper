#include <fstream>
#include <iostream>
#include <memory>
#include <vector>

using namespace std;

// 'e' == 1, capital is minus
char mul(char a, char b)
{
  if (b == 'e')
    return a;
  switch (a)
  {
    case 'e':
      return b;
    case 'E':
      switch (b)
      {
        case 'E': return 'e';
        case 'i': return 'I';
        case 'I': return 'i';
        case 'j': return 'J';
        case 'J': return 'j';
        case 'k': return 'K';
        case 'K': return 'k';
      }
    case 'i':
      switch (b)
      {
        case 'E': return 'I';
        case 'i': return 'E';
        case 'I': return 'e';
        case 'j': return 'k';
        case 'J': return 'K';
        case 'k': return 'J';
        case 'K': return 'j';
      }
    case 'I':
      switch (b)
      {
        case 'E': return 'i';
        case 'i': return 'e';
        case 'I': return 'E';
        case 'j': return 'K';
        case 'J': return 'k';
        case 'k': return 'j';
        case 'K': return 'J';
      }
    case 'j':
      switch (b)
      {
        case 'E': return 'J';
        case 'i': return 'K';
        case 'I': return 'k';
        case 'j': return 'E';
        case 'J': return 'e';
        case 'k': return 'i';
        case 'K': return 'I';
      }
    case 'J':
      switch (b)
      {
        case 'E': return 'j';
        case 'i': return 'k';
        case 'I': return 'K';
        case 'j': return 'e';
        case 'J': return 'E';
        case 'k': return 'I';
        case 'K': return 'i';
      }
    case 'k':
      switch (b)
      {
        case 'E': return 'K';
        case 'i': return 'j';
        case 'I': return 'J';
        case 'j': return 'I';
        case 'J': return 'i';
        case 'k': return 'E';
        case 'K': return 'e';
      }
    case 'K':
      switch (b)
      {
        case 'E': return 'k';
        case 'i': return 'J';
        case 'I': return 'j';
        case 'j': return 'i';
        case 'J': return 'I';
        case 'k': return 'e';
        case 'K': return 'E';
      }
  }
}

int main(int argc, char* argv[])
{
  ifstream in(argv[1]);
  unsigned int N;
  in >> N;
  in.ignore();

  for (unsigned int n = 0; n < N; ++n)
  {
    unsigned int L, X;
    in >> L >> X;
    in.ignore();
    unique_ptr<char[]> str{new char[L+1]};
    in.getline(str.get(), L+1); // +1 to eat endl char

    cout << "Case #"<<n+1<<": ";
    char wanted = 'i';
    char cur = 'e'; // 1
    for (unsigned int x = 0; x < X; ++x)
    {
      char* p = str.get();
      for (unsigned int l = 0; l < L; ++l)
      {
        cur = mul(cur, *p++);
        if (cur == wanted)
        {
          if (wanted == 'i')
          {
            wanted = 'j';
            cur = 'e';
          }
          else if (wanted == 'j')
          {
            wanted = 'k';
            cur = 'e';
          }
          // stay at 'k'
        }
      }
    }

    if (cur == wanted)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
}
