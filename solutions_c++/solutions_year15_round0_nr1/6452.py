// Ahmed Refaay
// Standing Ovation
# include <iostream>
# include <array>
# include <fstream>
# include <string>
using namespace std;
int main (){
	ifstream inFile;  // object for reading from a file
    ofstream outFile; // object for writing to a file
	char inputFilename[] = "A-large.in";
    char outputFilename[] = "abcdef.txt";
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
	string numbers[2001];
	int q=0;
	while (!inFile.eof()) {
    inFile >> numbers[q];
	q++;
    }
	int T=stoi(numbers[0]),i=0,j=0,max=0,k=0,need=0,m=0,n=0,total=0;
	string people;
	while (i < T){
	max = stoi(numbers[j+1]);
	people = numbers[j+2];
	while (k<=max){
	m=people[k]-'0';
	need=k;
	if (need>n){
	total=total+need-n;
	n+=(need-n);
	}
	k++;
	n+=m;
	}
	outFile<<"Case #"<<i+1<<": "<<total<<endl;
	i++;
	j+=2;
	max=0;k=0;need=0;m=0;n=0;total=0;
	}
	inFile.close();
	outFile.close();
	cout<<"Done"<<endl;
	system("pause");
}