#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;
const int maxn = 5;
int cards1[maxn][maxn];
int cards2[maxn][maxn];

int main(){
	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-practice.txt");

	int cases;
	in >> cases;
	for (int k = 1; k <= cases; k++){
		int ans1, ans2;
		in >> ans1;
		for (int i = 1; i < maxn; i++){
			for (int j = 1; j < maxn; j++){
				in >> cards1[i][j];
			}
		}
		in >> ans2;
		for (int i = 1; i < maxn; i++){
			for (int j = 1; j < maxn; j++){
				in >> cards2[i][j];
			}
		}
		int num = 0;
		int ans;

		for (int i = 1; i < maxn; i++){
			for (int j = 1; j < maxn; j++){
				if (cards1[ans1][i] == cards2[ans2][j]){
					num++;
					ans = cards1[ans1][i];
				}
			}
		}

		if (num == 0){
			out << "Case #" << k << ": Volunteer cheated!" << endl;
		}
		else if (num == 1){
			out << "Case #" << k << ": " << ans<< endl;
		}
		else{
			out << "Case #" << k << ": Bad magician!" << endl;
		}
	}

	return 0;
}