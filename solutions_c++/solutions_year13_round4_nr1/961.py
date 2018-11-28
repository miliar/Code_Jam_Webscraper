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
    unsigned long long n;
    int m;
    inp>>n>>m;
    set<unsigned long long> unique;
    vector<unsigned long long> entry;
    vector<unsigned long long> exit;
    vector<unsigned long long> number;
    unsigned long long gain = 0;
    for (int j = 0; j < m; j++) {
      unsigned long long entry_, exit_, number_;
      inp>>entry_>>exit_>>number_;
      entry.push_back(entry_);
      exit.push_back(exit_);
      number.push_back(number_);
      unique.insert(entry_);
      unique.insert(exit_);
      if (exit_ > entry_) {
	for (int k = 0; k < number_; k++) {
	  gain += ((exit_ - entry_) * n - (((exit_ - entry_) * (0 + exit_ - entry_ - 1)) / 2)) % 1000002013;
	}
      }
    }
    vector<unsigned long long> stops(unique.begin(), unique.end());
    vector<unsigned long long> nument(stops.size());
    vector<unsigned long long> numexit(stops.size());
    vector<unsigned long long> cumsum(stops.size());
    for (int j = 0; j < stops.size(); j++) {
      for (int k = 0; k < entry.size(); k++) {
	if (stops[j] == entry[k]) {
	  nument[j] += number[k];
	}
      }
      for (int k = 0; k < exit.size(); k++) {
	if (stops[j] == exit[k]) {
	  numexit[j] += number[k];
	}
      }
    }

    cumsum[0] = nument[0] - numexit[0];

    for (int j = 1; j < stops.size(); j++) {
      cumsum[j] = cumsum[j - 1] + nument[j] - numexit[j];
    }

    bool done = false;
    unsigned long long fakeGain = 0;
    int start = 0;
    while (start != -1) {
      int j = start;
      unsigned long long minimum_val = 9999999999999;
      while (cumsum[j] != 0) {
	if (minimum_val > cumsum[j]) {
	  minimum_val = cumsum[j];
	}
	j++;
      }

      if (j > start) {
	for (int k = 0; k < minimum_val; k++) {
	  fakeGain += ((stops[j] - stops[start]) * n - (((stops[j] - stops[start]) * (0 + stops[j] - stops[start] - 1)) / 2)) % 1000002013;
	}
      }
      for (int k = start; k < j ; k++) {
	cumsum[k] -= minimum_val;
      }
      start = -1;
      for (int k = 0; k < stops.size(); k++) {
	if (cumsum[k] != 0) {
	  start = k;
	  break;
	}
      }
    }
    
    outp<<"Case #"<<i+1<<": "<<gain - fakeGain % 1000002013<<endl;

    /* End of code */

  }

  inp.close();
  outp.close();
}
