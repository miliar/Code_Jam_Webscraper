#include <cstdio>
#include <cstring>

using namespace std;

char in[1005], out[1005];

void LastWord(int len){
	for(int i=1; i<len; ++i){
	if( in[i] >= out[0] ){
		char tmp[1005];
		sprintf(tmp, "%s", out);
		sprintf(out, "%c%s", in[i], tmp);
	}
	else					sprintf(out, "%s%c", out, in[i]);
	}
}

int main(void){
	freopen("A-large.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int cas, cc=0;
	
	scanf("%d", &cas);
	while( cas-- ){
		scanf("%s", in);
		memset(out, 0, sizeof(out));
		out[0] = in[0];
		LastWord(strlen(in));
		printf("Case #%d: %s\n", ++cc, out);
	}
	
	return 0;
}

