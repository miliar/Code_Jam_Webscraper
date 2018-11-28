#include <iostream>
#include <string>
using namespace std;

// S[i] is # of people with shyness i
int S[1010];
int maxShyness = -1;

int solve()
{
  int i;
  int guestsSurplus = 0;
  int nStandingGuests = 0;
  for (i = 0; i <= maxShyness; i++)
  {
    if (nStandingGuests < i) {
      int newGuests = i-nStandingGuests;
      guestsSurplus += newGuests;
      nStandingGuests += newGuests;
    }
    nStandingGuests += S[i];
  }

  return guestsSurplus;
}

void readTestCase()
{
  string strS;
  cin >> maxShyness;
  cin >> strS;

  for (int i = 0; i < maxShyness+1; i++)
    S[i] = strS.at(i)-'0';

}

int main(int argc, char **argv)
{
  int T;
  cin >> T;
  
  for (int t = 1; t <= T; t++)
  {
    readTestCase();
    int sol = solve();

    // debug
    //cout << "Input is : " << maxShyness << " " << S[0] << S[1] << "..." << S[maxShyness-1] << S[maxShyness] << endl;

    cout << "Case #" << t << ": " << sol << endl;
  }

  return 0;
  
}
