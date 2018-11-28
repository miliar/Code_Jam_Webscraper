#include <iostream>
#include <string>
using namespace std;

int T, t;

int sMax, stood, op;
string s;

int main(){

	freopen("ip.in", "r", stdin);
	freopen("op.txt", "w", stdout);

	cin >> T;	t = T;

	for(int t=1 ; t<=T ; t++){

		cin >> sMax;
		cin >> s;
		stood = 0;

		op = 0;
		for (int i = 0; i <= sMax; i++){
			if (i > stood && s[i] > 48){
				op += i - stood;
				stood += i - stood;
			}
			stood += s[i] - 48;
		}

		printf("Case #%d: %d\n", t, op);
	}


	return 0;
}