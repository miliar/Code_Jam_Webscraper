#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;


main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for(int c=1; c<=t; c++){
		int s;
		fin >> s;
		string line;
		fin >> line;
		string waste;
		getline(fin, waste);

		int sum=0, count=0;//count for counting to the current pos
	  	for(int i=0; i<=s; i++){
			count += (line[i]-'0');
			if(count<i+1){
				count++;
				sum++;
			}
		}
		fout << "Case #" << c << ": " << sum << endl;
	}
	system("pause");
}
