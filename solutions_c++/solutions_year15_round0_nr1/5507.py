//============================================================================
// Name        : opera.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main() {

	ifstream myfile ("example.txt");
	ofstream output;
	output.open("output.txt");
	int Nb;
	myfile>>Nb;
	for (int i=1;i<=Nb;i++)
	{
		output<<"Case #"<<i<<": ";
		int max;
		char c;


		myfile>>max;
		int v[max];
		int stand=0;
		int nbfriend=0;
		for (int j=0;j<=max;j++)
		{
		myfile>>c;
		v[j]=(int) c-'0';
		stand=stand+v[j];
		if(stand<=j)
		{
			nbfriend++;
			stand++;
		}

		}
		output<<nbfriend<<endl;

	}
	return 0;
}
