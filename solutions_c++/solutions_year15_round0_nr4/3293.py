// Ahmed Refaay
// Pancakes
# include <iostream>
# include <array>
# include <fstream>
# include <string>
using namespace std;
int main (){
	ifstream inFile;  // object for reading from a file
    ofstream outFile; // object for writing to a file
	char inputFilename[] = "D-small-attempt0.in";
    char outputFilename[] = "abcd.txt";
	inFile.open(inputFilename, ios::in);
    if (!inFile) {
       cerr << "Can't open input file " << inputFilename << endl;
       exit(1);
    }
    outFile.open(outputFilename, ios::out);
    if (!outFile) {
       cerr << "Can't open output file " << outputFilename << endl;
       exit(1);
    }
	string numbers[1000];
	int q=0;
	while (!inFile.eof()) {
    inFile >> numbers[q];
	q++;
    }
	int T=stoi(numbers[0]),j=1,i=0,X=0,R=0,C=0,grid=0;
	string winner;
	while (i < T){ // To get all test cases
		X = stoi(numbers[j]);j++;
		R = stoi(numbers[j]);j++;
		C = stoi(numbers[j]);j++;
		grid=R*C;
		if (grid%X==0){
			if (X==1){winner="GABRIEL";}
			else if (grid>=(X*(X-1))) {winner="GABRIEL";}
			else {winner="RICHARD";}
		}
		else {winner="RICHARD";}
	outFile<<"Case #"<<i+1<<": "<<winner<<endl;
	i++;	
	}
	inFile.close();
	outFile.close();
	cout<<"Done"<<endl;
	system("pause");
}