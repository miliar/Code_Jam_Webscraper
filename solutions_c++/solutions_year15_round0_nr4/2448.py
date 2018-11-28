#include<iostream>
#include<fstream>

using namespace std;

int main(){
	int total_test_cases = 0;
	char line[100];
	char ch[100];
	int var_X=0, var_R=0, var_C=0;
	ifstream ifile;
	ifile.open("D-small-attempt0.in");
	ofstream ofile;
	ofile.open("output4.out");

	ifile.getline(line,100);
	total_test_cases = atoi(line);

	for (int case_no = 1; case_no <= total_test_cases; case_no++){
		ifile >> ch;
		var_X = atoi(ch);
		ifile >> ch;
		var_R = atoi(ch);
		ifile >> ch;
		var_C = atoi(ch);
		
		ofile << "Case #" << case_no << ": ";

		if ((var_C* var_R) % var_X != 0){
			ofile << "RICHARD" << endl;
		}
		else if (((var_R >= var_X) && (var_C >= (var_X - 1))) || ((var_C >= var_X) && (var_R >= (var_X - 1)))){
			ofile << "GABRIEL" << endl;
		}
		else{
			ofile << "RICHARD"<<endl;
		}
	}
}