#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
  string line1;
  int I;
  cin >> I;
  getline(cin,line1);
  for (int i=1;i<=I;i++) {
    string line;
    getline(cin,line);
    //cout << line << endl;
    if (!cin.fail()) {
    // Compute the lexicographically last string 
      string current;
      string tmp;
      tmp = line[0];
      current=tmp;
      //cout << current << endl;
      for (int k=1;k<line.length();k++) {
	//cout << current << " " << line[k] << endl;
	if (line[k] >= current[0]) {
	  //current.insert(0,line[k]);
	  string temp;
	  temp= current;
	  string temp1;
	  temp1=line[k];
	  current = temp1 + temp;
	  //current = current + temp;
	  //current = line[k]+current;
	} else {
	  string tmp2;
	  tmp2 = line[k];
	  string tmp3;
	  tmp3 = current;
	  current = tmp3 + tmp2;
	}
	//cout << current << endl;
      }
      cout << "Case #"<<i <<": " << current << endl;
    }
  }
}
