#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

void print(bool b, int count){
	if (b)
		cout << "Case #" << count << ": " << "GABRIEL" << endl;
	else
		cout << "Case #" << count << ": " << "RICHARD" << endl;
}
int main(){

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	

	int T, X, R, C;
	cin >> T ;
	int count = 0;
	while (T--){
		cin >> X >> R >> C;
		count++;

		if (X == 1){
			print(true, count);
			continue;
		}
		if (X == 2){ // 1posibility
			if (R*C % X == 0){
				print(true, count);
			}else{
				print(false, count);
			}
			continue;
		}
		if (X == 3){//straight or corner
			if (R == 1 || C == 1 || R*C % X != 0)
				print(false, count);
			else
				print(true, count);
		}
		if (X == 4){
			if (R <= 2 || C <= 2 || R*C%X != 0)
				print(false, count);
			else
				print(true, count);
		}
	}

	return 0;
}