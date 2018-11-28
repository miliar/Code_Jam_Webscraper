#include<iostream>
#include<fstream>

using namespace std;

void main(){

	fstream fin;
	fin.open("A-small-attempt0.in", ios::in);

	fstream fout;
	fout.open("output.txt", ios::out);

	int N;
	fin>>N;

	for(int z=0 ; z < N ; z++){

		int r1;
		fin>>r1;
		--r1;
		int arr1[4][4];
		for(int i=0 ; i < 4 ; i++){
			for(int j=0 ; j<4 ; j++){
				fin>>arr1[i][j];
			}
		}

		int r2;
		fin>>r2;
		--r2;
		int arr2[4][4];
		for(int i=0 ; i < 4 ; i++){
			for(int j=0 ; j<4 ; j++){
				fin>>arr2[i][j];
			}
		}


		int matches = 0;
		int card = 0;
		for(int i=0 ; i< 4 ; i++){
			for(int j=0 ; j<4 ; j++){
				if(arr1[r1][i] == arr2[r2][j]){
					matches++;
					card = arr1[r1][i];
					break;
				}
			}
		}

		if(matches == 0){
			fout<<"Case #"<<z+1<<": Volunteer cheated!"<<endl;
		}
		else if(matches == 1){
			fout<<"Case #"<<z+1<<": "<<card<<endl;
		}
		else{
			fout<<"Case #"<<z+1<<": Bad magician!"<<endl;
		}

	}


}