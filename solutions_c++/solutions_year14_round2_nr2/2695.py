#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int test_cases, i, j, k,m, A, B, K, temp,count;
	ifstream fin("int.in");
	ofstream fout("Small_Output.txt");
	fin >> test_cases;
	for (i = 0; i < test_cases; i++){
		fin >> A;
		fin >> B;
		fin >> K;
		count = 0;
		for (j = 0; j < A; j++){
			for (k = 0; k < B; k++){
				temp = j&k;
				for (m = 0; m < K; m++){
					if (m == temp){
						count++;
						break;
					}
				}
			}
		}

		fout << "Case #" << i + 1 << ": " << count << endl;
	}
	system("pause");
	return 0;
}