#include <fstream>
#include <iostream>
#include <stdlib.h>
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
#if 0
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
}
#endif
#if 1

int cmp(const void * pa, const void * pb){
	double re;
	re = (*(double*)pa) - (*(double*)pb);
	if (re > 0.0)
		return -1;
	else if (re == 0.0)
		return 0;
	else
		return 1;
}

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");

	int n;
	fin >> n;

	double a_1[2000];
	double a_2[2000];

	for (int i = 0; i < n; i++){
		int bar_count;
		fin >> bar_count;
		for (int j = 0; j < bar_count; j++){
			fin >> a_1[j];
		}

		for (int j = 0; j < bar_count; j++){
			fin >> a_2[j];
		}
		qsort(a_1, bar_count, sizeof(double), cmp);
		qsort(a_2, bar_count, sizeof(double), cmp);


		int answer_1 = 0;
		int answer_2 = 0;

		int k = 0;
		for (int j = 0; j < bar_count; j++){
			if (a_1[k] > a_2[j]){
				k++;
				answer_1++;
			}
			else {
				continue;
			}
		}
		k = 0;
		for (int j = 0; j < bar_count; j++){
			if (a_2[k] > a_1[j]){
				k++;
			}
			else {
				answer_2++;
				continue;
			}
		}

		fout << "Case #" << i+1 << ": "<< answer_1 << " " << answer_2 << endl;
		
		
		
	}
}
#endif