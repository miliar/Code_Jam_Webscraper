#include <iostream>
#include <fstream>

using namespace std;


int main(){
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int t;
	fin >> t;

	for(int i = 1; i <= t; i++){
		int r, del, r1[4], temp;
		fin >> r;
		for(int j = 1; j < r; j++)
			for(int k = 0; k < 4; k++)
				fin >> del;
		for(int j = 0; j < 4; j++)
			fin >> r1[j];
		for(int j = r+1; j <= 4; j++)
			for(int k = 0; k < 4; k++)
				fin >> del;

		fin >> r;
		for(int j = 1; j < r; j++)
			for(int k = 0; k < 4; k++)
				fin >> del;
		int times = 0, num;
		for(int j = 0; j < 4; j++){
			fin >> temp;
			if(temp == r1[0] || temp == r1[1] || temp == r1[2] || temp == r1[3]){
				times++;
				num = temp;
			}
		}
		for(int j = r+1; j <= 4; j++)
			for(int k = 0; k < 4; k++)
				fin >> del;
		fout << "Case #" << i << ": ";
		if(times == 0)
			fout << "Volunteer cheated!\n";
		else if(times == 1)
			fout << num << "\n";
		else
			fout << "Bad magician!\n";
	}


	return 0;
}
