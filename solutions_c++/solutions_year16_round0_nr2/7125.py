#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

char s[105];
int main(){
	int N;
	scanf("%d", &N);
	for(int icase = 1; icase <= N; icase++){
		scanf("%s", s);
		int len = strlen(s);
		int num = 0;
		for(int i = 0; i < len - 1; i++){
			if(s[i] != s[i + 1])
				num++;
		}
		if(s[len - 1] == '-'){
			num++;
		}
		printf("Case #%d: %d\n", icase, num);
	}
	return 0;
}
