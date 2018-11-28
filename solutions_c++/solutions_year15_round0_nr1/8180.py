// SO.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <fstream>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T, *m;
	string *M;
    string strT, i;
	
	std::ifstream infile("C:\\CG\\SO\\Debug\\A-small-attempt0.in");
	std::ofstream outfile("C:\\CG\\SO\\Debug\\A-small-attempt0.out");

    getline (infile, strT);
    try
    {
        T = stoi(strT);
    
        m = new int[T];
        M = new string[T];
    
        for(int j = 0; j < T; j++)
        {
			getline (infile, i);
            vector<string> minMax;
            istringstream ss(i);
            copy(istream_iterator<string>(ss),
            istream_iterator<string>(),
            back_inserter(minMax));
            m[j] = stoi(minMax[0]);
            M[j] = minMax[1];
        }
        
        
        for(int j = 0; j < T; j++)
        {
			int standingPeople = 0;
			int extraPeople = 0;
           for(int k = 0; k <= m[j]; k++)
		   {
			   if((M[j][k] - '0') > 0)
			   {
				   int diff = k - standingPeople; 

				   if( diff > 0)
				   {
						extraPeople += diff;
						standingPeople += diff;
				   }
			   }

			   standingPeople += (M[j][k] - '0');
			  
		   }
           outfile << "Case #" << j+1 <<": " << extraPeople << endl;     
        }
		outfile.close();
    }
    catch(...)
    {
        return 0;
    }
}
