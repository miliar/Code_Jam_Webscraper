#include <iostream> 
#include <fstream>
#include <string> 
#include <stdlib.h> 
#include <cstring>
#include <time.h> 
#include <cmath>
#include <unordered_set>
using namespace std;

int main (int argc, char** args) { 
  ifstream in;
  in.open(args[1]);
  if (!in) { 
   cerr << "Can't open filebase.in" << endl; exit(2); 
  } 
  // read all input from in, write to cout 
  // in >> ... 
  // cout << ...
  srand (time(NULL));
  ofstream out("output");
  int total;
  in >> total;
  for (long t = 0; t < total; t++) {
    out << "Case #" << t + 1 << ": ";
    int k,c,s;
    in >> k >> c >> s;
    long long max = pow(k,c);
    if (s == 1 && max == 1) {
      out << 1 << endl;
      continue;
    }
    if (s == 1 && max != 1) {
      out << "IMPOSSIBLE" << endl;
      continue;
    }
    long long diff = pow(k, c - 1);
    long long start = 1;
    for (int i = 0; i < s; i++) {
      out << start << " ";
      start += diff;
    }
    out << endl;
    //out << count << endl;
    cout << "Finished " << t + 1 << " out of " << total << endl;
    
  }
  out.close();
  return 0; 
} 