#include <iostream>
#include <string>

using namespace std;

int main()
{
   int T;
   cin >> T;
   
   for (int testCase = 1; testCase <= T; testCase++)
   {
       int Smax;
       string S;
       
       cin >> Smax >> S;
       
       int people = 0;
       int friends = 0;
       for (int level = 0; level <= Smax; level++)
       {
            if (people < level)
            {
                friends += level - people;
                people = level;
            }
            
            people += S[level] - '0';
       }
       
       cout << "Case #" << testCase << ": " << friends << endl;
   }
   
   return 0;
}

