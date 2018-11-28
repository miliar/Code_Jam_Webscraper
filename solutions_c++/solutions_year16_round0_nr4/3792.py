#include <iostream>
#include <fstream>
using namespace std;


int main() {


	int test;

	ifstream myfile;
	myfile.open ("input.txt");
	myfile>>test;

	ofstream myfile2;
	myfile2.open ("output.txt");


	for (int i=0;i<test;i++){

		int num=0;
		myfile>>num;
		myfile>>num;
		myfile>>num;

		
		myfile2<<"Case #"<<i+1<<": ";

		for (int j=1; j<num; j++){
			myfile2<<j<<" ";
		}
	
		myfile2<<num<<endl;


	}


	myfile.close();
	myfile2.close();

	return 0;
	
}