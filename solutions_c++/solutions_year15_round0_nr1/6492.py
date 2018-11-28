#include <iostream>
#include <algorithm>
#include <vector>
#include<fstream>
using namespace std;
int main()
{
  int T,i,j,k;
  char c;
  int a[4];
  int b[4];
  int number, convc;
  int standupsofar;
  int friends;
  ifstream input;
  ofstream output;
  input.open("A-large.in");
  output.open("aout.txt");
  input >> T;
  for(i=0;i<T;i++){
	input >> number;
	cout << " ";
	standupsofar = 0;
	friends = 0;
	for (j = 0; j < number+1; j++) {
	  input >> c;
	  convc = int(c)-48;
	  if (standupsofar >= j) {
	    standupsofar += convc;
	  }
	  else {
	    if (convc > 0) {
	      friends += j - standupsofar;
	      standupsofar = j + convc;
	    }
	  }
	  cout << convc;
	}
	cout << " " << friends;
	cout << endl;
	output << "Case #"<< i+1 <<": ";
	output << friends << endl;
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
