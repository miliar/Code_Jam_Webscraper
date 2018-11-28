#include <iostream>
#include <string>
#include <vector>
#include <fstream>


using namespace std;

int main(int argc, char **argv)
{
	ifstream in(argv[1]);
	int nCase;
	in >> nCase;
	for (int i = 0; i < nCase; i++){
		int row ;
		in >>row;
		int a[4];
		int tmp;
		for (int w = 0;w < 4; w++){
			for (int ww = 0; ww < 4; ww++){
				if (w+1 == row){
					in >> a[ww];
				}
				else {
					in >> tmp;
				}
			}
		}
		int row2 ;
		in >> row2;
		int b[4];
		for (int w = 0;w < 4; w++){
			for (int ww = 0; ww < 4; ww++){
				if (w+1 == row2){
					in >> b[ww];
				}
				else {
					in >> tmp;
				}
			}
		}
		vector<int> same;
		for (int w = 0; w < 4; w++){
			for (int ww = 0; ww < 4; ww++){
				if (a[w] == b[ww]){
					same.push_back(a[w]);
				}
			}
		}
		if (same.size() >= 2){
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
		if (same.size() == 1){
			cout<<"Case #"<<i<<": "<<same[0]<<endl;
		}
		if (same.size() == 0){
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
