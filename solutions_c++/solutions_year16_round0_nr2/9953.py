#include <cstdio>
#include <cstring>

int main(){
	char str[105];
	int numTC, TC = 1, len, ans;
	bool isUp;
	scanf("%d", &numTC);
	while(numTC--){
		scanf("%s", str); len = strlen(str); ans = 0; isUp = str[0]=='+';
		for(int i=1; i<len; i++){
			if(str[i]!=str[i-1]){
				ans++; isUp = !isUp;
			}
		}
		printf("Case #%d: %d\n", TC++, isUp? ans: ans+1);
	}
	return 0;
}