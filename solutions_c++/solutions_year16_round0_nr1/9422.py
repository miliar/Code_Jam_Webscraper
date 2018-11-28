#include <iostream>
#include <string>

using namespace std;

void solve (int cases)
{
   bool a[10] = {false};
   int nn;
   int n;
   string s;
   bool solved = false;
   
   cin >> n;
   nn = n;
   int i = 1;
   
   if (n == 0)
   {
      cout << "Case #" << cases << ": " << "INSOMNIA" << endl;
      return;
   }
  
   while (!solved)
   {   
      s = to_string (n);
      
      for (int i = 0; i < s.length (); i++)
	 a[s[i] - '0'] = true; 

      solved = true;
      for (int i = 0; i < 10; i++)
	 if (!a[i])
	    solved = false;

      if (!solved)
      {
	 n = nn * (i + 1);
	 i++;
      }
   }  

   cout << "Case #" << cases << ": " << n << endl;   
}

int main ()
{
   int n;
   cin >> n;
   
   int i = 1;
   while (n--)
   {
      solve (i);
      i++;
   }
   
   return 0;
}
