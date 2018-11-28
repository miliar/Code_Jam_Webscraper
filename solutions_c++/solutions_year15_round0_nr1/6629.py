//============================================================================
// Name        : Standing_Ovation.cpp
// Author      : Yao Zhang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int addpeople(int shyness, int number,int time){
	int addnumber = 0;
	int *num = new int[shyness+1];
	for(int i=shyness; i>=0; i--){
		num[i] = number%10;
		number /= 10;
	}
	int alreadystand = num[0];;
	cout<<endl;
	for(int i=1;i<=shyness;i++){
		if(i > alreadystand){
			addnumber += i - alreadystand;
		//	cout<<"addnumber="<<addnumber<<endl;
			alreadystand = i+num[i];
		//	cout<<"alreadystand="<<alreadystand<<endl;
		}
		else
			alreadystand +=num[i];
	}
	cout<<"Case #"<<time+1<<": "<< addnumber<<endl;
	return addnumber;
}

int main() {
	int total;
	ifstream infile("input.txt");
	ofstream SaveFile("output.txt");
	if (infile.is_open()){
		int shyness;
		int number;
		int addnumber;
		infile>>total;
		for(int i=0; i<total; i++){
			infile>>shyness;
			infile>>number;
			addnumber = addpeople(shyness, number, i);
			SaveFile<<"Case #"<<i+1<<": "<< addnumber<<endl;
		}
		infile.close();
		SaveFile.close();
	}

	else{
			cout<<"Error,can't open...\n";
			exit(2);
	}
}
