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

unsigned long long value_gain_left(unsigned long long v[], unsigned long long e, unsigned long long r, int i, int j);
unsigned long long value_gain_right(unsigned long long v[], unsigned long long e, unsigned long long r, int i, int j);
unsigned long long value_gain_mid(unsigned long long v[], unsigned long long e, unsigned long long r, int i, int j);

unsigned long long value_gain_left(unsigned long long v[], unsigned long long e, unsigned long long r, int i, int j) {
  if (i == j) {
    return 0;
  }

  int highest = 0;
  unsigned long long highest_val = 0;
  for (int k = i; k < j; k++) {
    if (v[k] > highest_val) {
      highest_val = v[k];
      highest = k;
    }
  }
  if (j - highest <= (e / r)) {
    return highest_val * r * (j - highest) + value_gain_left(v, e, r, i, highest);
  } else {
    return highest_val * e + value_gain_left(v, e, r, i, highest) + value_gain_mid(v, e, r, highest + 1, j);
  }
}

unsigned long long value_gain_right(unsigned long long v[], unsigned long long e, unsigned long long r, int i, int j) {
  if (i == j) {
    return 0;
  }

  int highest = 0;
  unsigned long long highest_val = 0;
  for (int k = i; k < j; k++) {
    if (v[k] > highest_val) {
      highest_val = v[k];
      highest = k;
    }
  }
  if (highest - i + 1 <= (e / r)) {
    return highest_val * r * (highest - i + 1) + value_gain_right(v, e, r, highest + 1, j);
  } else {
    return highest_val * e + value_gain_mid(v, e, r, i, highest) + 
      value_gain_right(v, e, r, highest + 1, j);
  }

}

unsigned long long value_gain_mid(unsigned long long v[], unsigned long long e, unsigned long long r, int i, int j) {
  if (i == j) {
    return 0;
  }
  int highest = 0;
  unsigned long long highest_val = 0;
  for (int k = i; k < j; k++) {
    if (v[k] > highest_val) {
      highest_val = v[k];
      highest = k;
    }
  }
  if (highest - i + 1 <= (e / r) && j - highest <= (e / r)) {
    return highest_val * (r * (highest - i + 1) + r * (j - highest) - e);
  }
  
  if (highest - i + 1 <= (e / r)) {
    return highest_val * r * (highest - i + 1) + value_gain_mid(v, e, r, highest + 1, j);
  }

  if (j - highest <= (e / r)) {
    return highest_val * r * (j - highest) + value_gain_mid(v, e, r, i, highest);
  }
  return highest_val * e + value_gain_mid(v, e, r, highest + 1, j) + value_gain_mid(v, e, r, i, highest);
}

int main(int argc, char **argv) {
  ifstream inp(argv[1]); //input file
  ofstream outp((string(argv[1])+".out").c_str()); //output file

  int t;
  inp>>t;

  for(int i=0; i<t; i++) {

    /* Code goes here */
    unsigned long long e, r, n;
    inp>>e>>r>>n;
    unsigned long long v[n];


    int highest = 0;
    unsigned long long highest_val = 0;
    for (int j = 0; j < n; j++) {
      inp>>v[j];
      if (v[j] > highest_val) {
	highest_val = v[j];
	highest = j;
      }
    }

    unsigned long long answer = e * highest_val + value_gain_left(v, e, r, 0, highest)
      + value_gain_right(v, e, r, highest + 1, n);

    outp<<"Case #"<<i+1<<": "<<answer<<endl;

    /* End of code */

  }

  inp.close();
  outp.close();
}
