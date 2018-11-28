#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <iomanip>
using namespace std;

int main(int argc, char* argv[])
{
  freopen(argv[1], "rt", stdin);
  freopen(argv[2], "wt", stdout);

  int T;
  double C, F, X;

  double rate;
  double amount;
  double time;

  cin>>T;
  for (int t=1; t<=T; t++)
  {
    printf("Case #%d: ", t);
    cin>>C>>F>>X;
    //cout<<C<<" "<<F<<" "<<X<<endl;
    time = 0;
    rate = 2;
    amount = 0; 

    while (amount < X)
    {
      if (amount < C)
      {
        time += (C - amount) / rate;
        amount = C;
      }
      
      if (amount >= C)
      {
        double timeContinueToWin = (X - amount) / rate;
        double timeFarmToMatch = C / F;
        if (timeContinueToWin < timeFarmToMatch)
        {
          time += timeContinueToWin;
          amount = X;
        }
        else
        {
          amount -= C;
          rate += F;
        }
      }
    }

    cout<<setprecision(10)<<time<<endl;


  }
}
