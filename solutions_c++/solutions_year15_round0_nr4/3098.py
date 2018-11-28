#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int main(){

	long long int t, r, c, k, x;

	ifstream fin("D-small-attempt0.in");
	ofstream fout("test.out");

	//initialize possibilty matrix
	int a[5][5][5];

	a[1][1][1] = 1;
	a[1][1][2] = 1;
	a[1][1][3] = 1;
	a[1][1][4] = 1;
	a[1][2][2] = 1;
	a[1][2][3] = 1;
	a[1][2][4] = 1;
	a[1][3][3] = 1;
	a[1][3][4] = 1;
	a[1][4][4] = 1;
	//
	a[2][1][1] = 0;
	a[2][1][2] = 1;
	a[2][1][3] = 0;
	a[2][1][4] = 1;
	a[2][2][2] = 1;
	a[2][2][3] = 1;
	a[2][2][4] = 1;
	a[2][3][3] = 0;
	a[2][3][4] = 1;
	a[2][4][4] = 1;
	//
	a[3][1][1] = 0;
	a[3][1][2] = 0;
	a[3][1][3] = 0;
	a[3][1][4] = 0;
	a[3][2][2] = 0;
	a[3][2][3] = 1;
	a[3][2][4] = 0;
	a[3][3][3] = 1;
	a[3][3][4] = 1;
	a[3][4][4] = 0;
	//
	a[4][1][1] = 0;
	a[4][1][2] = 0;
	a[4][1][3] = 0;
	a[4][1][4] = 0;
	a[4][2][2] = 0;
	a[4][2][3] = 0;
	a[4][2][4] = 0;
	a[4][3][3] = 0;
	a[4][3][4] = 1;
	a[4][4][4] = 1;

	fin>>t;
	for(k=1;k<=t;k++){
		fin>>x;
		fin>>r;
		fin>>c;
		if(r>c)
			swap(r,c);
		fout<<"Case #"<<k<<": "<<(a[x][r][c]?"GABRIEL":"RICHARD")<<"\n";
	}
	fin.close();
	fout.close();
	return 0;
}