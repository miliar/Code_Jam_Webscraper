#include<cstdio>
#include<cstring>
bool us[10];
void ww(int x){
	while (x){
		us[x % 10] = true;
		x = x / 10;
	}
}
bool usall(){
	for (int i = 0; i < 10;i++)
	if (!us[i])
		return false;
	return true;
}
int main(){
	int T, n;
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	int ic = 0;
	while (T--){
		scanf("%d", &n);
		if (n <= 0){
			printf("Case #%d: INSOMNIA\n", ++ic);
			continue;
		}
		memset(us, false, sizeof(us));
		for (int i = n;; i += n){ 
			ww(i);
			if (usall()){
				printf("Case #%d: %d\n", ++ic, i);
				break;
			}
		}
	}
	return 0;
}