#include <iostream>
#include <algorithm>
#include <vector>
#include<fstream>
using namespace std;
int main()
{
  int T,X,R,C,i;
  char c;
  int a[4];
  int b[4];
  int out;
  int number, convc;
  int standupsofar;
  int friends;
  ifstream input;
  ofstream output;
  input.open("D.in");
  output.open("aout.txt");
  input >> T;
  for(i=0;i<T;i++) {
        out = 0;
	input >> X;
	input >> R;
	input >> C;
	friends = max(R,C);
	C = min(R,C);
	R = friends;
	if (X == 1)
	  out = 1;
	if (X == 2 && R*C %2 == 0)
	  out = 1;
	if (X == 3) {
	  if (R == 3 && C == 2) {
	    out = 1;
	  }
	  if (R == 3 && C == 3) {
	    out = 1;
	  }
	  if (R == 4 && C == 3) {
	    out = 1;
	  }
	}
	if (X == 4 && C >= 3 && R == 4) {
	  out = 1;
	}
	cout << " " << friends;
	cout << endl;
	output << "Case #"<< i+1 <<": ";
	if (out == 1)
	  output << "GABRIEL" << endl;
	else 
	  output << "RICHARD" << endl;
	//	if(temp==1)
	//		output << num;
	//	if(temp ==0)
	//		output << "Volunteer cheated!";
	//	if(temp >1)
	//		output << "Bad magician!";
	//	output << endl;
	//	cout << number << endl;
	//	cout << rowb << endl;
  }
  return 0;
}
