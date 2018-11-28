#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
int main() {
	ifstream myfile("A-small-attempt0.in");
	ofstream outfile;
	outfile.open ("result.txt");
	string data;
	int T, row1, row2, count = 1;
	int A[4][4], B[4][4];
	getline(myfile, data);
	stringstream(data)>>T;
	do {
		getline(myfile, data);
		stringstream(data)>>row1;
		for(int i=0; i<4;i++) {
			getline(myfile, data);
			istringstream stream(data);
			stream >> A[i][0] >> A[i][1] >> A[i][2] >> A[i][3];
		}
		getline(myfile, data);
		stringstream(data)>>row2;
		for(int i=0; i<4;i++) {
			getline(myfile, data);
			istringstream stream(data);
			stream >> B[i][0] >> B[i][1] >> B[i][2] >> B[i][3];
		}
		int found=0, result;
		for(int i=0; i<4; i++) {
			for(int j=0;j<4;j++) {
				if(A[row1-1][i] == B[row2-1][j]) {
					found++;
					result = A[row1-1][i];
					if(found >1)
						break;
				}
			}
		}
		if(found == 1) {
			outfile<<"Case #"<<count<<": "<<result<<"\n";
		}
		else if(found > 1) {
			outfile<<"Case #"<<count<<": Bad magician!\n";
		}
		else {
			outfile<<"Case #"<<count<<": Volunteer cheated!\n";
		}
		
		count++;
		T--;
	} while(T!=0);
	outfile.close();
	return 0;
}
