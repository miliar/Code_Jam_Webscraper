#include <iostream>
using namespace std;

int MatchRows(int arr1[4][4], int row1, int arr2[4][4], int row2) {
	int ans = -2;
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++) {
			if (arr1[row1][i] == arr2[row2][j]) {
				if (ans != -2)
					return -1;
				else
					ans = arr1[row1][i];
			}
		}
	return ans;
		
}

int PerformMagic(){
	int first_answer;
	cin>>first_answer;
	int firstcards[4][4];
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			cin>>firstcards[i][j];
	int second_answer;
	cin>>second_answer;
	int secondcards[4][4];
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			cin>>secondcards[i][j];
	return MatchRows(firstcards, first_answer-1, secondcards, second_answer-1);
}

int main() {
	int testcases;
	cin>>testcases;
	for (int i=0; i<testcases; i++) {
		cout<<"Case #"<<i+1<<": ";
		int status = PerformMagic();
		if (status == -1)
			cout<<"Bad magician!";
		else if (status == -2)
			cout<<"Volunteer cheated!";
		else
			cout<<status;
		cout<<endl;
	}
	return 0;
}