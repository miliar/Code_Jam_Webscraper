#include <cstdio>
#include <cstring>
#include <string.h>
using namespace std;


int main(){
	int T;
	scanf("%d", &T);
	char s[110]; gets(s);
	for (int t=1; t<=T; t++){
		gets(s);
		int len = strlen(s);
		char c = s[0];
		int ans = 0;
		for (int i=1; i<len; i++){
			if (s[i] == c){
				continue;
			}else{
				if (c == '-'){
					ans++;
				}else{
					ans+=1;
				}
				c = s[i];
			}
		}
		if (c == '-'){
			ans++;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
