#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int arr1[4][4], arr2[4][4],test_cases,ans1,ans2,i,j,k,count,found;
	ifstream fin("int.in");
	ofstream fout("Q1_Output.txt");
	fin >> test_cases;
	for (i = 0; i < test_cases; i++){
		count = 0;
		fin >> ans1;
		for (j = 0; j < 4; j++){
			for (k = 0; k < 4; k++)
				fin >> arr1[j][k];
		}

		fin >> ans2;
		for (j = 0; j < 4; j++){
			for (k = 0; k < 4; k++)
				fin >> arr2[j][k];
		}

		for (j = 0; j < 4; j++){
			for (k = 0; k < 4; k++){
				if (arr1[ans1 - 1][j] == arr2[ans2 - 1][k]){
					found = arr1[ans1 - 1][j];
					count++;
				}
			}
		}
		fout << "Case #"<<i+1<<": ";
		if (count == 0)
			fout << "Volunteer Cheated!\n";
		else if (count == 1)
			fout << found << endl;
		else if (count >1)
			fout << "Bad magician!\n";
	}
	system("pause");
	return 0;
}