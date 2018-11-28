#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>
#include <stdlib.h>
using namespace std;

fstream in ("/home/m/Google Code JAM C/test.txt");
int dim;
string A;
int main(){
	in>>dim;
	unsigned long long m[dim][2];
	unsigned int n[dim];
	for(int i=0; i<dim; i++){
		in>>m[i][0];
		in>>m[i][1];
	}

	for(int i=0; i<dim; i++){
		n[i]=0;
		for(long long a=m[i][0], b=m[i][1]; a<=b; a++){
			stringstream ss; ss<<a; ss>>A;
			if(A==string(A.rbegin(), A.rend())){
				stringstream ss; ss<<sqrt(a); ss>>A;
				if(A==string(A.rbegin(), A.rend())) n[i]++;
			}
		}
		cout << "Case #" << i+1 << ": " << n[i] << endl;
	}
	return 0;
}