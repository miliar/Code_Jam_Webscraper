#include<bits/stdc++.h>
using namespace std;

int TCs, TC;
char inputS[1010];
int K, L;
int i, x, y, c, ans;

int Check(){
	for (i=0; i<L; i++) if (inputS[i]=='-') return 0;
	return 1;
}

int main(){
	c = '+' ^ '-';
	
	scanf("%d", &TCs);
	for (TC=1; TC<=TCs; TC++){
		printf("Case #%d: ", TC);
		scanf("%s%d", inputS, &K);
		L = strlen(inputS);
		
		ans = 0;
		for (i=0; i<=L-K; i++) if (inputS[i]=='-'){
			for (x=0; x<K; x++) inputS[i+x] ^= c;
			ans++;
		}
		
		if (!Check()) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	
	return 0;
}


