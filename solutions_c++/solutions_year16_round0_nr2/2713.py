#include <cstdio>
#include <cstring>

int T;
char in[105];

int main(){
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++){
		scanf("%s", in);

		int ct = 0;
		int len = strlen(in);
		for(int i = 1; i < len; i++){
			if(in[i] != in[i - 1])
				ct++;
		}
		if(in[len - 1] == '-')ct++;

		printf("Case #%d: %d\n", tt, ct);
	}
}