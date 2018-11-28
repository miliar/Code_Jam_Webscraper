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
		int diff=0;
		string face;
		myfile>>face;

		for (int j=1; j<face.length(); j++){
			if (face[j]!=face[j-1]){
				diff++;
			}
		}

		if (face[face.length()-1]=='-'){
			diff++;
		}
		
		myfile2<<"Case #"<<i+1<<": "<<diff<<endl;

	}


	myfile.close();
	myfile2.close();

	return 0;
	
}