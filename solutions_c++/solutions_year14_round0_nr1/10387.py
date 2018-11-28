#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

int main(){
	int T, ii;
	ifstream cin("A-small-attempt2.in");
//	ostream cout("A.out");
	ofstream outfile;
	//ifstream infile;
	//infile.open("A-small-attempt0.in");
	outfile.open("a.out");
	cin>> T;
	for (ii=1; ii<=T; ii++){
		int x, y, z;
		cin>> x;
		int i, j, k, m, n;
		int map1[5][5], map2[5][5];
		for (i=1; i<=4; i++)
			for (j=1; j<=4; j++){
				cin>> map1[i][j];
		}
		
		int a[5];
		for (i=1; i<=4; i++)
			a[i] = map1[x][i];
		
		cin>> y;
		for (i=1; i<=4; i++)
			for (j=1; j<=4; j++){
				cin>> map2[i][j];
		}
		int b[5];
		for (i=1; i<=4; i++)
			b[i] = map2[y][i];
		int flag=0, ans = 0;
		for (i=1; i<=4; i++)
			for (j=1; j<=4; j++){
				if (a[i] == b[j]){
					flag++;
					ans = a[i];
				}
		}
		outfile<< "Case #"<< ii<< ": ";
		if (flag == 1) outfile<< ans<< endl;
		if (flag > 1) outfile<< "Bad magician!"<< endl;
		if (flag == 0) outfile<< "Volunteer cheated!"<< endl;
	}
	cin.close();
	outfile.close();
	return 0;
}