#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
	fstream in, out;
	in.open("A-small-attempt4.in", ios::in);
	out.open("out.in", ios::out);
	int T, res, n, n1, count = 0;
	in >> T;
	int array1[4][4];
	int array2[4][4];
	for(int i=1 ; i<=T ; i++){
		in >> n;
		for(int j=0 ; j<4 ; j++){
			for(int k=0 ; k<4 ; k++)
				in >> array1[j][k];
		}
		in >> n1;
		for(int j=0 ; j<4 ; j++){
			for(int k=0 ; k<4 ; k++)
				in >> array2[j][k];
		}
		for(int j=0 ; j<4 ; j++){
			for(int k=0 ; k<4 ; k++){
				if(array1[n-1][j] == array2[n1-1][k]){
					count ++;
					res = array1[n-1][j];
					
				}
			}
		}
		if(count == 1)
			out << "Case #" << i << ": " << res << endl;
		else if(count > 1)
			out << "Case #" << i << ": " << "Bad magician!" << endl;
		else if(count == 0)
			out << "Case #" << i << ": " << "Volunteer cheated!" << endl;
			count = 0;
	}
}
