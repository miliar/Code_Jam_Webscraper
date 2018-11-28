#include<iostream>
#include<fstream>
#include<string>
using namespace std;

#define STOP {cin.sync();cin.get();}
#define LOOP(n) for(int abc=0; abc<(int)(n);abc++)

ifstream fin("A-large.in");
ofstream fout("output.txt");

void solve(int num){
	int i = 0;
	int ini, las;
	char TEMP;
	char S_temp[1001];
	char ans[1001 * 2 + 1];

	fin >> S_temp;
	
	ans[1001] = S_temp[i++];
	ini = las = 1001;

	LOOP(strlen(S_temp)){
		TEMP = S_temp[i++];

		if ((TEMP - ans[ini]) >= 0){
			ans[--ini] = TEMP;
		}
		else{
			ans[++las] = TEMP;
		}
	}

	//cout << "Case #" << num << ": " << (ans + ini) << endl;
	fout << "Case #" << num << ": " << (ans + ini) << endl;
}

int main(){
	int T;

	//cin >> T;
	fin >> T;

	for (int num = 1; num <= T; num++){
		solve(num);
	}

	//STOP

	return 0;
}