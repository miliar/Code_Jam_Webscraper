#include <cstdio>
#include <cstring>

using namespace std;

int T,jaw,n;
bool udah,state;
char st[110];

int main(){
	scanf("%d",&T);
	gets(st);
	for (int t = 1; t <= T; t++){
		gets(st);
		n = strlen(st);
		if (st[0] == '+') udah = true; else udah = false;
		jaw = 0;
		for (int i= 1; i < n; i++){
			if (st[i] != st[i - 1]){
				if (st[i] == '-'){
					udah = true;
				} else {
					if (udah) jaw += 2; else jaw++;
					udah = true;
				}
			}
		}
		if (st[n-1] == '-'){
			if (udah) jaw += 2; else jaw++;
		}
		printf("Case #%d: %d\n",t,jaw);
	}
}