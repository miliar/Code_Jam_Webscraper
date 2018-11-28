#include <iostream>
#include <fstream>
using namespace std;

int same_num(int arr1[], int arr2[], int *num) 
{
	int i, j;
	int res = 0;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (arr1[i] == arr2[j]) {
				res++;
				*num = arr1[i];
			}
		}
	}
	return res;
}

int main()
{
	int casenum;
	int card[4][4];
	int ans1, ans2;
	int row, col;
	int card_sel1[4];
	int card_sel2[4];

	ifstream fin("A-small-attempt1.in");
	ofstream fout("result2.out");

	fin >> casenum;
	for (int i = 1; i <= casenum; i++) {

		//first
		fin >> ans1;
		for (row = 0; row < 4; row++) {
			for (col = 0; col < 4; col++) {
				fin >> card[row][col];
			}
		}

		for (col = 0; col < 4; col++)
			card_sel1[col] = card[ans1 - 1][col];


		//second
		fin >> ans2;
		for (row = 0; row < 4; row++) {
			for (col = 0; col < 4; col++) {
				fin >> card[row][col];
			}
		}

		for (col = 0; col < 4; col++)
			card_sel2[col] = card[ans2 - 1][col];


		//solution
		int card_chosen;
		int solution = same_num(card_sel1, card_sel2, &card_chosen);
		if (solution == 1) {
			fout << "Case #" << i << ": " << card_chosen << endl;
		}
		else if (solution == 0) {
			fout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
		}
		else {
			fout << "Case #" << i << ": " << "Bad magician!" << endl;
		}

	}

	
	return 0;
}