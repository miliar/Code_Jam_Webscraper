#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int t, ans, conut;
bool pos[20];

int main(){
	scanf("%d", &t);
	int i, j;
	for(int k = 1; k <= t; ++k){
		memset(pos, false, sizeof pos);
		scanf("%d", &i);
		int inp;
		for(int a = 1; a <= 4; ++a){
			for(int b = 0; b < 4; ++b){
				scanf("%d", &inp);
				if(a == i) pos[inp] = true;
			}
		}
		scanf("%d", &j);
		conut = 0;
		for(int a = 1; a <= 4; ++a){
			for(int b = 0; b < 4; ++b){
				scanf("%d", &inp);
				if(a == j){
					if(pos[inp] == true) ans = inp, ++conut;
				}
			}
		}
		if(conut == 1) printf("Case #%d: %d\n", k, ans);
		else if(conut == 0) printf("Case #%d: Volunteer cheated!\n", k);
		else printf("Case #%d: Bad magician!\n", k);
	}
	return 0;
}
