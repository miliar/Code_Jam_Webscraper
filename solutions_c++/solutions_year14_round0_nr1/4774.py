#include <iostream>

using namespace std;

int main(){
	int T;

	cin >> T;

	int first, second;

	for(int k = 1; k <= T; k++){
		int firstArr[5][5];
		int secondArr[5][5];
		int answer = 0;
		bool badMag = false;

		cin >> first;

		for(int i = 1; i <= 4; i++){
			for(int j = 1; j <= 4; j++){
				cin >> firstArr[i][j];
			}
		}

		cin >> second;

		for(int i = 1; i <= 4; i++){
			for(int j = 1; j <= 4; j++){
				cin >> secondArr[i][j];
			}
		}

		for(int i = 1; i <= 4; i++){
			int tmpFirst = firstArr[first][i];

			for(int j = 1; j <= 4; j++){
				int tmpSecond = secondArr[second][j];

				if(tmpFirst == tmpSecond){
					if(answer == 0){
						answer = tmpFirst;
					}else{
						badMag = true;
						break;
					}
				}
			}
		}

		if(badMag){
			cout << "Case #" << k <<": Bad magician!" << endl;
		}else{
			if(answer == 0){
				cout << "Case #" << k <<": Volunteer cheated!" << endl;
			}else{
				cout << "Case #" << k <<": " << answer << endl;
			}
		}

	}

	return 0;
}