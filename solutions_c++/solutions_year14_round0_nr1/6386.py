#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int testCount = 0;
	cin >> testCount;
	int testCase = 1;
	int answer, result, resultCount, row1[4], row2[4];
	char buffer[100];
	while (testCase <= testCount){
		resultCount = 0;
		cin >> answer;
		cin.getline(buffer, 100);
		for (int i = 1; i <= 4; ++i){
			cin.getline(buffer, 100);
			if (i == answer){
				sscanf_s(buffer, "%d %d %d %d", &row1[0], &row1[1], &row1[2], &row1[3]);
			}
		}
		cin >> answer;
		cin.getline(buffer, 100);
		for (int i = 1; i <= 4; ++i){
			cin.getline(buffer, 100);
			if (i == answer){
				sscanf_s(buffer, "%d %d %d %d", &row2[0], &row2[1], &row2[2], &row2[3]);
			}
		}

		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				if (row1[i] == row2[j]){
					result = row1[i];
					++resultCount;
				}
			}
		}
		switch (resultCount)
		{
		case 0:
			cout << "Case #" << testCase << ": Volunteer cheated!" << endl;
			break;
		case 1:
			cout << "Case #" << testCase << ": " << result << endl;
			break;
		default:
			cout << "Case #" << testCase << ": Bad magician!" << endl;
			break;
		}
		++testCase;
	}
	return 1;	
}