# include <iostream>
#include <string>

using namespace std;

int main(){

	int num_cases;
	cin >> num_cases;
	int choice1, choice2, trash;
	int board1[4];
	int board2[4];
	for(int i = 1; i <= num_cases; i++){
		cin >> choice1;
		int count = 0;
		for(int j = 0; j < 16; j++){
			if(j / 4 + 1 == choice1){
				cin >> board1[count++];
			} else {
				cin >> trash;
			}
		}
		count = 0;
		cin >> choice2;
		for(int j = 0; j < 16; j++){
			if(j / 4 + 1 == choice2){
				cin >> board2[count++];
			} else {
				cin >> trash;
			}
		}
		count = 0;
		int ans;
		int check_map[16] = {0};
		for(int k = 0; k < 4; k++){
			check_map[board1[k]-1] = 1;
		}
		for(int k = 0; k < 4; k++){
			if(check_map[board2[k]-1] == 1){
				count++;
				ans = board2[k];
			}		
		}
		if(count == 0){
			cout << "Case #" << i << ": Volunteer cheated!\n";
		} else if(count == 1){
			cout << "Case #" << i << ": " << ans << endl;
		} else {
			cout << "Case #" << i << ": Bad magician!\n";
		}
	}
	return 0;
}