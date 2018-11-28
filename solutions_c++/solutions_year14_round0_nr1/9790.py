#include<iostream>
using namespace std;
int arr[4][4];
int arr1[4][4];
int main(){
	int n;
	cin >> n;
	int t=n;
	while(n--){
		int r1;
		int r2;
		int mc=0;
		int m=0;
		cin >> r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> arr[i][j];
		cin >> r2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> arr1[i][j];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(arr[r1-1][i]==arr1[r2-1][j]){
					mc++;
					m = i;
				}
		if(mc==0)
			cout <<"Case #" << t-n <<": Volunteer cheated!" << endl;
		if(mc > 1)
			cout <<"Case #" << t-n << ": Bad magician!" << endl;
		if(mc == 1)
			cout <<"Case #" << t-n << ": " << arr[r1-1][m] << endl;
	}
}