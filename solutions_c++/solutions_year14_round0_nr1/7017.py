#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int k=1;k<=T;++k){
		int row1;
		cin >> row1;
		--row1;
		int grid1[4][4];
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				cin >> grid1[i][j];
			}
		}
		int row2;
		cin >> row2;
		--row2;
		int grid2[4][4];
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				cin >> grid2[i][j];
			}
		}
		sort(grid1[row1], grid1[row1]+4);
		sort(grid2[row2], grid2[row2]+4);
		//for(int i=0;i<4;++i){
		//	cout << grid1[row1][i] << " " << grid2[row2][i] << endl;
		//}
		int ind1=0, ind2=0;
		int value=-1;
		int count=0;
		while(ind1!=4 && ind2 !=4){
			if(grid1[row1][ind1]==grid2[row2][ind2]){
				++count;
				value = grid1[row1][ind1];
				//cout << "Value : " << value << endl;
				++ind1;
				++ind2;
			} else if (grid1[row1][ind1]>grid2[row2][ind2]){
				++ind2;
			} else {
				++ind1;
			}
		}
		if(count==0){
			cout << "Case #" << k << ": Volunteer cheated!" << endl;
		} else if (count >=2){
			cout << "Case #" << k << ": Bad magician!" << endl;
		} else {
			cout << "Case #" << k << ": " << value << endl;
		}
	}
}
