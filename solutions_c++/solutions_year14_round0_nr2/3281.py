#include <iostream>
#include <iomanip>
using namespace std;


class CookiePicker
{
public:
  static const double StartRate = 2.0;
  CookiePicker(double C,double F,double X):
    mFarmCost(C),
    mFarmCookieRate(F),
    mWinTotoal(X)
  {
    mFarmNumber = 0;
    mRate = StartRate+mFarmNumber*mFarmCookieRate;
    mTime = 0;
  }
  double getWinTime(void);
  bool buyFarmorNot(double &winTime);
public:
  double mFarmCost;
  double mFarmCookieRate;
  double mWinTotoal;

  double mTime;
  double mRate;
  double mFarmNumber;
};
bool CookiePicker::buyFarmorNot(double &winTime)
{
  double buyFarmWinTime;
  double nextWinTime = mWinTotoal/mRate;
  buyFarmWinTime = mFarmCost/mRate+mWinTotoal/(mRate+mFarmCookieRate);
  if (buyFarmWinTime <nextWinTime)
    {
      winTime =mFarmCost/mRate;
      return true;
    }
  else
    {
      winTime = nextWinTime;
      return false;
    }

}
double CookiePicker::getWinTime(void)
{
  bool buyFarm = false;
  double nextTime;
  while ( true )
    {
      buyFarm=buyFarmorNot(nextTime);
      if (buyFarm)
        {
          mFarmNumber++;
          mRate = mRate+ mFarmCookieRate;
          mTime = mTime + nextTime;
        }
      else
        {
           mTime = mTime+ nextTime;
           break;
        }
    }
  return mTime;
}

void output(int time, double winTime)
{
  cout.precision(7);
  cout<<"Case #"<<setiosflags(ios::fixed)<<time<<": ";
  cout<<winTime<<endl;
}


int main(void)
{
  double C,F,X;
  int times;
  //freopen("input.txt","r",stdin);
  //freopen("output.txt","w",stdout);
  cin>>times;
  int i;
  double winTime;

  for (i=0;i<times;i++)
    {
      cin>>C>>F>>X;

      CookiePicker cp(C,F,X);
      winTime = cp.getWinTime();
      output(i+1,winTime);
    }
}
