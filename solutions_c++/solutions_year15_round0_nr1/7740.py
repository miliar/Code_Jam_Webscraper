#include <fstream>
#include <cstdlib>
#include <string>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	int T;
	fin.open("A-large.in");
	fout.open("output.txt");
	fin >> T;
	for (int i = 1; i <= T; i++){
		int Smax;
		fin >> Smax;
		//int *shyness = new int[Smax + 1];
		long long standing=0;
		long long friends = 0;
		string shynessString;
		fin >> shynessString;
		int shynessPersons;
		for (int j = 0; j <= Smax; j++){
			shynessPersons=shynessString[j]-48;
			if (standing < j){
				friends += (j - standing);
				standing = j;
			}
			standing += shynessPersons;
		}


		fout << "Case #" << i << ": " << friends << endl;
	}


	fin.close();
	fout.close();

	return 0;
}