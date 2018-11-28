#include <cstdio>
#include <cstring>

void sol(){
	char str[105];
	int ret = 0, c = -1, l;
	scanf("%s", str);
	l = strlen(str);
	for(int i = 0;i < l and c == -1;i++)
		if(str[i] != '-') c = i;
	c == 0? ret = 0: ret = 1;
	if(c == -1) c = l;
	for(int i = 0;i < c;i++) str[i] = '+';
	while(1) {
		c = -1;
		for(int i = 0;i < l and c == -1;i++)
			if(str[i] == '-') c = i;
		if(c == -1) break;
		for(int i = c;str[i] == '-' and i < l;i++)
			str[i] = '+';
		ret += 2;
	}
	printf("%d\n", ret);	
}

int main() {
	int ks;
	scanf("%d", &ks);
	for(int i = 1;i <= ks;i++)
		printf("Case #%d: ", i), sol();
}
