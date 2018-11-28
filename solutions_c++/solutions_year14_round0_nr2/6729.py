#ifndef GCJ_COOKIE_CLIKER_H__
#define GCJ_COOKIE_CLIKER_H__

class CookieClicker
{
  public:
    CookieClicker(double price, double rate, double g);
    double solve();

  private:
    double solveRec(double rate);

    double farmPrice;
    double farmRate;
    double goal;
};

#endif
