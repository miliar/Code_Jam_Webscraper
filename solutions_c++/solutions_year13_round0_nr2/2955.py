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
    bool possible = true;
    int n, m;
    inp>>n>>m;
    int rows[n][m];
    for (int j = 0; j < n; j++) {
      for (int k = 0; k < m; k++) {
	inp>>rows[j][k];
      }
    }
    for (int j = 0; j < n; j++) {
      if (!possible) {
	break;
      }
      for (int k = 0; k < m; k++) {
	if (!possible) {
	  break;
	}
	bool possible1 = true;
	bool possible2 = true;
	for (int l = 0; l < n; l++) {
	  if (rows[j][k] < rows[l][k]) {
	    possible1 = false;
	  }
	}
	for (int h = 0; h < m; h++) {
	  if (rows[j][k] < rows[j][h]) {
	    possible2 = false;
	  }
        }
	if (!possible1 && !possible2) {
	  possible = false;
	}
      }
    }
    

    if (possible) {
      outp<<"Case #"<<i+1<<": YES";
    } else {
      outp<<"Case #"<<i+1<<": NO";
    }
    outp<<endl;

    /* End of code */

  }

  inp.close();
  outp.close();
}
