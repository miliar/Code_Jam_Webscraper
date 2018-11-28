#include <stdio.h>
#include <cstring>

using namespace std;

#define LETTERS 101

void solve();
bool isCons(char c);

int main(){
	int cases;
	scanf("%d", &cases);

	for(int i=0; i<cases; i++){
		printf("Case #%d: ", i+1);
		solve();
	}

	return 0;
}

void solve(){
	char buf[LETTERS];
	bool vis[LETTERS];
	int len, cap;

	scanf("%s %d", buf, &cap);
	len = strlen(buf);

	for(int i=0; i<=len-cap; i++){
		vis[i] = true;
		for(int j=0; j<cap; j++){
			if(!isCons(buf[i+j])){
				vis[i] = false;
				break;
			}
		}
	}

	int count = 0;

	for(int i=0; i<=len-cap; i++){
		for(int j=i+cap-1; j<len; j++){
			//printf("testing (%d, %d)\n", i, j);

			if(vis[i]){
				count++;
				continue;
			}
			for(int k=i; k<=(j-cap+1); k++){
				if(vis[k]){
					//printf("found (%d, %d)\n", i, j);
					count++;
					break;
				}
			}
		}
	}
	printf("%d\n", count);
}

bool isCons(char c){
	char alfa[] = {'a', 'e', 'i', 'o', 'u'};
	for(int i=0; i<strlen(alfa); i++){
		if(alfa[i]==c)
			return false;
	}
	return true;
}
