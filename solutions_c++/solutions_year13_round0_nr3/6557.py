
#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;
bool Check(int a){
	int	wei = int(log10(a) + 1),
		i;
	char str[4];
	sprintf(str,"%d",a);
	for(i=0; i<wei/2; i++){
		if(str[i]!=str[wei-1-i])return false;
	}
	return true;
}
int main(){
	ifstream input("C-small-attempt0.in");
	ofstream output("out.out");
	int T, i, j, count,
		A, B, sA, sB;
	input>>T;
	for(i=1; i<=T; i++){
		input>>A>>B;
		sA = int(ceil(sqrt(A)));
		sB = int(floor(sqrt(B)));
		count = 0;
		for(j=sA; j<=sB; j++){
			if(Check(j)){
				if((j*j<=B)&&Check(j*j)){count++;} 
			}
		}
		output<<"Case #"<<i<<": "<<count<<endl;
	}
	input.close();
	output.close();
	return 0;
}
