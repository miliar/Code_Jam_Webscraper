#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream infile ("input.txt");
	ofstream outfile ("output.txt");

	int t, count=0, i=0;
	char prev;
	infile >> t;
	char N[100];
	for (int k=0; k<t; k++){
		infile >> N;

		prev = N[0];
		i=0;
		count=0;
		while(N[i]!='\0'){
			i++;
			if(N[i]==prev){
				continue;
			}
			else if(N[i]!=prev){
				count++;
				prev = N[i];
			}
		}

		if (N[i-1]=='+'){
			count=count-1;
		}

		outfile <<"case #"<<(k+1)<<": "<<count<<endl;
	}
}