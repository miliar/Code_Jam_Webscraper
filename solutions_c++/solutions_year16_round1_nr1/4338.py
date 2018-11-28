#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define MV_R 0
#define MV_L 1

int main(void)
{
	int T;
	scanf("%d\n",&T);
	for (int t=1;t<=T;t++){
		char S[1001];
		char op[1001];
		scanf("%s\n",S);
		int s_len = strlen(S);
		int s_range = s_len; // ’Tõ”ÍˆÍ
		for (int i=0;i<s_len;i++){
			op[i]=-1;
		}
		while (1){
			if (s_range<=0)break;
			// ’Tõ”ÍˆÍ“à‚Ìmax‚ð’T‚·
			char S_max=S[0];int idx_max=0;
			for (int i=1;i<s_range;i++){
				if (S[i]>=S_max){
					S_max = S[i];
					idx_max = i;
				}
			}
			op[idx_max] = MV_L;
			for (int i=idx_max+1;i<s_range;i++){
				op[i] = MV_R;
			}
			s_range = idx_max;
		}
		char r_mem[1001*2];
		char *ret;
		ret=&r_mem[1000];
		memset(r_mem,0,sizeof(r_mem));
		for (int i=0;i<s_len;i++){
			if (op[i]==MV_L){
				ret--;
				ret[0]=S[i];
			}
			else if (op[i]==MV_R){
				ret[i]=S[i];
			}
			else assert(0);
		}
		printf("Case #%d: %s\n",t,ret);
	}
	return 0;
}
