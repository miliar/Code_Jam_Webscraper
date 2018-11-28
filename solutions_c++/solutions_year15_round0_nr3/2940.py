#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int product(int a, int b){
	//absx = |x|
	int ans, absa = abs(a), absb = abs(b);
	if((absa == 1)||(absb == 1)) return a*b;
	
	if(absa == absb) ans = -1;
	else
		if(absa == 2){
			if(absb == 3) ans = 4;  
			else if(absb == 4) ans = -3;
		}
		else
			if(absa == 3){
				if(absb == 2) ans = -4;
				if(absb == 4) ans = 2;
			}
			else
				if(absa == 4){
					if(absb == 2) ans = 3;
					if(absb == 3) ans = -2;
				}
	if(a < 0) ans *= -1;
	if(b < 0) ans *= -1;
	return ans;
}

int quart(char c){
	if(c == 'i') return 2;
	if(c == 'j') return 3;
	if(c == 'k') return 4;
}

 // 1 = 1
 // i = 2
 // j = 3
 // k = 0
//stages = 1, 2, 3 for ijk1
int main(){

	int t, l, x, current, index, stage;
	string input;

	cin >> t;
	for(int tt = 1; tt <= t; tt++){
		cin >> l >> x;
		cin >> input;
		index = 0, current = 1, stage = 0;
		for(int index = 0; index < l * x; index++){
			if(stage == 0){
				current = product(current, quart(input[index%l]));
				if(current == 2){ 
					stage++;
					current = 1;
				}
			}
			else if(stage == 1){
				current = product(current, quart(input[index%l]));
				if(current == 3){
					stage++;
					current = 1;
				}
			}
			else if(stage == 2){
				current = product(current, quart(input[index%l]));
				if(current == 4){
					stage++;
					current = 1;
				}
			}
			else if(stage == 3){
				current = product(current, quart(input[index%l]));
			}

		}
		if((stage == 3)and(current == 1)){
			cout << "Case #" << tt << ": " << "YES" << endl;
		}
		else cout << "Case #" << tt << ": " << "NO" << endl;
	}

	return 0;
}