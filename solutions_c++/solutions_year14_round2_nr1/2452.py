#include<iostream>
#include <string>
#include <set>
using namespace std;

void fail(int currCase) {
  cout << "Case #" <<currCase <<": Fegla Won"<< endl;      
}

void pass(int currCase, int result) {
  cout << "Case #" <<currCase <<": "<<result<< endl;      
}

int main () {
  int cases, currCase = 0, i;
  int count, totalStrings, passed;
  string a, b, t;
  char last;
  cin >> cases;
  while (currCase++ < cases) {
    cin >> totalStrings;
    cin >> a >> b;
    if ( a.size() > b.size() ) {
      t = a;
      a = b;
      b = t;
    }
    last = '0';
    i = 0;
    count = 0;
    passed = 1;

    while( i < a.size() && i < b.size() ) {
      if ( a[i] == b[i] ) {
        last = a[i];        
        i++;
      } else if ( last == a[i] ) {
        a.erase(i, 1);
        count++;
      } else if ( last == b[i] ) {
        b.erase(i, 1);
        count++;
      } else {
        passed = 0;
        fail(currCase);
        break;
      } 
    }
    if ( passed && i < a.size() ) {
      while(i < a.size()) {
        if ( last != a[i] ) {
          passed = 0;
          fail(currCase);
          break;
        }
        count++;
        i++;        
      }
    } 
    if ( passed && i < b.size() ) {
      while(i < b.size()) {
        if ( last != b[i] ) {
          passed = 0;
          fail(currCase);
          break;
        }
        count++;        
        i++;        
      }
    }
    if (passed) {
      pass(currCase, count);
    }
  }
  return 0;
}
