#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

bool palin(double *in);

int main()
{
  int T=0;
  cin >> T;
  for (auto t=0;t<T;t++) {
    double A=0., B=0.;
    cin >> A >> B;
    //cout << A << "," << B << endl;
    double ra=floor(sqrt(A));
    double rb=floor(sqrt(B));
    long long count = 0;
    for (double i=ra;i<=rb;i+=1.) {
      //      cout << i;
      if (palin(&i)) {
	//cout << " true" << endl;
	double ii = i*i;
	if (palin(&ii)) {
	  if (A <= ii && ii <= B) {
	    count++;
	    //cout << i << ", " << ii << endl;
	  }
	}
      } else {
	//	cout << endl;
      }
    }
    cout << "Case #" << t+1 << ": " << count << endl;
  } // T loop
}

bool palin(double* in) {
  string line;
  stringstream ss;
  ss << *in;
  ss >> line;
  if (line.length() > 1) {
    if (line[0] != line[line.length()-1]) {
      return false;
    }
  }
  string rline(line);
  reverse(rline.begin(),rline.end());
  return (line == rline ? true : false);
}
