#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <stack>

using namespace std;

int K, C , S;
string a[105];

int num = 0;
string member[1000];
string arr[1000];
string KG;
int K_C;
void parse() {
 	cin >> K >> C >> S;
 	KG = "";
 	for (int i = 0; i < K; i++)
 		KG = KG + "G";
 	K_C = 1;
 	for (int i = 0; i < C; i++)
 		K_C *= K;
}

void make_member(int i) {
	if (i == K){
		num ++;
		member[num] = "";
		for (int j = 0; j < K; j++)
			member[num] = member[num] + a[j];
		return;
	}

	for (int j = 0; j <= 1; j++){
		if (j == 0 )
			a[i] = "G";
		else a[i] = "L";

		make_member(i+1);
	}
}


void solve(){
	for (int i = 1; i <= num; i++)
		arr[i] = member[i];

	for (int cc = 2; cc <= C; cc++){

		for (int i = 1; i <= num; i++){
			string s = "";
			for (int j = 0; j < arr[i].length(); j++)
				if (arr[i][j] == 'G')
					s = s + KG;
				else s = s + member[i];
			arr[i] = s;
		}

		for (int i = 1; i <= num; i++)
			cout << arr[i] << endl;
	}
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++){
		parse();
		make_member(0);
		solve();
	}
	return 0;
}



