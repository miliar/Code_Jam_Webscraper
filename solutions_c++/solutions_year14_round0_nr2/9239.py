// run cat sample.in | ./qrb > qrb_sample.out
#include <boost/format.hpp>
#include <iostream>
#include <iomanip>
using namespace std;
int debug = 0;

int main(int argc, const char *argv[]) {
  int Tc = 0;
  double c = 0.0; // cost per farm
  double f = 0.0; // farm output
  double x = 0.0; // total number of cookies needed
  double t = 0.0; // time
  double cookies = 0.0; // current number of cookies
  double cps = 2.0; // cookies per second (base production rate)
  int nf = 0; // number of farms
  double tinc = 0.0; // time increment
  double cookie_inc = 0.0; // cookie increment
  double est1 = 0.0; // time to x with current number of farms
  double est2 = 0.0; // time to next farm
  int sf = 0; // skip farm
  double testmin = 0.0; // minimun time est
  double testminprev = 0.0; // minimun save time
  cin >> Tc;
  if (debug == 1) {
    cout << Tc <<  endl;
  }
  for (int tcase = 1; tcase <= Tc; tcase++) {
    cin >> c >> f >> x;
    if (debug == 1) {
      cout << boost::format("%1$.7f") % c  << " " << boost::format("%1$.7f") % f << " " << boost::format("%1$.7f") % x << endl;
    }

    // initial conditions
    t = 0.0;     // time zero
    cookies = 0; // no cookies
    nf = 0;      // no farms
    testmin = t + (x - cookies) / (nf * f + cps); // initial estimate of time to complete
    while (cookies < x) {
      sf = 0;
      // estimate time to complete with current farms
      est1 = (x - cookies) / (nf * f + cps);
      // estimate time to next farm
      est2 = (c - cookies) / (nf * f + cps);
      tinc = est2;
      // problem: when do you know you're close enough?
      if ((t + est1) > testmin) {
	break;
	tinc = est1;
	sf = 1;
      }
      testminprev = testmin;
      testmin = t + est1;
      cookie_inc = tinc * (nf * f + cps);
      /**
      cout << "cookie_inc: " << cookie_inc 
	   << " tinc: " << tinc 
	   << " nf: " << nf
	   << " f: " << f
	   << endl;
      **/
      cookies += cookie_inc;
      t += tinc;
      if ((sf == 0) && (cookies + 0.000005 >= c)) {
	nf++;
	cookies -= c;
      }
      if (debug == 1) {
	cout << "time: " << boost::format("%1$.7f") % t 
	     << " cookies: " << boost::format("%1$.7f") % cookies 
	     << " farms: " << nf 
	     << " est1: " << est1 
	     << " est2: " << est2 
	     << " tinc: " << tinc 
	     << " production: " << (cps + nf * f)
	     << " testmin: " << boost::format("%1$.7f") % testmin
	     << endl;
	  }

    }
    // cout << "Case #" << tcase << ": " << boost::format("%1$.7f") % t << endl;
    cout << "Case #" << tcase << ": " << boost::format("%1$.7f") % testmin << endl;

  }
}
