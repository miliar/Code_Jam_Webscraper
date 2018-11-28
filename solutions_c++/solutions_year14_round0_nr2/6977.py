#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
          long double fr, inc, dis, tt , nt, dt;
          int t, x = 1, c = 0;
          cin >> t;
          while (x <= t) {
                    double rate = 2;

                    cin >> fr >> inc >> dis;
                    tt = dis/rate;
                    dt = 0;
                    //cout <<"dir" << tt << endl;
                    while (1) {
                              nt = dt + fr/rate;
                              dt = nt;
                              rate += (inc);
                              nt += (dis/rate);
                            //  cout << "newtime " << nt << " " << tt << endl;
                              if (tt > nt) {
                                        tt = nt;
                              } else {
                                        break;
                              }
                              c++;
                    }
                    cout <<"Case #"<<x<<": " << fixed<<setprecision(7) << tt << endl;
                    x++;
          }
          return 0;
}

