#include <stdio.h>
#include <string.h>

int t;
int cnt[30];
char s[2020];
int dig[10];

int get_dig(char d, const char *name){
	int res = cnt[d-'A'];
	for(int i=0;name[i];++i){
		cnt[name[i]-'A'] -= res;
	}
	return res;
}

int main(){
	scanf("%d\n",&t);
	for(int tt=1;tt<=t;++tt){
		printf("Case #%d: ",tt);
		memset(cnt,0,sizeof(cnt));
		memset(dig,0,sizeof(dig));
		scanf("%s\n", s);
		for(int i=0;s[i];++i){
			cnt[s[i]-'A']++;
		}
		dig[0] = get_dig('Z', "ZERO");
		dig[4] = get_dig('U', "FOUR");
		dig[6] = get_dig('X', "SIX");
		dig[8] = get_dig('G', "EIGHT");
		dig[7] = get_dig('S', "SEVEN");
		dig[5] = get_dig('V', "FIVE");
		dig[3] = get_dig('R', "THREE");
		dig[2] = get_dig('W', "TWO");
		dig[1] = get_dig('O', "ONE");
		dig[9] = get_dig('I', "NINE");
		for(int i=0;i<10;++i){
			for(int j=0;j<dig[i];++j){
				printf("%c", i+'0');
			}
		}
		puts("");
	}
	return 0;
}
