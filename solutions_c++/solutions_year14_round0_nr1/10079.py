#include <iostream>
#include <vector>
#include <conio.h>

using namespace std;

void main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		int firstAnswer;
		cin >> firstAnswer;
		firstAnswer--;
		int** firstcards = new int*[4];
		for (int j = 0; j < 4; ++j) {
			firstcards[j] = new int[4];
		}
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				cin >> firstcards[j][k];
			}
		}
		int secondAnswer;
		cin >> secondAnswer;
		secondAnswer--;
		int** secondcards = new int*[4];
		for (int j = 0; j < 4; ++j) {
			secondcards[j] = new int[4];
		}
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				cin >> secondcards[j][k];
			}
		}
		vector<int> answers;
		answers.push_back(firstcards[firstAnswer][0]);
		answers.push_back(firstcards[firstAnswer][1]);
		answers.push_back(firstcards[firstAnswer][2]);
		answers.push_back(firstcards[firstAnswer][3]);
		int answer = -1;
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				if (secondcards[secondAnswer][j] == answers[k]) {
					if (answer == -1) {
						answer = answers[k];
					}
					else {
						cout << "Case #" << i + 1 << ": Bad magician!" << endl;
						goto end;
					}
				}
			}
		}
		if (answer == -1) {
			cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
		}
		else {
			cout << "Case #" << i + 1 << ": " << answer << endl;
		}
	end:;
	}
	_getch();
}