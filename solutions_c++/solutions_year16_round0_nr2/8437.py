#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void flipPancake(int N, int *digit){
	while(N != 0){
		int rem = N % 10;
		N = N/10;
		if(digit[rem]==0) digit[rem]=1;
	}
}
void main() {
  ifstream input_data;
  input_data.open("B-small-attempt0.in");
  ofstream myfile;
  myfile.open("pancakeOP.txt");
  int num,curr,prev,caseNum;
  caseNum=0;
  string text;
  getline(input_data,text);
  while (getline(input_data,text)){  // read t. cin knows that t is an int, so it reads it as such.
	caseNum+=1;
	num = 0;
	prev = -1;
	for(int i = 0; i < text.length(); ++i) {
		curr = ((text[i]=='+' )? 1 : 0 );
		if(curr != prev){
			num +=1;
			prev = curr;
		}
	}
	// curr is the the bottom of stack
	myfile << "Case #" << caseNum << ": " << ((curr==1)?num-1:num) << endl;
  }
  input_data.close();
  myfile.close();
}