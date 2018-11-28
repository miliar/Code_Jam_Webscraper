#include <iostream>  
#include <fstream>
#include <string>
using namespace std;  

void main() {

 ifstream input("A-large.in");
 ofstream output("output.txt");
  int t, n;
  input >> t;  
  for (int i = 1; i <= t; ++i) {
    input >> n;  
	if (n==0)	{
		output << "Case #" << i << ": " << "INSOMNIA" << endl;
		continue;
	}
	string fDigits="----------";
	int N=n;
	while (fDigits!="0123456789")	{
		string digits = to_string((_Longlong)N);
		for (int j=0; j < (int)digits.length(); j++)	{
			int s= (int)digits[j] - 48;
			fDigits[s]=digits[j];
		}
		N+=n;
	}
	N-=n;
	output << "Case #" << i << ": " << N << endl;
  }
}