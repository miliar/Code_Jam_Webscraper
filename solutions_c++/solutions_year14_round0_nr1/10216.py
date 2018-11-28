#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int readMaxtrix(ifstream &instream, int a[]);
int copyArray(int src[], int des[]);
int search(int n, int array[]); // return 0 if not found, else otherwise

int main(int argv, char* agrs[]){
	ofstream fout;
	ifstream fin;
//	cout << "number of parameters : "<<argv << endl;
//	cout << agrs[0]<<endl;
//	cout << agrs[1]<<endl;
	if (argv >=3){
		fout.open(agrs[1],std::ios::app);
		fin.open(agrs[2],std::ios::app);
	}
	else {
		cout << "Not enough parameters."<<endl;
		cout <<"Parameter list : [program name] [output file name] [input filename] " <<endl;
		return 1;
	}

	char* lineheader = "Case #";
	char* badmagician = "Bad magician!";
	char* badvolunteed = "Volunteer cheated!";
	int n; // bien luu tru so test cases
	fin >> n;

	for (int i=0; i< n; i++){

		int number1, number2; // row number of fist and second time.
		int matrix1[4][4] , matrix2[4][4], // matrix of arrangement
		possibility[4]; // cards of possibility

		// ---------- read input ----------
		fin >> number1;
//		if (number1 > 4 || number1 < 1){
//			cout << "Invalid argument. Row number is out of range." <<endl;
//			return 1;
//		}
		for (int j=0;j<4;j++){
			readMaxtrix(fin, matrix1[j]);
			if (number1-1 == j)
				copyArray(matrix1[j],possibility);
		}

		fin >> number2;
//		if (number2 > 4 || number2 < 1){
//					cout << "Invalid argument. Row number is out of range." <<endl;
//					return 1;
//				}
		for (int j=0;j<4;j++)
			readMaxtrix(fin,matrix2[j]);
		//------------end reading ------------

		//------------do computation for result ---------
		int count=0; // number of possible cards
		int result; // variable holds the card number.
		for (int j=0; j<4 ; j++){
			if (search(possibility[j], matrix2[number2-1])){
				count ++;
				result = possibility[j];
			}
		}
		//------------ consider the result ------------
		fout << lineheader << i+1 << ": ";
		switch (count){
		case 0: fout << badvolunteed << endl; break;
		case 1: fout << result << endl; break;
		default : fout << badmagician << endl;
		}

	}
	return 0;
}

int readMaxtrix(ifstream &instream, int a[]){
	for (int i=0; i <4 ; i++)
		instream >> a[i];
	return 0;
}

int copyArray(int src[], int des[]){
	for (int i=0;i<4;i++)
		des[i] = src[i];
	return 0;
}

//return 0 if not found, else otherwise
int search(int n, int array[]){
	for (int i = 0; i<4; i++){
		if (n == array[i])
			return 1;
	}
	return 0;
}

