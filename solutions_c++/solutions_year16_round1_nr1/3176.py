
#include <iostream>
#include <fstream>
#define toDigit(c) (c-'0')
using namespace std;

int main () {
	int count;
  	int result, n, l, d;
  	
	ifstream input;
	ofstream output;
  	
	//input.open("A-sample.in", std::ios_base::in);
  	//output.open("A-sample.out", std::ios_base::out);
	
  	//input.open("A-small.in", std::ios_base::in);
  	//output.open("A-small.out", std::ios_base::out);
  	
	input.open("A-large.in", std::ios_base::in);
  	output.open("A-large.out", std::ios_base::out);
	    	
  	input >> count;

  	string s1,s2;
  	getline(input, s1);

  	for(int i=1; i<=count; i++)
  	{
  		getline(input, s1);
  		
  		s2 = s1[0];
		
		for(int j=1; j<s1.length(); j++)
		{
			char c = s2[0];
			if(c > s1[j])
			 s2 = s2 + s1[j];
			else
			 s2 = s1[j] + s2;
		}
		
		output<<"Case #"<<i<<": "<<s2<<endl;
	}  	
  
  	input.close();
  	output.close();
  	
  	return 0;
}
