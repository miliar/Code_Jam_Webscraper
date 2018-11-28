#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
	int tc;
	cin >> tc;
	for(int tcase=1; tcase<=tc ; tcase++){
		int a1, a2;
		cin >> a1;
		int arr1[4][4];
		for(int i=0 ; i<4; i++){
			for(int j=0 ; j<4 ; j++){
				cin >> arr1[i][j];
			}
		}
		
		cin >> a2;
		int arr2[4][4];
		for(int i=0 ; i<4; i++){
			for(int j=0 ; j<4 ; j++){
				cin >> arr2[i][j];
			}
		}
		
		int ans = 0;
		int num = -1;
		for(int i=0; i<4 ; i++){
			for(int j=0; j<4 ; j++){
				if(arr1[a1-1][i] == arr2[a2-1][j]){
					ans++;
					num = arr1[a1-1][i];
				}
			}
		}
		if(ans == 1){
			cout << "Case #" << tcase << ": " << num << endl;
		}else if(ans > 1){
			cout << "Case #" << tcase << ": Bad magician!" << endl;
		}else{
			cout << "Case #" << tcase << ": Volunteer cheated!" << endl;
		}
	}
	return 0;
}
