#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <sstream>
using namespace std;
int isPalindrome(int n);
int main(int argc, char** argv)
{
//    cout << "Hello World!!";    
      int T,j; // number of test cases
      // ifstream infile("TTTT.in");
      ifstream infile("C-small-attempt0.in");
      infile >> T;

      for (j=0;j<T;j++)
      {
          int res = 0;
          int l,h;
          infile >> l >> h;
          int lsqrt, hsqrt;
          lsqrt = (int) sqrt(l>0? l-1 : l);
          hsqrt = (int)sqrt(h+1);
          for(int i=lsqrt;i<=hsqrt;i++)
          {
              int isq = i * i;
              if (isPalindrome(i) && isPalindrome(isq) && isq >=l && isq <=h)
              {
                  res++;
              }
          }
          cout << "Case #" << j+1 << ": " << res << endl;    
      }
}     

int isPalindrome(int n)
{
    if (n<10)
       return 1;
    stringstream ss;
    ss << n;
    string str = ss.str();
    string rev = string(str);
    reverse(rev.begin(), rev.end());
    string::iterator it = rev.begin();
    for ( ; it!=rev.end() && *it =='0'; ++it)
        ;
    rev.erase(rev.begin(), it);    
    if(rev.compare(str)==0)
       return 1;
    return 0;   
}
