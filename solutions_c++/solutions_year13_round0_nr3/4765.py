//============================================================================
// Name        : CJam3.cpp
// Author      : Daniel Gomez
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <math.h>

using namespace std;

bool isPalindrom(int a);
short orden(int a);
bool raiz_exacta(int a);

int main(void) {

	 ifstream myReadFile;
	 ofstream myWriteFile;
	 int T, A, B, N;

	 myReadFile.open("C-small-attempt0.in");
	 myWriteFile.open("C-small-attempt0.out");
	 if (myReadFile.is_open()) {
		 myReadFile >> T;
		 for(int i=0; i<T; i++){
			 myReadFile >> A;
			 myReadFile >> B;
			 N=0;
			 for(int j=A; j<=B;j++)
				 if(isPalindrom(j) && isPalindrom((int)sqrt(j)) && raiz_exacta(j))
					 N++;

			 printf("Case #%i: %i \n", (i+1), N);
			 myWriteFile << "Case #"<< (i+1) <<": "<< N <<" \n";
		 }
	}
	myReadFile.close();
	myWriteFile.close();


	system("pause");
	return EXIT_SUCCESS;
}

bool isPalindrom(int a){
	int o = orden(a);
	char  buf1[o+1];
	char  buf2[o+1];
	snprintf(buf1, sizeof(buf1), "%d", a);
	for(int i=0;i<o;i++) buf2[i] = buf1[o-1-i];
	for(int i=0;i<o-1;i++) if(buf2[i] != buf1[i]) return false;
	return true;
}

bool raiz_exacta(int a){
	if(sqrt(a) - (int)sqrt(a) == 0 ) return true;
	return false;
}

short orden(int a){
	if(a<10) return 1;
	else if(a<100) return 2;
	else if(a<1000) return 3;
	else if(a<10000) return 4;
	else if(a<100000) return 5;

	return 0;
}


