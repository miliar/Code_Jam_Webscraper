#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

const int mulM[5][5] = {{0, 0, 0, 0, 0},
			{0, 1, 2, 3, 4},
			{0, 2, -1, 4, -3},
			{0, 3, -4, -1, 2},
			{0, 4, 3, -2, -1}};

int multiply(int a, int b){
	int sign = 1;
	if(a < 0) {sign *= -1; a *= -1;}
	if(b < 0) {sign *= -1; b *= -1;}
	return sign * mulM[a][b];
}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int T; scanf("%d", &T);
	for(int t = 1 ; t <= T ; t ++){
		long long L, X; scanf("%lld %lld", &L, &X);
		string s; cin >> s;
		
		int intRep[10000];
		for(int i = 0 ; i < s.length() ; i ++){
			if(s[i] == 'i') intRep[i] = 2;
			else if(s[i] == 'j') intRep[i] = 3;
			else intRep[i] = 4;
		}

		int tot = 1; int period;
		for(int i = 0 ; i < L ; i ++) tot = multiply(tot, intRep[i]);
		if(tot == 1) period = 1;
		else if(tot == -1) period = 2;
		else period = 4;

		long long truncate = (X-100)/period;
		if(X >= 100) X -= truncate*period;

		bool I = false;
		bool J = false;
		bool K = false;
		int cum = 1;

		for(int i = 0 ; i < L*X ; i ++){
			cum = multiply(cum, intRep[i%L]);
			if(i == L*X-1 && I && J && cum == -1) K = true;
			if(I && cum == 4) J = true;
			if(cum == 2) I = true;
		} 
		if(K) printf("Case #%d: YES\n", t);
		else printf("Case #%d: NO\n", t);
	}
	return 0;
}
