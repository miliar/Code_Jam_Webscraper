#include <iostream>
using namespace std;
char S[101];
int main(){
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int TC, tc;
	cin >> TC;
	for (tc = 1; tc <= TC; tc++){
		cin >> S;
		int num = 0;
		int cur = S[0] == '+' ? 0 : 1;
		for (int i = 1; S[i]; i++){
			if (S[i] != S[i - 1]){
				num++; cur = !cur;
			}
		}
		if (cur) num++;
		cout << "Case #" << tc << ": " << num << endl;
	}
	return 0;
}