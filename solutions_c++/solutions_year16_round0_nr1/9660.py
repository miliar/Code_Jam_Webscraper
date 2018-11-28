#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("A-small-attempt5 (1).in");
ofstream fout("output.txt");

void solve(int num){
	int N, N_temp;
	int judge = 0;
	int i;

	//cin >> N;
	fin >> N;

	if (N == 0){
		//cout << "Case #" << num << ": INSOMNIA" << endl;
		fout << "Case #" << num << ": INSOMNIA" << endl;
		return;
	}

	for (i = 1;; i++){
		N_temp = i*N;

		while (N_temp != 0){
			judge |= int(pow(2, (N_temp % 10)));
			N_temp /= 10;
		}

		if (judge == 1023) break;
	}


	//cout << "Case #" << num << ": " << i*N << endl;
	fout << "Case #" << num << ": " << i*N << endl;

}

int main(){
	int T;
	//cin >> T;
	fin >> T;

	for (int num = 0; num < T; num++){
		solve(num + 1);
	}

	return 0;
}