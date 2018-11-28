#include <iostream>
using namespace std;
int M[5][5];
int vec[20];

void doWork(){
	int row;
	cin >> row;
	row--;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			cin >> M[i][j];
	for(int i = 0; i < 4; ++i)
		vec[M[row][i]]++;
}
int main(){
	int t,tc;
	cin >> tc;
	for(t = 1; t <=tc; ++t){
		for(int i = 0; i < 20; ++i) vec[i] = 0;
		doWork();
		doWork();
		int cont = 0, res;
		for(int i = 1; i <= 16; ++i)
			if(vec[i] == 2){
				cont++;
				res = i;
			}
		cout << "Case #" << t << ": ";
		if(cont == 0)
			cout << "Volunteer cheated!" << endl;
		if(cont == 1)
			cout << res << endl;
		if(cont > 1)
			cout << "Bad magician!" << endl;
	}
}