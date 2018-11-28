#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(){
	ifstream infile;
	infile.open("A-large.in");
	if (!infile.is_open()) cout << "Failed to load file!" << endl;

	ofstream outfile;
	outfile.open("output2.txt");
	int T;
	int N;
	infile >> T;

	for (int i = 1; i <= T; i++){
		infile >> N;
		outfile << "Case #" << i << ":";
		vector<int> A;
		int x, sum = 0, max, mp, max2, mp2;
		for (int j = 0; j < N; j++) { infile >> x;  A.push_back(x); }
		for (int j = 0; j < N; j++) { sum +=  A[j]; }
		while (sum > 0){
			max = A[0]; mp = 0; max2 = A[1]; mp2 = 1;
			for (int j = 1; j < N; j++) { if (A[j] > max) { max = A[j]; mp = j; } }
			for (int j = 0; j < N; j++) { if (A[j] >= max2 && j != mp) { max2 = A[j]; mp2 = j; } }
			if (sum - 2 == 1) { outfile << " " << char(65 + mp); sum--; A[mp]--; }
			else if (max == max2) { outfile << " " << char(65 + mp) << char(65 + mp2); sum -= 2; A[mp]--; A[mp2]--; }
			else { outfile << " " << char(65 + mp); sum--; A[mp]--; }
		}
		outfile << endl;
	}
	infile.close();
	outfile.close();
	system("pause");
	return 0;
}