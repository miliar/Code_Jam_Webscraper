// Qual 1a Magic Trick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in;
	ofstream out;

	int T,row1,row2,cnum,card;

	in.open(argv[1]);
	out.open("output.txt");

	in >> T;
	for(int i=1;i<=T;++i) {
		int cards[17]={0};
		int counter=0;
		in >> row1;
		for(int j=1;j<row1;++j) {
			in >> cnum >> cnum >> cnum >> cnum;
		}
		for(int j=0;j<4;++j) {
			in >> cnum;
			cards[cnum]=1;
		}
		for(int j=row1;j<4;++j) {
			in >> cnum >> cnum >> cnum >> cnum;
		}

		in >> row2;
		for(int j=1;j<row2;++j) {
			in >> cnum >> cnum >> cnum >> cnum;
		}
		for(int j=0;j<4;++j) {
			in >> cnum;
			if(cards[cnum]==1) {
				card=cnum;
				counter++;
			}
		}
		for(int j=row2;j<4;++j) {
			in >> cnum >> cnum >> cnum >> cnum;
		}
		out << "Case #" << i << ": ";
		if(counter==1) {
			out << card << endl;
		}
		if(counter>1) {
			out << "Bad magician!" << endl;
		}
		if(counter<1) {
			out << "Volunteer cheated!" << endl;
		}

	}

	in.close();
	out.close();
	return 0;
}

