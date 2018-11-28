#include <cstdio>
#include <string.h>
#include <list>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	int ca=0;
	char s[1010]; gets(s);
	while (T--){
		gets(s);
		int len = strlen(s);
		list<char> ans; ans.clear();
		int c = 0;
		ans.push_back(s[0]);
		for (int i=1; i<len; i++){
			if (s[i] >= ans.front()){
				ans.push_front(s[i]);
			}else{
				ans.push_back(s[i]);
			}
		}
		printf("Case #%d: ", ++ca);
		for (int i=0; i<len; i++){
			char c = ans.front();
			ans.pop_front();
			printf("%c", c);
		}
		printf("\n");
	}
	return 0;
}
