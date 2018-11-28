#include <iostream>
#include <stdio.h>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>

#define MAX(a,b) ((a)>(b)?(a):(b))

using namespace std;

int main() {
  ifstream fi("A-large.in");
  ofstream fo("outputa2L");

  // to store audience
  vector<int> aud;
  vector<int> ss;
  
  int t;
  fi >> t;
  fi.ignore();
  for(int i=0; i<t; i++) {
    int max;
    fi >> max;
    fi.ignore();   
    string s;
    fi >> s;
    stringstream trim;
    trim << s;
    s.clear();
    trim >> s;

    // assume input is properly taken after this line.
    
    int sum = 0;
    int count = 0;
    
    for(int j=0; j<s.size(); j++) {
      sum += s[j]-48;
      if(sum < j+1) {
	count++;
	sum++;
      }
    }
    fo << "Case #" << i+1 << ": " << count << endl;
    
    s.clear();
    ss.clear();
  }
}
