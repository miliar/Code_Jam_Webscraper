#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#define _USE_MATH_DEFINES 
#include <math.h> 
using namespace std;

int T;

long r,t;
int main()
{
	 
/*	freopen("A-small-attempt0", "r");
    freopen("a1.out", "w", stdout);
  */  
	ofstream fout;
	fout.open("a1.out");
	ifstream fin;
	fin.open("A-small-attempt1.in");
    fin >> T;
    for (int i = 1; i <= T; i++) {
        fin >> r >> t;
		long R = r+1;
		long c = 0;
		long S,lastS = 0;
       do{
		    
		   S = (R*R - (R-1)*(R-1))  + lastS; 
		   R = R+2;
		   c++;
		   lastS = S;

	   }while(S <= t);
        fout << "Case #" << i << ": ";
        fout <<c-1<<endl;
    }
	fout.close();
	fin.close();
    return 0;
}