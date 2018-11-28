#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <set>
#include <string>
#include <map>
//#include <functional>

using namespace std;

int conv[5][5] = {	{0, 0, 0, 0,  0},
					{0, 1, 2, 3,  4},
					{0, 2, -1,4, -3},
					{0, 3, -4,-1, 2},
					{0, 4, 3, -2,-1}};
int main(){
	int T; scanf("%d", &T);
	for(int t=1;t<=T;t++){
		int L, X; scanf("%d %d", &L, &X);
		char z[10000]; scanf(" %s", z);
		string m = z;
		string s = "";
		while(X--) s += m;

		map<char, int> ctoi;
		ctoi['1'] = 1;
		ctoi['i'] = 2;
		ctoi['j'] = 3;
		ctoi['k'] = 4;

		int act = 1;
		int sign = 0;
		int let = 2;
		int hotovo = false;
		for(int i=0;i<s.length();i++){
			act = conv[act][ctoi[s[i]]];
			if(act < 0){
				sign = 1-sign;
				act *= -1;
			} 
			if(let == act && sign == 0){
				act = 1;
				let++;
				if(let == 5){
					//check done
					///////////////////k s jednickou na konci
					for(int j=i+1;j<s.length();j++){
						act = conv[act][ctoi[s[j]]];
						if(act < 0){
							sign = 1-sign;
							act *= -1;
						} 
					}
					if(sign == 0 && act == 1){
						hotovo = true;
						break;
					}
				}
			}
		}
		printf("Case #%d: %s\n", t, hotovo?"YES":"NO");


	}
}