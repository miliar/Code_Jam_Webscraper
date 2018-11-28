#include <cstdio>
#include <string.h>
#include <list>
using namespace std;

char dir[10][10];
int d[26];
int ans[700];
int endx;
bool found;
bool check(){
	for (int i=0; i<26; i++){
		if (d[i] != 0){
			return false;
		}
	}
	return true;
}

void run(int x, int a){
	if (a == 10){
		return;
	}

	if (check()){
		endx = x;
		found = true;
		return;
	}

	int l = strlen(dir[a]);
	bool ok = true;
	for (int i=0; i<l; i++){
		int c = (int)(dir[a][i]) -  65;
		if (d[c] == 0){
			ok = false;
		}
	}
	if (!ok){
		return run(x, a+1);
	}
	for (int i=0; i<l; i++){
		int c = (int)(dir[a][i]) -  65;
		d[c]--;
	}

	ans[x] = a;
	run(x+1, a);
	if (found) return;
	for (int i=0; i<l; i++){
		int c = (int)(dir[a][i]) -  65;
		d[c]++;
	}
	run(x, a+1);
}

int main(){
	memset(dir,0,sizeof(dir));
	strcpy(dir[0], "ZERO");
	strcpy(dir[1], "ONE");
	strcpy(dir[2], "TWO");
	strcpy(dir[3], "THREE");
	strcpy(dir[4], "FOUR");
	strcpy(dir[5], "FIVE");
	strcpy(dir[6], "SIX");
	strcpy(dir[7], "SEVEN");
	strcpy(dir[8], "EIGHT");
	strcpy(dir[9], "NINE");

	int T;
	scanf("%d",&T);
	int ca = 0;
	char s[2010]; gets(s);
	while (T--){
		gets(s);
		
		memset(ans,0,sizeof(ans));
		memset(d,0,sizeof(d));
		int len = strlen(s);
		for (int i=0; i<len; i++){
			int c = (int)(s[i]) -  65;
			d[c]++;
		}

		found = false;
		run(0, 0);

		printf("Case #%d: ", ++ca);
		for (int i=0; i<endx; i++){
			printf("%d", ans[i]);
		}

		printf("\n");
	}
	return 0;
}
