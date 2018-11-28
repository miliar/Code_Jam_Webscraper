#include <iostream>
#include <fstream>

using namespace std;

void storeNum(int N, int *digit){
	while(N != 0){
		int rem = N % 10;
		N = N/10;
		if(digit[rem]==0) digit[rem]=1;
	}
}
int countSheeps(int N){
	int num = N;
	int digit [10] = {0};
	int sum = 0;
	int *dgPtr = digit;
	if (N==0)
		return -1;
	while(sum!=10){
		sum=0;
		storeNum(num,dgPtr);
		for(auto& dig : digit)
			sum += dig;
		num+=N;
	}
	return num-N;
}

void main() {
  ifstream input_data;
	input_data.open("A-large.in");
  ofstream myfile ;
	myfile.open("output.txt");
  int t,N;
  input_data >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
	input_data >> N;
	int num = countSheeps(N);
	if (num != -1)
		myfile<< "Case #" << i << ": " <<num<< endl;
	else
		myfile << "Case #" << i << ": " << "INSOMNIA "<< endl;
  }
  input_data.close();
  myfile.close();
}