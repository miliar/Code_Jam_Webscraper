// gcjqa.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <set>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream a("D:\\gcj\\A-large.in.sdx");
	ofstream o("D:\\gcj\\output.txt");
	int nr; a>>nr;
	for (int i=0; i<nr; i++){
		set<char> h;
		o << "Case #" << (i+1) << ": ";
		int base; a >> base;
		int d=0;
		int c=0;
		while(h.size()<10 && c <10000){
			d+=base;
			char buffer[1024];
			itoa(d, buffer, 10);
			string s(buffer);
			for (string::iterator it=s.begin(); it!=s.end(); it++){
				h.insert(*it);
			}
			//cerr << c << " " << endl;
			c++;
		}
		if (c>=10000){
			o << "INSOMNIA" <<endl;
		}
		else
			o << d << endl;

	}
	a.close();
	o.close();
	return 0;
}

