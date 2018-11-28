#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

void deleteCommon(string &str, int *&mas, int n, int&z){
	mas = new int [n];
	for (int i = 0; i < str.size(); i++){
		mas[i] = 0;
	}

	int k = 0;
	for (int i = 0; i < str.size(); i++){
		if (str[i] == str[i + 1]){
			str.erase(i, 1);
			i--;
			mas[k]++;
		} else {
			k++;
		}
	}
	z = k;
}

int main(){
	ifstream fin;
	ofstream fout;
	int T;

	fin.open("input.txt");
	fout.open("output.txt");
	fin >> T;
	
	for (int k = 1; k <= T; k++){
		int N;
		fin >> N;
		string *mas = new string[N];
		for (int i = 0; i < N; i++){
			fin >> mas[i];
		}
		bool isOk = true;
		int n = 0;
		for (int i = 0; i < N; i++){
			n = max(n,(int) mas[i].size());
		}
		
		
		int **temp = new int *[N];
		int z;

		for (int i = 0; i < N; i++){
			deleteCommon(mas[i], temp[i], n, z);
		}
		
		for (int i = 0; i < N - 1; i++){
			if (mas[i] != mas[i + 1]){
				isOk = false;
				break;
			}
		}

		int s = 0;
		if (isOk){
			for (int i = 0; i < z; i++){
				int *data = new int[N];
				for (int j = 0; j < N; j++){
					data[j] = temp[j][i];
				}

				sort(&data[0], &data[N]);
				double c = 0;
				for (int i = 0; i < N; i++){
					c += (double)data[i];
				}

				c /= (double)N;
				double q = INT_MAX;
				int k = 0;

				for (int i = 0; i < N; i++){
					if (abs(c - data[i]) < q){
						q = abs(c - data[i]);
						k = i;
					}
				}

				for (int i = 0; i < N; i++){
					s += abs(data[i] - data[k]);
				}
			}
		}

		fout << "Case #" << k << ": ";

		if (isOk){
			fout << s << endl;
		} else {
			fout << "Fegla Won" << endl;
		}
	}
	fin.close();
	fout.close();
}