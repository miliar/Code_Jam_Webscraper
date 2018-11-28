#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool ispal(int n)
{
     char s[12];
     itoa(n, s, 10);
     int l = strlen(s) - 1;
     for(int i = 0; i <= l; ++i)
             if(s[i] != s[l-i])
                     return false;
     return true;
     }

bool isdec(double s)
{
     int ss = s;
     double sss = ss;
     if(s - sss > 0)
             return false;
     return true;
     }

int main(int argc, char *argv[])
{
    ifstream cin ("C-small-attempt0.in");
    ofstream cout ("C-small-attempt0.out");
    int n, ctr = 1, a, b, cter = 0;
    cin>>n;
    while(n--)
    {
              cter = 0;
              cin>>a>>b;
              for(int i = a; i <= b; ++i)
                      if(ispal(i) && isdec(sqrt(i)) && ispal(sqrt(i)))
                                      cter++;
              cout<<"Case #"<<ctr<<": "<<cter<<endl;
              ctr++;
              }
    return 0;
    //system("PAUSE");
    //return EXIT_SUCCESS;
}
