  /*  
    name : Adarsh K                    
    mail : aadarshkarthikeyan@gmail.com  || adarshkarthikeyan@outlook.com                 
  */

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // freopen("in.txt", "r", stdin);                 // for giving input as file  (in.txt)
    // freopen("out.txt", "w", stdout);               // for saving output to file (out.txt)
	long long T,res,t,i;
  char s[101];
  for(cin >> T,t = 1; t <= T; t++)
  {
    res = 0;
    cin >> s;
    if(strlen(s) > 1)
    {
      for(i = 1; i < strlen(s); i++)
      {
        if(s[i-1] != s[i])
        {
          res++;
        }
      }
      if(s[strlen(s)-1] == '-')
        res++;
    }
    else
    {
      if(s[0] == '-')
        res = 1;
    }
    cout << "Case #" << t << ": " << res << endl;
  }
	
  return 0; 
}

