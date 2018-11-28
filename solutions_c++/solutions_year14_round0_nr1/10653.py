#include <iostream>
using namespace std;

int main() {
	freopen("input.in","r",stdin);
	freopen("output.in","w",stdout);
	int arr[6][6];
	int arr1[6][6];
	int testCases;
	int answer1,answer2;
	int counter;
	cin >> testCases;
	for(int k = 1;k <= testCases;k++) {
		cin >> answer1;
		for(int i = 0;i < 4;i++) {
			for(int j = 0;j < 4;j++) {
				cin >> arr[i][j];
			}
		}
		cin >> answer2;
		int commonNum = 0;
		for(int i = 0;i < 4;i++) {
			for(int j = 0;j < 4;j++) {
				cin >> arr1[i][j];
			}
		}
		counter = 0;
		for(int i = 0;i < 4;i++) {
			for(int j = 0;j < 4;j++) {
				if(arr[answer1-1][i] == arr1[answer2-1][j]) {
					commonNum = arr[answer1-1][i];
					++counter;
				}
			}
		}
		if(counter == 0)
			cout << "Case #" << k << ": Volunteer cheated!" <<endl;
		else if(counter == 1)
			cout << "Case #" << k << ": " << commonNum <<endl;
		else if(counter > 1)
			cout << "Case #" << k << ": Bad magician!" <<endl;
	}
	return 0;
}
