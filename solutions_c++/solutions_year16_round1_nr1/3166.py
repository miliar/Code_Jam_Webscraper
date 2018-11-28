#include <iostream> 
#include <fstream>
#include <string> 
#include <stdlib.h> 
#include <cstring>
#include <time.h> 
#include <cmath>
#include <vector>
#include <stdio.h>

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
  for (int t = 0; t < total; t++) {
    out << "Case #" << t + 1 << ": ";
    char ori[2000];
    in >> ori;
    std::vector<char> v;
    v.push_back(ori[0]);
    int length = strlen(ori);
    for (int i = 1; i < length; i++) {
        if (ori[i] >= v[0]) {
            v.insert(v.begin(), ori[i]);
        } else {
            v.push_back(ori[i]);
        }
    }
    for (auto c : v) {
        out << c;
    }
    out << endl;
    //out << count << endl;
    cout << "Finished " << t + 1 << " out of " << total << endl;
    
  }
  out.close();
  return 0; 
} 