#include <iostream>

using namespace std;

int main(){
	int t=0;
	int ans;
	int arr1[4][4];
	int arr2[4][4];
	int* row1,*row2;
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> t;
	for(int cn=1;cn<=t;cn++){
		cout << "Case #" << cn << ": ";
		cin >> ans;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin >> arr1[i][j];
			}
		}
		row1 = arr1[ans-1];
		cin >> ans;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin >> arr2[i][j];
			}
		}
		row2 = arr2[ans-1];
		int common = 0;
		for(int i=0;i<4;i++){
			int key = row1[i];
			for(int j=0;j<4;j++){
				if(key == row2[j]){
					common++;
					ans = j;
					break;
				}
			}
		}
		if(common == 1) {
			cout << row2[ans]; 
		}
		if(common == 0){
			cout << "Volunteer cheated!";
		}
		if(common >1){
			cout << "Bad magician!";
		}
		cout << endl;
	}
	return 0;
}