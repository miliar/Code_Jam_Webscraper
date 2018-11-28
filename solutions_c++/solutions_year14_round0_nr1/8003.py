#include <iostream>
#include <vector>
using namespace std;

int main() {

	int n;
	
	cin >> n;
	
	for(int i = 0; i < n; ++i){
		int r1, r2;
		
		cin >> r1;
		r1--;
		vector< vector<int> > vec1(4);
		for(int j = 0; j < 4; ++j){
			vector<int> tmpVec(4);
			cin >> tmpVec[0] >> tmpVec[1] >> tmpVec[2] >> tmpVec[3];
			vec1[j] = tmpVec;
		}
		
		cin >> r2;
		r2--;
		vector< vector<int> > vec2(4);
		for(int j = 0; j < 4; ++j){
			vector<int> tmpVec(4);
			cin >> tmpVec[0] >> tmpVec[1] >> tmpVec[2] >> tmpVec[3];
			vec2[j] = tmpVec; 
		}
		
		int count = 0;
		int num = 0;
		for(int j = 0; j < 4; ++j){
			for(int k = 0; k < 4; ++k){
				//cout << endl;
				//cout << "vec1[" << r1 << "][j] = " << vec1[r1][j];
				//cout << "vec2[" << r2 << "][k] = " << vec2[r2][k];
				//cout << endl;
				
				if(vec1[r1][j] == vec2[r2][k]) {
					++count;
					num = vec1[r1][j];
				}
			}
		}
		
		cout << "Case #" << i+1 << ": ";
		if(count == 0)
			cout << "Volunteer cheated!" << endl;
		else if(count == 1)
			cout << num << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}