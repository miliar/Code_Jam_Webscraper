#include <fstream>
#include <string>
#include <stdio.h>
#include <iostream>
#include <cstdlib>
using namespace std;
int n;
int main(){
	ofstream fout ("StandingOvation.out");
	ifstream fin ("A-large.in");
	int x, add, current;
	string y;
	fin>>n;
	for(int i =0; i<n; i++){
		fin>>x>>y;
		current = add = 0;
		for(int j=0; j<x+1; j++){
			if(current<j){
				add += j-current;
				current += j-current;
			}
			current += atoi(y.substr(j,1).c_str());			
		}
		fout<< "Case #" << i+1 << ": " << add << endl;
	}
}