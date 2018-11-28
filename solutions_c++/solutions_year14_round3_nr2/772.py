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

  const unsigned long long int const_modulo = 1000000007;

  int t;
  inp>>t;

  for(int i=0; i<t; i++) {

    /* Code goes here */
    int n;
    inp>>n;
    vector<string> trains;
    for (int j = 0; j < n; j++) {
      string instring;
      inp>>instring;
      trains.push_back(instring);
    }
    unsigned long long int possible = 1;    

    unsigned long starts[26];
    unsigned long ends[26];
    unsigned long unconnected[26];
    unsigned long same[26];

    unsigned long thingends[26];

    for (int j = 0; j < 26; j++) {
      starts[j] = 0;
      ends[j] = 0;
      unconnected[j] = 0;
      same[j] = 0;
      thingends[j] = 0;
    }
    bool impossible = false;
    for (int j = 0; j < n; j++) {
      starts[trains[j][0] - 'a']++;
      ends[trains[j][trains[j].length() - 1] - 'a']++;
      if (trains[j][0] == trains[j][trains[j].length() - 1]) {
	same[trains[j][0] - 'a']++;
	for (int k = 0; k < trains[j].length(); k++) {
	  if (trains[j][k] != trains[j][0]) {
	    impossible = true;
	  }
	}
      } else {
	thingends[trains[j][trains[j].length() - 1] - 'a'] = j;
      }
      for (int k = 1; k < trains[j].length() - 1; k++) {
	if ((trains[j][k] != trains[j][k - 1]) && (trains[j][k] != trains[j][trains[j].length() - 1])) {
	  unconnected[trains[j][k] - 'a']++;
	  if (unconnected[trains[j][k] - 'a'] > 1 || starts[trains[j][k] - 'a'] > 0 || ends[trains[j][k] - 'a'] > 0) {
	    impossible = true;
	  }
	}
      }
    }
    int train_parts = 0;
    for (int j = 0; j < 26; j++) {
      if (starts[j] - same[j] > 1 || ends[j] - same[j] > 1) {
	impossible = true;
      }
      for (int k = same[j]; k > 0; k--) {
	possible = (possible * k) % const_modulo;
      }
      if (starts[j] - same[j] == 0 && (starts[j] != 0 || ends[j] != 0)) {
	train_parts++;
      }
    }

    for (int j = train_parts; j > 0; j--) {
	possible = (possible * j) % const_modulo;
    }
    if (train_parts == 0) {
      impossible = true;
    }

    if (impossible) {
      outp<<"Case #"<<i+1<<": 0"<<endl;
    } else {
      outp<<"Case #"<<i+1<<": "<<possible<<endl;
    }

    /* End of code */

  }

  inp.close();
  outp.close();
}
