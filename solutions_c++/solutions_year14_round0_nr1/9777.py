#include <iostream>

using namespace std;

int shuffle1[4][4];
int shuffle2[4][4];
int test[8];

int main(){
	size_t testcase;
	int first_ans, second_ans,found, ans=0,t;

	cin >> testcase;

	for(t=0; t<testcase; t++){
		found = 0;
		cin >> first_ans;

		for(int x=0; x<4; x++){
			for(int y=0; y<4; y++){
				cin >> shuffle1[x][y];
			}
		}
		cin >> second_ans;

		for(int x=0; x<4; x++){
			for(int y=0; y<4; y++){
				cin >> shuffle2[x][y];
			}
		}

		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(shuffle1[first_ans-1][j] == shuffle2[second_ans-1][i]){
					found++;
					ans = shuffle1[first_ans-1][j];
				}
			}
		}
		if(found == 1){
			cout << "Case #" << (t+1) <<": " << ans << endl;
		}
		else if(found > 1){
			cout << "Case #" << (t+1) <<": Bad magician!" << endl;
		}
		else if(found == 0){
			cout << "Case #" << (t+1) <<": Volunteer cheated!" << endl;
		}

	}

	return 1;
}
