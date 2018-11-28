#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forn1(i, n) for (int i = 1; i <= (int)(n); i++)

int countFlips(string B) {

	int i,l,count;
	char c;
	
	l = B.length();
	c = '.';
	count = 0;
	forn(i,l) 
		if (B[i]!=c){
			c = B[i];
			count++;	
		}
	
	return count;

}

int main() {

    ifstream fin ("input.txt");
    ofstream fout ("output.out");
    
    int i,j,k,t,T,N,out,l;
    string B;
   
    fin >> T;
    
    forn1(t,T) {
    
		fin >> B;
		
		k = countFlips(B);
		if (B[B.length()-1]=='+') k--;

        fout<<"Case #"<<t<<": "<<k<<'\n';
    
    }
    
    fin.close();
    fout.close();
    return 0;
}
