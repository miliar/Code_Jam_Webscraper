#include <iostream>
#include <fstream>
using namespace std;
main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");	
	unsigned long long a, b, k, count=0;
	int time;
	fin >> time;
	for(int c=1; c<=time; c++){
		fin >> a >> b >> k;
		count=0;
		for(unsigned long long i=0; i<a; i++){
			for(unsigned long long j=0; j<b; j++){
				if((i&j)<k){
					count++;
				}
			}
		}
		fout << "Case #"<< c <<": "<<count<<endl;
	}
	
}
