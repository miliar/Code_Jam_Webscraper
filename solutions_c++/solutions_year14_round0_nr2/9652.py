/* David Stenzel
 * Google Code Jam  2014*/
	
#include <iostream>
#include <iomanip>

using namespace std;

const int STANDARD_COOKIE_RATE = 2;

double getSmallestTime(const double &C, const double &F, const double &X);
double findSmallestTime(const double &C, const double &F, const double &X, const double &start, const double &f);
double timeToGetCookies(const double &C, const double &F, const double &X, const int &f);
double timeToGetFarm(const double &C, const double &F, const int &f);

int main()
{
  int T;
  double C, F, X;
  cin >> T;
  for (int i = 1; i <= T; ++i)
    {
      cin >> C;
      cin >> F;
      cin >> X;
      cout << "Case #" << i << ": " << fixed << setprecision(7) << getSmallestTime(C, F, X) << endl;
    }
  return 0;
}

double getSmallestTime(const double &C, const double &F, const double &X)
{
  return findSmallestTime(C, F, X, (double) X / STANDARD_COOKIE_RATE, 1);
}

double findSmallestTime(const double &C, const double &F, const double &X, const double &start, const double &f)
{
  double comparison = timeToGetCookies(C, F, X, f);
  if (comparison >= start)
    return start;
  return findSmallestTime(C, F, X, comparison, f+1);
}

double timeToGetCookies(const double &C, const double &F, const double &X, const int &f)
{
  double totalTime = 0;
  if (C < X)
    {
      for (int i = 0; i < f; ++i)
	{
	  totalTime+=timeToGetFarm(C, F, i);
	}
      totalTime += timeToGetFarm(X, F, f);
    }
  else
    {
      totalTime = (double) X / STANDARD_COOKIE_RATE;
    }
  return totalTime;
}

double timeToGetFarm(const double &C, const double &F, const int &f)
{
  return (double) C / ((F*f) + STANDARD_COOKIE_RATE);
}
