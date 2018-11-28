#include <iostream>
#include <string>

using namespace std;

int main() {
  int cases=0;
  cin >> cases;
  int caseNum=0;
  while (caseNum < cases) {
    caseNum++;
    long smax=0;
    cin >> smax;
    long friends=0;
    long standees=0;
    for (long i=0; i<=smax; i++)
    {
	    char nextc = '0';
	    cin >> nextc;
	    int next= nextc-'0';
	    if (next>0 and i>standees) {
		    friends+=i-standees;
		    standees+=i-standees;
	    }
	    standees+=next;
    }
    cout << "Case #" << caseNum << ": " << friends << endl;
  }
  return 0;
}

