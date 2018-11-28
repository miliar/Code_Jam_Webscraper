#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;

vector<int> getCommon(vector<int> &v1, vector<int> &v2){
	vector<int> v3;

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),back_inserter(v3));

    return v3;
} 


int main(){
	ifstream input_file;
	ofstream output_file;
	input_file.open("A-small-attempt0.in");
	output_file.open("C-small-1-magic.out");
	int t = 0;
//	cin >> t;
	input_file >> t;
	int k = 1;
	while(t){
		int r1 = 0;
		int r2= 0;
		vector<int> v1;
		vector<int> v2;
		int A[4][4];
		int B[4][4];
//		cin >> r1;
		input_file >> r1;
		for( int i = 0 ; i < 4; i++){
			for(int j = 0; j < 4; j++){
		//		cin >> A[i][j];
				input_file >> A[i][j];
			}
		}
		int real_r1 = r1-1;
		for (int j = 0; j < 4; j++){
			v1.push_back( A[real_r1][j] );
		}
	//	cin >> r2;
		input_file >> r2;
		for( int i = 0 ; i < 4; i++){
			for(int j = 0; j < 4; j++){
			//	cin >> B[i][j];
				input_file >> B[i][j];
			}
		}
		int real_r2 = r2-1;
		for (int j = 0; j < 4; j++){
			v2.push_back( B[real_r2][j] );
		}
		
		auto v3 = getCommon(v1,v2);
		if( v3.size() > 1 ) output_file << "Case #" << k << ": " << "Bad magician!" << "\n";
		else if(v3.size() == 1) output_file << "Case #" << k << ": " << v3[0] << "\n";
		else output_file << "Case #" << k << ": " << "Volunteer cheated!" << "\n";
		k = k + 1;
		t = t - 1;
	}
	return 0;
}
