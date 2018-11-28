#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
using namespace std;

int main(){
	char data[1000], temp[1000];
	int t = 0, i, s = 0;
	ifstream infile; 
	ofstream outfile;
    outfile.open("output3.txt");
	infile.open("B-small-attempt0.in");
	infile >> data; 
	t = atoi(data);
	for(i = 0; i<t; i++){
		int d=0, j, p[1000], max=0, k=0;
		int min = 0,d1 = 0;
		int m = 100000;
		int time1;
		infile >> data;
		d = atoi(data);
		for(j=0; j<d; j++)
			infile >> temp[j];
		for(j=0; j<d; j++)
			p[j] = temp[j] - '0';
		if(d == 1 && p[0] <= 3)
			outfile<<"Case #"<<i+1<<": "<<p[0]<<"\n";
		else{
			max = p[0];
			k=0;
			for(j=1; j<d;j++){
				if(max<p[j]){
					max = p[j];
					k=j;	
				}		
			}	
			if(max <= 3){
				outfile<<"Case #"<<i+1<<": "<<max<<"\n";
			}
			else{
				for(j = 1;j < max; j++){
					min = 0;
					for(k = 0; k < d; k++){
						d1 = p[k]/j;
						if(p[k] % j == 0){
							d1--;
						}
						min += d1;
						
					}
			time1 = min + j;
			if(time1 < m)
				m = time1;
			}
			if(max < m)
				m = max;
			outfile<<"Case #"<<i+1<<": "<<m<<"\n";	

			}
					
		}

	}
}