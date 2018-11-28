#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int palindrome(long long n);

int main()
{
    ofstream fout ("C-small-attempt0.out");
    ifstream fin ("C-small-attempt0.in");
    long long T, a,b,countp,j,x,xp;
    fin>>T;
    for(int i=1; i<=T; i++)
    {
        countp = 0;
        fin >> a >> b;
        for(j=a; j<=b; j++)
        {
            if(palindrome(j))
            {
                xp = long (sqrt(j));

                if((xp*xp)==j && palindrome(xp))
                {
                    //cout<<xp<<" "<< xp*xp <<" "<< j<<endl;
                    countp++;
                }
            }
        }
        fout<<"Case #"<<i<<": "<<countp<<endl;
    }
    return 0;
}
int palindrome(long long n)
{
     long long num, rev,dig;
     num = n;
     rev = 0;
     while (num > 0)
     {
          dig = num % 10;
          rev = rev * 10 + dig;
          num = num / 10;
     }

    if(n==rev)
        {
            //cout<<n<<" is a fair square"<<endl;
            return true;
        }
    else
        return false;
}
