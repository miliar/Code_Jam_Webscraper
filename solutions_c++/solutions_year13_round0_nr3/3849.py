#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

/*
inline unsigned long intsqrt(unsigned long long a) {
    unsigned long long rem = 0;
    int root = 0;
    int i;

    for (i = 0; i < 16; i++) {
        root <<= 1;
        rem <<= 2;
        rem += a >> 30;
        a <<= 2;

        if (root < rem) {
            root++;
            rem -= root;
            root++;
        }
    }

    return (unsigned long) (root >> 1);
}
*/
inline bool checkp(unsigned long long original)
{
  unsigned long long reversed=0, n=original;

  while (n>0)
  {
    reversed=reversed*10+n%10;
    n /= 10;
  }

  return original==reversed;
}

int main()
{
    ifstream fin("psquaresin.txt");
    ofstream fout("psquaresout.txt");
    int t;
    unsigned long long a,b;
    unsigned long sa,sb;
    fin>>t;
    for (int test=1; test<=t; test++)
    {
        int c=0;
        fin>>a>>b;
        sa=(unsigned long)ceil(sqrt(a));
        sb=(unsigned long)floor(sqrt(b));
        //cout<<sa<<" "<<sb<<endl;
        for (int i=sa; i<=sb; i++)
        {
            if(checkp(i))
            {
                if(checkp(i*i))
                    c++;
            }
        }
        fout<<"Case #"<<test<<": "<<c<<endl;
    }
    return 0;
}
