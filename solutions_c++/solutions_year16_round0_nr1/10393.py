#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");

int N;
int input;
bool used[11];

void sheep(int m, bool used[], int cnt, int sh){
	bool flag = true;
	for (int i = 0; i < 10; i++){
		if (used[i] == false){
			flag = false;
		}
	}

	if (m * (sh+1) == m){
		cout << "Case #" << cnt + 1 << ": " << "INSOMNIA" << endl;
		fout << "Case #" << cnt + 1 << ": " << "INSOMNIA" << endl;

		return;
	}

	if (flag){
		//ÀßÀÚ~
		cout << "Case #" << cnt + 1 << ": " << m*(sh-1) << endl;
		fout << "Case #" << cnt + 1 << ": " << m*(sh-1) << endl;

		return;
	}

	//used[m*sh % 10] = true;


	char temp[100];
	_itoa_s(m*sh, temp, 10);
	
	for (int j = 0; j < strlen(temp); j++){
		used[temp[j] - '0'] = true;
	}

	sheep(m, used, cnt, sh + 1);

}

void main()
{
	
	fin >> N;
	for (int i = 0; i < N; i++){
		memset(used, false, sizeof(used));
		fin >> input;
		
		sheep(input, used, i, 1);
	}

}