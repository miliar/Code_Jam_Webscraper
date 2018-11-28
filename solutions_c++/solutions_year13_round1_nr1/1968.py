#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <stdlib.h>
using namespace std;

int main() {

	int x,T,count=0,op;
	int r,t;

    ofstream fout("D:\\eclipse\\gcj-1a\\Debug\\A-small-attempt0.out");
    ifstream fin("D:\\eclipse\\gcj-1a\\Debug\\A-small-attempt0.in");

   	fin>>T;
    for(x=1;x<=T;x++){
		fin>>r;
		fin>>t;
		r++;
		op=(r*r)-((r-1)*(r-1));
		while(op <= t)
		{
				t=t-op;
				count++;
				r=r+2;
				op=(r*r)-((r-1)*(r-1));
		}
		fout<<"Case #"<<x<<": "<<count<<endl;
		count=0;
	}

    fout.close();
    fin.close();
   	return 0;
}
