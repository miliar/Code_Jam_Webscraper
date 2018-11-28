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

bool seen[10];
    
void addSeen(unsigned long long int x) {
	while (x>0) {
		seen[x%10] = true;
		x/=10;
	}
}

bool allSeen() {
	bool out;
	int i;
	out = true;
	forn(i,10)  out = out && seen[i];
	return out;
}
bool allZeros() {
	bool out;
	int i;
	out = false;
	forn(i,10)  out = out || seen[i];
	return !out;
}

int main() {

    ifstream fin ("input.txt");
    ofstream fout ("output.out");
    
    int i,j,k,t,T,B,out;
    unsigned long int N;
    bool done;
   
    fin >> T;
    
    forn1(t,T) {
    	memset(seen,false,10);
    	
    	fin>>N;
		
		done = false;
		for(j=1;j<=10000000 && !done;j++) {
			addSeen(N*j);
			cout << N*j << ' ';
			forn(k,10) cout <<seen[k];
			cout <<'\n';
			if (allSeen()) done = true;
			if (allZeros()) done = true;
		}
		j--;
    
        fout<<"Case #"<<t<<": ";
        
        if (allSeen()) {
        	fout << (unsigned long long int)j*N << '\n';
        } else {
        	fout << "INSOMNIA\n";
        }
    
    }
    
    fin.close();
    fout.close();
    return 0;
}
