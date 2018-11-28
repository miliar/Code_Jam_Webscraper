#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
  int numcases;
  int maxshy;
  char numshy;
  int current_standing = 0;
  int friends_needed = 0;
  
  cin >> numcases;

  for (int testcase=1; testcase <= numcases; testcase++)
  {
    current_standing = 0;
    friends_needed = 0;
    cin >> maxshy;
    for (int shylevel = 0; shylevel <= maxshy; shylevel++)
    {
      cin >> numshy;
      numshy -= '0'; // convert to normal integer 0-9
      if (current_standing < shylevel) {
        // shylevel - current_standing is how many extra people we need to get this level to stand
        friends_needed += shylevel - current_standing;
        current_standing += shylevel - current_standing;
      }
      current_standing += numshy; // these people will be standing before we get to the next level
    }

    cout << "Case #" << testcase << ": " << friends_needed << endl;
  }
  

  return 0;
}
