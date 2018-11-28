#include <cstdio>
#include <iostream>
#include <vector>


using namespace std;

int n;


vector<string> vc(4);
int ii = 1;

bool win(char item) {
	int a , b;
	bool exist = false;
	for(int i=0;i<vc.size();i++) {
		for(int j=0;j<vc.size();j++)
			if(vc[i][j] == 'T'){
				vc[i][j] = item;
				a = i; b = j;
				exist = true;
			}
	}
	for(int i=0;i<vc.size();i++) {
		if(vc[i][0] == item and vc[i][1] == item and vc[i][2] == item and vc[i][3] == item) {
			if(exist)vc[a][b] = 'T';
			 return true;
		}
		if(vc[0][i] == item and vc[1][i] == item and vc[2][i] == item and vc[3][i] == item) {
			if(exist)vc[a][b] = 'T'; return true;
		}
	}

	if(vc[0][3] == item and vc[1][2] == item and vc[2][1] == item and vc[3][0] == item) {
			if(exist)vc[a][b] = 'T'; return true;
	}

	if(vc[0][0] == item and vc[1][1] == item and vc[2][2] == item and vc[3][3] == item) {
			if(exist)vc[a][b] = 'T'; 
			return true;
	}
	if(exist)vc[a][b] = 'T';
	return false;
}

void simulate () {
	if(win('O') and win('X')) {
		printf("Case #%d: Draw\n", ii++);
		return;
	}
	if(!win('O') and !win('X')) {
		for(int i=0;i<vc.size();i++)for(int j=0;j<vc.size();j++)
			if(vc[i][j] == '.') {
				printf("Case #%d: Game has not completed\n", ii++);
				return;
			}
			printf("Case #%d: Draw\n", ii++);
		return;
	}
	if (win('X'))
	{
		printf("Case #%d: X won\n", ii++);
		return;
	}
	if (win('O'))
	{
		printf("Case #%d: O won\n", ii++);
		return;
	}
	
	printf("Case #%d: Game has not completed\n", ii++);
}

void resolve() {
	vc.clear();
	// vc.resize(4);
	for(int i=0; i<4 ;i++) {
		string a; cin >> a;
		vc.push_back(a);
		// cout << vc[i] << endl;
	}

	simulate();
}

int main() {
	int nc;
	cin >> nc;
	for(int i=0; i<nc ;i++) {
		resolve();
	}
}