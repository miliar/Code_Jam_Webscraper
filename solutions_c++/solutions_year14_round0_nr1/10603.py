


#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int A[4][4];
int a1[4];
int a2[4];



int answer(string& error){
	int res = -1;

	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			if(a1[i] == a2[j]){
				if(res == -1) res = a1[i];
				else{
					error = "Bad magician!";
					return -1;
				}
			}
		}
	}

	if(res == -1) error = "Volunteer cheated!";
	return res;
}


int main(){
	ifstream fin;
	ofstream fout;
	fout.open("output.txt");
	fin.open("input.txt");

	int T,n;
	string error;
	fin>>T;
	for(int i=0; i<T; i++){
		fin>>n;
		for(int j=0; j<4; j++)
			for(int k = 0; k<4; k++)
				fin>>A[j][k];
		for(int j=0; j<4; j++){
			a1[j] = A[n-1][j];
		}
		fin>>n;
		for(int j=0; j<4; j++)
			for(int k = 0; k<4; k++)
				fin>>A[j][k];
		for(int j=0; j<4; j++){
			a2[j] = A[n-1][j];
		}


		int res = answer(error);
		if(res == -1)
			fout<<"Case #"<<i+1<<": "<<error<<endl;
		else fout<<"Case #"<<i+1<<": "<<res<<endl;

	}



	return 0;
}




