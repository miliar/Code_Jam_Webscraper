#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef vector<long>::iterator longIt;
typedef vector<double>::iterator doubleIt;
typedef vector<string>::iterator stringIt;
typedef vector<vector<long> >::iterator vecIntIt;
typedef vector<vector<double> >::iterator vecDoubleIt;
typedef vector<vector<string> >::iterator vecStringIt;

template <class T>
inline const T max_arg(const T& a, const T& b) {
  return (b<a)?1:2;
}

template <class T>
inline bool from_string(T& t, const string& s,
                        std::ios_base& (*f)(std::ios_base&)) {
  istringstream iss(s);
  return !(iss>>f>>t).fail();
}

template <class T>
inline string to_string(const T& t) {
  stringstream ss;
  ss<<t;
  return ss.str();
}

int main(int argc, char **argv) {
  ifstream inp(argv[1]); //input file
  ofstream outp((string(argv[1])+".out").c_str()); //output file

  int t;
  inp>>t;

  for(int i=0; i<t; i++) {

    /* Code goes here */
    double r, t;
    inp>>r>>t;

    double result = (1 - 2 * r + sqrt(1 - 4 * r + 4 * r * r + 8 * t)) / 4;

    unsigned long long res = result;

    bool good = false;
    unsigned long long answer = 0;

    if (res < 10) {
      res = 10;
    }

    while (!good) {
      for (unsigned long long j = res - 10; j <= res + 10; j++) {
	if (2 * j * r + (1 + (j - 1) * 2) * j > t) {
	  good = true;
	  answer = j - 1;
	  break;
	}
      }
      if (!good) {
	res += 19;
      }
      if (answer == res - 10) {
	good = false;
	res -= 19;
      }
    }

    outp<<"Case #"<<i+1<<": "<<answer<<endl;

    /* End of code */

  }

  inp.close();
  outp.close();
}
