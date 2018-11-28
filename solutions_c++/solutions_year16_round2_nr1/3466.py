#include <cstdio>
#include <cstring>

using namespace std;

char in[2005], w[10][10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"}, ans[2005];
int cnt[26];

char backtrace(int index, int num, int len){
	if( num==len ){
		ans[index] = 0;
		puts(ans);
		return 1;
	}
	int i, j;
	for(i=0; i<10; i++){
		for(j=0; w[i][j]; j++)
		if( !cnt[w[i][j]-'A'] )	break;
		if( w[i][j] )	continue;
		
		ans[index] = '0'+i;
		for(j=0; w[i][j]; j++)
			cnt[w[i][j]-'A']--;
		if( backtrace(index+1, num+strlen(w[i]), len) )	return 1;
		for(j=0; w[i][j]; j++)
			cnt[w[i][j]-'A']++;
	}
	return 0;
}

int main(void){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int cas, cc=0;
	
	scanf("%d", &cas);
	while( cas-- ){
		scanf("%s", in);
		memset(cnt, 0, sizeof(cnt));
		for(int i=0,j=strlen(in); i<j; i++)	cnt[in[i]-'A']++;
		printf("Case #%d: ", ++cc);
		backtrace(0,0,strlen(in));
	}
	
	return 0;
}

