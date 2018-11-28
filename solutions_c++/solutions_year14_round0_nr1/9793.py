#include <iostream>

using namespace std;

int main(){
	int t = 0;
	cin >> t;
	for(int i = 0; i < t; i++){
		
		int atrow = 0;
		int frow[2][4] = {{0}};
		int tmp = 0;

		for(int turn = 0; turn < 2; turn++)
		{
			cin >> atrow;
			
			// eat useless lines before useful data
			int eatBefore = (atrow-1)*4;
			for(int j = 0; j < eatBefore; j++){
				cin >> tmp;
			}

			// save useful row into array
			for(int j = 0; j < 4; j++){
				cin >> frow[turn][j];
			}

			// east useless lines after useful data
			int eatAfter = 16 - eatBefore - 4;
			for(int j = 0; j < eatAfter ; j++){
				cin >> tmp;
			}

		}

		// start to compare collected two rows
		int sameCount = 0;
		int theSame = 0;
		bool toBreak = false;

		for(int pf = 0; pf < 4; pf++){
			for(int ps = 0; ps < 4; ps++){
				if(frow[0][pf] == frow[1][ps]){
					sameCount++;
					theSame = frow[0][pf];
				}
//				cout << frow[0][pf] << " " << frow[1][ps] << endl;
				if(sameCount > 1){
					toBreak = true;
					break;
				}
			}
			if(toBreak){
				break;
			}
		}
		
		switch(sameCount){
			case 0:
				cout << "Case #" << i+1 << ": Volunteer cheated!";
				break;
			case 1:
				cout << "Case #" << i+1 << ": " << theSame;
				break;
			default:
				cout << "Case #" << i+1 << ": Bad magician!";
		}

		cout << endl;

	}
}