//============================================================================
// Name        : codejam2014_1B1.cpp
// Author      : Mehmet Fatih Uslu
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <iomanip>
#include <cstring>
using namespace std;

int compare (const void *a, const void *b)
{
    const int *ia = (const int *)a; // casting pointer types
    const int *ib = (const int *)b;
    return *ia  - *ib;
}

int main() {

	int T=0;

	fstream inputFile, outputFile, logFile;

    inputFile.open("input",ios::in);
    outputFile.open("output",ios::out);
    logFile.open("log",ios::out);

    inputFile >> T;

    for(int dongu=1; dongu<=T; dongu++) {

    	int N = 0;
    	inputFile >> N;

    	string* dizi = new string[N];
    	int** intdizi = new int*[N];
    	char** ozetdizi = new char*[N];
    	int maxindex = 0;
    	int possible;
    	int step = 0;

    	for(int i=0;i<N;i++){

    		possible = 0;
    		inputFile >> dizi[i];
    		intdizi[i] = new int[100];
    		ozetdizi[i] = new char[100];

    		for(int j=0;j<100;j++)
    			intdizi[i][j] = 0;

    		int intindex = 0;

    		cout<<"case"<<dongu<<":"<<endl;

    		for(int j=0;j<dizi[i].size();){

    			int k=0;
    			do{
    				intdizi[i][intindex]++;
    				ozetdizi[i][intindex] = dizi[i][j];
    				k++;
    			}
    			while(j+k < dizi[i].size() && dizi[i][j]==dizi[i][j+k]);

    			intindex++;
    			j = j+k;
    		}

    		for(int j=0;j<intindex;j++){

    			cout<<intdizi[i][j];
    		}
    		cout<<endl;

    		if(maxindex==0){

    			maxindex = intindex;
    		}
    		else if(maxindex!=intindex){

    			possible = 0;
    			break;
    		}

    		possible = 1;
    	}

    	for(int j=0;j<maxindex;j++){

    		for(int k=0;k<N;k++){

    			if(ozetdizi[0][j]!=ozetdizi[k][j]){

    				possible = 0;
    			}
    		}
    	}

		for(int j=0;j<maxindex;j++){

			int sonuc = 0;
			int* yenidizi = new int[N];

			for(int k=0;k<N;k++){
				yenidizi[k] = intdizi[k][j];
			}
			qsort(yenidizi,N,sizeof(int),compare);

			for(int k=0;k<N;k++){

				sonuc+=abs(yenidizi[N/2]-yenidizi[k]);
			}
			step+=sonuc;
		}

    	outputFile << "Case #" <<dongu <<": ";

    	if(possible == 0)
    		outputFile <<"Fegla Won"<<endl;
    	else
    		outputFile <<step<<endl;
    }

	return 0;
}
