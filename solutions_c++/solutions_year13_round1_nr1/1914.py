#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>
#include <utility>
#include <fstream>

using namespace std;

typedef  unsigned int uint;



void main()
{
    uint t,tidx;
	uint i,j,k;
	double r,vol,consm,r1,r2,cnum;

	fstream testfin,testfout;

    testfout.open("out.txt",ios::out);
	testfin.open("A-small-attempt1.in",ios::in);

    testfin >> t;
	
	for(tidx = 1;tidx < (t+1);tidx++)
	{
	    consm = 0;cnum = 0;
		
	    testfin >> r;
		testfin >> vol;
		
		r1 = r;
		r2 = r+1;

		while(consm <= vol)
		{
		    consm = consm+r2*r2-r1*r1;

			r1 = r1+2;
			r2 = r2+2;

			cnum++;
			
		}

		cnum--;

		
	    testfout << "Case #" << tidx << ": " <<cnum<<endl;
 
	}

	
}