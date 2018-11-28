// gcjqa.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <set>
#include "InfInt.h"

using namespace std;

InfInt findDiv(InfInt n, int max=55){
	InfInt root=n.intSqrt();
	if (root > max)
		root = max;
	for (InfInt i=2; i<=root; i++){
		if (n%i==0)
			return i;
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream a("D:\\gcj\\C-large.in");
	ofstream o("D:\\gcj\\output.txt");
	int nr; a>>nr;
	for (int i=0; i<nr; i++){
		set<char> h;
		o << "Case #" << (i+1) << ": " << endl;
		cout << "Case #" << (i+1) << ": " << endl;
		int jjj=0;
		int n, j; a >> n >> j;
		string s(n-2, '0');
		s.insert(s.begin(), '1');
		s.insert(s.rbegin().base(), '1');
		char *endp = NULL;
		char buf[1024];
		int start=strtoul(s.c_str(), &endp, 2);
		while (jjj<j){
			itoa(start, buf, 2);
			s=string(buf);
			if (s.size()>n) break;
			string line=s;
			int jj=2;
			for (; jj<=10;jj++){
				InfInt sj = InfInt::fromString(s, jj);
				//cout << "sj: " << sj << " jj: " << jj << " s: " << s << endl;
				InfInt div=findDiv(sj);
				if (div != 0){					
					line.append(" ");
					line.append(InfInt::toString(div, 10));
				}
				else
					break;
			}
			if (jj>10){
				o << line.c_str() << endl;
				cout << line.c_str() << endl;
				jjj++;
			}
			start +=2;
		}
	
	}
	a.close();
	o.close();
	return 0;
}

