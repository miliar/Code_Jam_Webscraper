#ifndef _COOKIE_CLICKER_H_
#define _COOKIE_CLICKER_H_

#include <fstream>
#include <string>

using namespace std;

class CookieClicker
{
  public:
    CookieClicker( ifstream& infile );
    ~CookieClicker();

  private:
    int _testcases;
    ofstream _outfile;
};

#endif
