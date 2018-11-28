#include <iostream>
#include <sstream>
#include <NTL/ZZ.h>

using namespace std;
using namespace NTL;

bool is_palindrome(string s);

int main()
{
  int T;
  long count;
  stringstream ss;
  ZZ A;
  ZZ B;
  ZZ sqrt_A;
  ZZ sqrt_B;
  cin >> T;


  for(int t = 1; t <= T; t++)
  {
    count = 0;
    cin >> A;
    cin >> B;

    SqrRoot(sqrt_A, A);
    SqrRoot(sqrt_B, B);

    bool checked = false;
    for(ZZ i(sqrt_A); i <= sqrt_B; i++)
    {
      //will short out if checked 
      if(!checked ) 
      {
        if(i * i >= A)
        {
          checked = true;
        }
      }
      if(checked)
      {
        //get i as string
        ss.str("");
        ss.clear();
        ss << i;
        if(is_palindrome(ss.str()))
        {
          //get i^2 
          ZZ i_sqr;
          sqr(i_sqr, i);

          //convert to string
          ss.str("");
          ss.clear();
          ss << i_sqr;
          if(is_palindrome(ss.str()))
          {
            count++;
          }
        }
      }
    }

    cout << "Case #" << t << ": " << count << endl;
  }

  return 0;
}

bool is_palindrome(string s)
{
  int len = s.size();
  for(int i = 0; i < len/2; i++)
  {
    if(s[i] != s[len - i - 1])
      return false;
  }
  return true;
}
