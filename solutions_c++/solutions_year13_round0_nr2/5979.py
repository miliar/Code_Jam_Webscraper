#include<iostream>
#include<iomanip>
#include<string>
#include<fstream>

using namespace std;

int main(){

	ifstream in_file;
	in_file.open("smallB.txt");

	string num;

	in_file >> num;

	char* dum = &num[0];
	int numTest = atoi(dum);

	int m, n;

	for(int i = 0; i < numTest; i++){

		in_file >> num;
		dum = &num[0];
		int m = atoi(dum);
		in_file >> num;
		dum = &num[0];
		int n = atoi(dum);

		int lawn[m][n];
		int mark[m][n];

		for(int j = 0; j < m; j++){

			for(int k = 0; k < n; k++){

				in_file >> num;
				dum = &num[0];
				lawn[j][k] = atoi(dum);
				mark[j][k] = 0;
			}
		}

		int count1 = 0;
		int count2 = 0;

		bool fail = 0;

		for(int j = 0; j < m; j++){

			for(int k = 0; k < n; k++){

				if(lawn[j][k] == 1){

					for(int w = 0; w < n; w++){

						if(lawn[j][w] == 1){

							count1++;
						}
					}

					for(int w = 0; w < m; w++){

						if(lawn[w][k] == 1){

							count2++;
						}
					}

					if(count1 < n && count2 < m){

						cout << "Case #" << (i + 1) << ": NO" << endl;
						fail = 1;
						break;
					}

					count1 = 0;
					count2 = 0;
				}

				if(fail)
					break;
			}

			if(fail)
				break;
		}

		if(!fail)
			cout << "Case #" << (i + 1) << ": YES" << endl;
	} 

	return 0;
}
