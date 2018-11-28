#include <iostream>
#include <fstream>

using namespace std;



int main(){

	ifstream ifile("input.in");
	ofstream ofile("output.out");
	int c1;
	int c2;
	int count=0;
	char c3;
	int person = 0;

	ifile >> c1;
	
	for (int i = 0; i < c1; i++){
		ifile >> c2;
		for (int j = 0; j < c2+1; j++){
			ifile >> c3;
			if (count>0){
				count--;
			}
			if ((c3 - 48) == 0 && count == 0){
				person++;
			}
			else{
				count += (c3 - 48);
			}
			
		}
		ofile << "Case #"<<i+1<<": "<<person << endl;
		person = 0;
		count = 0;
	}

	ifile.close();
	ofile.close();
	

	system("pause");
	return 0;
}