#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
using namespace std;

int main(){
	char data[30], temp[10];
	int t = 0, i, s = 0, j;
	ifstream infile; 
	ofstream outfile;
    outfile.open("output3.txt");

	infile.open("A-small-attempt2.in");
	infile >> data; 
	t = atoi(data);
	for(i = 0; i<t; i++){
		int f=0, shy, x =0, total = 0;
		infile >> temp;
		infile >> data;
		s = atoi(temp);

		if(s == 0){
			outfile<<"Case #"<<i+1<<": "<<"0\n";
		}
		else{
			for(j =0; j<s+1; j++){
				shy = data[j]-'0';
				
				if(shy != 0){
					x = x+1;		
					if(j > total+f){
						f = j-total;
					}
					
					
				}
				total += shy;
			}
			outfile<<"Case #"<<i+1<<": "<<f<<endl;
		}

	}
}