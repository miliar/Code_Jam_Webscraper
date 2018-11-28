#include <iostream>

using namespace std;

int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

void traiter_elf(int p, int q)
{
    int pgcd = gcd(p,q);

    p = p/ pgcd;
    q = q/ pgcd;

    int q1=q;

    bool possible = true;

    while(q1>1 && possible)
    {
        possible = (q1%2) == 0;
        q1 = q1/2;
    }
    if(!possible)
    {
        cout << "impossible";
    }
    else
    {
        int i = 0;
        while(p<q)
        {
            p = p*2;
            i++;
        }
        cout << i;
    }
}

void elf()
{
    int n;
    cin >> n;

    for(int i = 0; i<n; i++)
    {
        int p,q;
        char buffer;
        cin >> p >> buffer >> q;
        cout << "Case #" << i+1 << ": ";
        traiter_elf(p, q);
        cout << "\n";
    }

}


int main()
{
    elf();
    return 0;
}
