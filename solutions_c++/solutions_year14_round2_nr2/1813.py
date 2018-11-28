/*************************************************************************
    > File Name: B.cpp
    > Author: csy
    > Mail: chshaoyi7@gmail.com 
    > Created Time: Sun 04 May 2014 12:53:31 AM CST
 ************************************************************************/

#include<iostream>
#include<fstream>
using namespace std;

int main(){

	int t,a,b,k;
	int total;
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");

	fin >> t;
	for(int i = 1; i <= t; i ++){
		fin >> a >> b >> k;
		total = 0;

		for(int p = 0; p < a; p ++){
			for(int q = 0; q < b; q ++){
				if((p&q) < k) total ++;
			}
		}

		fout << "Case #" << i << ": " << total << endl;
	}
}
