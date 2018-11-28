#include <stdio.h>
#include <iostream>
#include <fstream>

// OPTIONAL
#include <math.h>
#include <limits.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

long long pw(long long dig)
{
  long long num = 1;
  while(dig--)
  {
    num*=10;
  }
  return num;
}

int g_d(long long num, int pos)
{
  return (num%pw(pos+1))/pw(pos);
}

bool is_p(long long num)
{
  /* check if it is palindromes */
  //find digit
  long long t = num;
  long long dig = 0;

  while (t>0) {
    ++dig;
    t/=10;
  } // end while  

  bool a = true;
  for (int i = 0; i < dig/2; ++i) {
    if(g_d(num,i) != g_d(num,dig-i-1))
    { a = false; break; }
  } // end for i 

  return a;
} // end is_p

int main(int argc, const char *argv[])
{
  ifstream read("input.in");
  ofstream write;
  write.open ("output.out");
  // STARTS HERE

  long long n, s_mn, s_mx, ans;
  read >> n;

  for (int case_no = 1; case_no <= n; ++case_no) {
    read >> s_mn >> s_mx;
    s_mn = ceil(sqrt(s_mn));
    s_mx = floor(sqrt(s_mx));
    ans = 0;
    for (long long i = s_mn; i <= s_mx; ++i) {
      if(is_p(i))
        if (is_p(i*i))
        {
          ans++;
        }
    } // end for i 
    // END HERE
    write << "Case #" << case_no << ": ";
    // ANSWER HERE
    write << ans << endl;
  } // end for case_no 
  return 0;
}
