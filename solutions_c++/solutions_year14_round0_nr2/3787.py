#include <fstream>
#include <iostream>
using namespace std;
#if 0


int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int n;
	fin >> n;

	int arr[4];
	int count = 0;
	int answer;

	int row;
	for (int i = 0; i < n; i++){
		fin >> row;
		int temp;
		count = 0;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				fin >> temp;
				if (j == row-1){
					arr[count++] = temp;
				}
			}
		}
		fin >> row;
		count = 0;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				fin >> temp;
				if (j == row-1){
					for (int l = 0; l < 4; l++){
						if (arr[l] == temp){
							answer = temp;
							count++;
						}
					}
				}
			}
		}
		fout << "Case #" << i+1 << ": ";
		if (count == 0){
			fout << "Volunteer cheated!" << endl;
		}
		else if (count == 1){
			fout << answer << endl;
		}
		else {
			fout << "Bad magician!" << endl;
		}
	}
}
#endif
#if 1
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	
	int n;
	fin >> n;

	double c=0;
	double f=0;
	int f_c = 0;
	double x=0;
	
	for (int i = 0; i < n; i++){
		f_c = 0;
		fin >> c;
		fin >> f;
		fin >> x;
		double total = 0;
		while (x / (2 + f * f_c) > c / (2 + f * f_c) + x / (2 + f * (f_c + 1))){
			total += c / (2  + f * f_c);
			f_c++;
		}
		total += x / (2 + f * f_c);
		fout.precision(7);
		fout.setf(ios_base::fixed, ios_base::floatfield);
		fout << "Case #"<<i+1<<": " << total << endl;
	}
	
	fin >> n;
}
#endif