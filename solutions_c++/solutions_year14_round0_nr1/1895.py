#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>
#include<utility>
#include<memory.h>
#include<cstring>
#include<fstream>

using namespace std;

const long long MOD = 1e9 + 7;

int m1[5][5], m2[5][5], flag[22];

int main(){
	//freopen("A-small-attempt1.in","r",stdin);
	ifstream fin("in.txt");
	freopen("A-small-out.txt", "w", stdout);
	int T;
	fin >> T;
	for (int q = 1; q <= T; q++){
		int a, b;
		fin >> a;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				fin >> m1[i][j];
			}
		}
		fin >> b;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				fin >> m2[i][j];
			}
		}
		memset(flag, 0, sizeof(flag));
		for (int i = 0; i < 4; i++) flag[m1[a - 1][i]]++, flag[m2[b - 1][i]]++;
		int id = 0;
		for (int i = 1; i < 17; i++){
			if (flag[i]>1){
				if (id>0) id = -1;
				else if (0 == id) id = i;
			}
		}
		cout << "Case #" << q << ": ";
		if (-1 == id) cout << "Bad magician!\n";
		else if (0 == id) cout << "Volunteer cheated!\n";
		else cout << id << endl;
	}
}