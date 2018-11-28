#include <iostream>
#include <fstream> 
#include <iomanip>
using namespace std;

#define FOR_INCR(x,y) for(int x = 0; x < y; x++)
#define cout ofile
#define cin ifile


int main()
{

    int T;
    double result = 0.0;
    double c, x, f;
    ofstream ofile;
    ofile.open ("out.txt");
    ifstream ifile ("in.txt");
    cin >> T;
    double r  = 2.0;
    FOR_INCR(i,T)
    {
      cin >> c >> f >> x;
      while (x/r >(c/r +  (x/(r+f))))
      {
        result += (c/r);
        r = r +f; 
        //cout << " IN " <<(x/r) << "  " << (c/r +  (x/(r+f))) << endl;
      }
      result += x/r;
      cout << "Case #"<< i+ 1  <<": ";
      cout << fixed << showpoint;
      cout << setprecision(7);
      //cout.precision(7);
      cout <<  result << endl;

      r = 2.0;
      result = 0.0;
    }

    return 0;
}
