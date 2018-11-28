#include <iostream>

using namespace std;

int arr1[4][4];
int arr2[4][4];

int main(){
	int t;
	cin >> t;
	for(int i = 1 ; i <= t ; i++){
		int ans1,ans2;
		cin >> ans1;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				cin >> arr1[i][j];

		cin >> ans2;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				cin >> arr2[i][j];

		int count = 0,ans;

		for(int i = 0 ; i < 4 ; i++){
			for(int j = 0 ; j < 4 ; j++){
				if(arr1[ans1-1][i] == arr2[ans2-1][j]){
					count++;
					ans = arr2[ans2-1][j];
				}
			}
		}

		cout << "Case #" << i << ": ";
		if(count <= 0)
			cout << "Volunteer cheated!" << endl;
		else if(count == 1)
			cout << ans << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}