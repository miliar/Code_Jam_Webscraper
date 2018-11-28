#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

bool done(vector<bool> &x) {
  for (int i=0;i < x.size();i++) {
    if (!x[i]) return false;
  }
  return true;
}

int main() {
  int n;
  cin >> n;

  for (int I=1;I<=n;I++) {
    vector<bool> digits;
    digits.resize(10,false);
    int Y;
    cin >> Y;
    ostringstream out;
    out << Y;
    //    cout << Y << endl;
    string x;
    x = out.str();
    for (int i=0;i<x.size();i++) {
      digits[x[i]-'0']=true;
    }
    if (Y==0) {
      cout << "Case #"<<I << ": INSOMNIA"<<endl;
    } else {
      int z=2;
      
      while (!done(digits)) {
	//Y=Y*z;
	ostringstream out;
	out << Y*z;
	string x1;
	x1 = out.str();
	for (int i=0;i<x1.size();i++) {
	  digits[x1[i]-'0']=true;
	}
	z++;
      }
      cout << "Case #" << I << ": " << Y*(z-1) << endl;
    }
  }
}
