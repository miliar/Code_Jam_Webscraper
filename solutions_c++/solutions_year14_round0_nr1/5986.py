#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	for (int n=0; n < N; n++) {
		int row1,row2,c1[4][4],c2[4][4];
		
		cin >> row1;
		for(int i=0;i<4;i++) {
			cin >> c1[i][0] >> c1[i][1] >> c1[i][2] >> c1[i][3];
		}	
		cin >> row2;
		for(int i=0;i<4;i++) {
			cin >> c2[i][0] >> c2[i][1] >> c2[i][2] >> c2[i][3];
		}
		int count = 0;
		int number = -1;
		for(int i=0;i<4;i++) {
			int s = c1[row1-1][i];
			for(int j=0;j<4;j++) {
				//cout << "i:" << i << " j:" << j << " " << s << " " <<  c2[row2][j]  << endl;

				if (c2[row2-1][j]==s) {
					count++;
				//	cout << "count" << count;
					number = s;
					break;
				} 
			}		
		}
		if (count==0) {
			cout << "Case #" << n + 1 << ": Volunteer cheated!" << endl;
		} else if (count==1) {
			cout << "Case #" << n + 1 << ": " << number << endl;
			
		} else {
			cout << "Case #" << n + 1 << ": Bad magician!" << endl;
		}
	}	
}