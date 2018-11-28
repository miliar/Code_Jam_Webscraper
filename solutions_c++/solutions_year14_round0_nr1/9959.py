#include <iostream>
using namespace std;

int main()
{
	int T;
	int answer1,answer2;
	int arrange1[16],arrange2[16];

	cin>>T;
	
	for (int i = 0; i < T; i++) {
		cin>>answer1;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++) {
				cin>>arrange1[4*j+k];
			}
		}
		cin>>answer2;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++) {
				cin>>arrange2[4*j+k];
			}
		}
		
		int count = 0;
		int value = 0;
		for (int k = 0; k < 4; k++) {
			for (int j = 0; j < 4;j++) {
				if (arrange1[4*(answer1-1)+k] == arrange2[4*(answer2-1)+j]) {
					count++;
					value = arrange1[4*(answer1-1)+k];
				}
			}
		}
		cout << "case #"<<i+1<<": ";

		if (count == 1) {
			cout << value << endl;
		} else if (count > 1) {
			cout << "Bad magician!" << endl;
		} else if (count == 0) {
			cout << "Volunteer cheated!" << endl;
		}
	}

}