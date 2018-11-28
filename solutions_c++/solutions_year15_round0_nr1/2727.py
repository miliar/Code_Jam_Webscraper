#include <iostream>
#include <string>

using namespace std;

int main()
{
     int test_cases;
     cin >> test_cases;
     for(int i=0; i<test_cases; i++)
     {
          int maxshy;
          string audience;
          int to_invite = 0, clappers = 0;
          cin >> maxshy >> audience;
          for(int j=0; j<=maxshy; j++)
          {
               if(j > clappers)
               {
                    int extras = j-clappers;
                    to_invite+=extras;
                    clappers+=extras;
               }
               clappers+=audience[j]-'0';
          }

          cout << "Case #" << (i+1) << ": " << to_invite << endl;
     }

     return 0;
}
