#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
using namespace std;

int main(){
	ifstream ii("B-large.in");
	ofstream oo("o.out");
	int T;
	ii >> T;
	char S[100][101];
	int length[100];

	for (int i = 0;i < T;i++){
		ii >> S[i];
		length[i] = strlen(S[i]);

	}
	bool data[100][100];

	for (int i = 0;i < T;i++){
		for (int j = 0;j < length[i];j++){
			if (S[i][j] == '+')
				data[i][j] = 1;
			else data[i][j] = 0;
		}
	}
	for (int i = 0; i < T;i++){
		bool flag = true;
		for (int j = 0;j<101;j++){
			flag = flag & data[i][j];
		}
		if (flag == true)
			oo << "Case #" << i+1 << ": "  << 0 << endl;
		else {
			int num = 0;
			int index = 0;
			while(index != length[i]){
				bool record = data[i][index];
				int j;
				for (j = index+1;j < length[i];j++){
					if (data[i][j] != record)
						break;
				}
				index = j;
				if (record&& index != length[i])
					num += 1;
				else if (!record)
					num += 1;
			}
			oo << "Case #" << i+1 << ": "  << num<< endl;
		}
	}
}