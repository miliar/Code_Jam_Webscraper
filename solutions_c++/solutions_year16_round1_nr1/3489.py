#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int main(){

	int T;
	scanf("%d",&T);

	for(int t = 1 ; t <= T; t++){
		char s[1002];
		scanf("%s",s);

		int len = strlen(s);

		int c;
		string ans;
		for(int i = 0 ; i < len ; i++){
			if(i == 0){
				ans = s[i];
				c = s[i];
			}
			else if(c <= s[i]){
				ans = s[i]+ans;
				c = s[i];
			}
			else{
				ans = ans + s[i];
			}
		}

		printf("Case #%d: %s\n",t,ans.c_str());
	}

	return 0;
}
