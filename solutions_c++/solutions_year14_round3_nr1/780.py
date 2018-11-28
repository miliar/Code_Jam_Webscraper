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

bool check_correctness(unsigned long long int p, unsigned long long int q) {
  while ((q % 2) == 0) {
    q /= 2;
  }
  if (p % q == 0) {
    return true;
  } else {
    return false;
  }
}

int main(int argc, char **argv) {
  ifstream inp(argv[1]); //input file
  ofstream outp((string(argv[1])+".out").c_str()); //output file

  int t;
  inp>>t;

  for(int i=0; i<t; i++) {

    /* Code goes here */
    
    unsigned long long int p, q;
    char slash;
    inp>>p>>slash>>q;

    if (check_correctness(p, q)) {
      int generation = 0;
      
      while (p < q) {
	generation++;
	p *= 2;
      }
      outp<<"Case #"<<i+1<<": "<<generation<<endl;
    } else {
      outp<<"Case #"<<i+1<<": impossible"<<endl;
    /* End of code */
    }
  }

  inp.close();
  outp.close();
}
