#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forn1(i, n) for (int i = 1; i <= (int)(n); i++)

  	bool coin[32];
/*
    set<unsigned long int> primes;
  	std::set<int>::iterator it;
    
void loadPrimes() {
	unsigned long int i;

	ifstream primesIn("primes.txt");
	
	while(!primesIn.eof()) {
		primesIn >> i; 
		primes.insert(i);
	}

}

void inNum(unsigned long num) {
	int i;
	
	forn1(i,14) {
		coin[i]=num%2;
		num/=2;
	}

}

void printCoin() {
	int i;
	forn(i,16) cout << coin[15-i];
	cout << '\n';
}

unsigned long int coinBase(int base) {
	int i;
	unsigned long int out;

	out = 0;
	forn(i,16) out += coin[i]*pow(base,i);
	
	return out;
}*/

int main() {

    ifstream fin ("input.txt");
    ofstream fout ("output.out");
    
    int j,k,t,T,B,N,out,J,b,count,i,c;
    bool valid;
    bool a[15];
    
    fin >> T;
    
    forn1(t,T) {
    
    	fin>>N>>J;
    
		//loadPrimes();
		fout<<"Case #1:\n";
				
		count = 0;
		for(i=1;i<pow(2,15) && count<500;i++) {
			memset(a,false,15);
			memset(coin,false,31);
			coin[0]=coin[31]=true;;
			
			b = i;
			c = 0;
			while (b>0) {
				a[c] = b%2;
				b/=2;
				c++;
			}
			
			//cout <<count<< ' ';
			for(j=0;j<15&&count<500;j++) {
				if (a[j]) {
					coin[1+j*2] = true;
					coin[1+j*2+1] = true;
				}
			}
			
				forn(k,32) fout<<coin[k];
				fout<<" 3 2 5 2 7 2 3 2 11\n";
			
				count++;

    	}
    
    }
    
    fin.close();
    fout.close();
    return 0;
}
