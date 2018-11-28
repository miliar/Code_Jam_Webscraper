#include <iostream>
#include <string>

using namespace std;


typedef int sol_t;

void print_soln (const int ncase, const sol_t &sol)
{
  cout << "Case #" << ncase << ": " << sol << endl;
}


#define IS_VOWEL(ch) (('a' == (ch)) || \
                      ('e' == (ch)) || \
                      ('i' == (ch)) || \
                      ('o' == (ch)) || \
                      ('u' == (ch)))

int n_value (const string &name, const int n)
{
  int n_value = 0;
  for (int i = n; i <= name.length (); ++i)
    for (int j = 0; (j + i) <= name.length (); ++j)
    {
      string sub = name.substr (j, i /* length */);

      int cons_cons = 0;
      for (int k = 0; k < sub.length (); ++k)
      {
        if (IS_VOWEL (sub.at (k)))
        {
          cons_cons = 0;
        }
        else
        {
          ++cons_cons;
          if (cons_cons == n)
          {
            ++n_value;
            break;
          }
        }
      }
    }
    
  return n_value;
}

int main ()
{

  int ncases;
  cin >> ncases;

  for (int i = 0; i < ncases; ++i)
  {
    string name;
    int n;
    cin >> name >> n;

    print_soln (i+1, n_value (name, n));
  }

  return 0;
}

