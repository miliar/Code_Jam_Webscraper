/*
 * goo1.cpp
 *
 *  Created on: 11/04/2015
 *      Author: facundo
 */

#include <iostream>
#include <fstream>


using namespace std;



ifstream fin ("goo1.in");
ofstream fout ("goo1.out");

int pot (int base, int exp){
	int n=1;
	for (int i=0 ; i<exp ; i++){
		n*=base;
	}
	return n;
}

int  todo(){
	int S;
	fin >> S;//cout << "hey"<<S;
	int s=S;
	int str ;
	fin >> str;
	int amigos=0;
	int parados=0;
	int necesitoParados=0;
	while (necesitoParados<=S){
		//cout << "hh"<<necesitoParados<<"hh";
		if (parados<necesitoParados){
			amigos += necesitoParados-parados;
			parados=necesitoParados;
		}
		parados += int(str/(pot(10,s)));
		//cout << parados << " ";
		str = str%(pot(10,s));
		//cout << "str="<<str ;
		s--;
		necesitoParados++;
	}
	return amigos;
}

int main(){
	int N;
	fin >> N;
	int i=0;
	while (i<N){
		fout << "Case #"<<i+1<<": "<<todo() << endl;
		i++;
	}



	return 0;
}


