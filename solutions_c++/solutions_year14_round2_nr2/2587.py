#include <iostream>

using namespace std;

int main()
{
  int t;
  cin >> t;

  for(int x=1; x<=t; x++)
  {
    int a, b, k;
    cin >> a >> b >> k;

    int cont=0;

    for(int i=0; i<a; i++)
    {
      for(int j=0; j<b; j++)
      {
        if((i & j) < k)
          cont++;
      }
    }

    cout << "Case #" << x << ": " << cont << endl; 
  }

  return 0;
}
