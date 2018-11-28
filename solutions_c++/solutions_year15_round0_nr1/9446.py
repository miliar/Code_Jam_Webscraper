#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main ()
{
  int tcases, i;
  
  cin>>tcases;
  
  for (i = 1; i <= tcases; i++)
  {
    int maxshy, shyness;
    string ppl;
    int friends = 0;
    int sumppl = 0;
    
    cin>>maxshy>>ppl;

    for (shyness = 0; shyness <= maxshy; shyness++)
    {
      int needed = 0;
      
      if (sumppl >= shyness)  /* no friends needed */
        sumppl += (ppl[shyness] - '0');

      else  /* friends needed */
      {
        needed = shyness - sumppl;
        friends += needed;
        sumppl += needed + (ppl[shyness] - '0');
      }
    }

    printf("Case #%d: %d\n", i, friends);
  }

  return 0;
}
