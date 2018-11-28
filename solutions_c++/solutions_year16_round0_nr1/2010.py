#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int main(int argc,char **argv)
{
	int T;
	scanf("%d\n",&T);
	for (int t=1;t<=T;t++){
		int N;
		scanf("%d\n",&N);
		if (N==0){ // 0の場合は永遠に終わらない
			printf("Case #%d: INSOMNIA\n",t);
		}
		else{
			// 1以上であれば、カウントしているうちに上位の桁が1ずつ回っていくのでそれで1～9は達成される。
			// カウントすべき最小回数は100回(最上位が1の場合、その上が一周するのに100回かかる)
			// 0は10回回れば必ず出てくる
			// 値の範囲は10^6 * 100 = 10^8 < 2^31
			int appear[10];
			int a_cnt = 0;
			int step = N;
			memset(appear,0,sizeof(appear));
			int i;
			for (i=0;i<200;i++){
				// 出現する数をチェック
				char str[100];
				sprintf(str,"%d",N);
				char *p = str;
				//printf("%s\n",str);
				while (*p){
					int c = *p - '0';
					if (appear[c]==0){
						a_cnt++;
					}
					appear[c]=1;
					p++;
				}
				if (a_cnt == 10)break;
				N += step;
			}
			assert(i!=200);
			printf("Case #%d: %d\n",t,N);
		}
	}
	return 0;
}
