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
		if (N==0){ // 0�̏ꍇ�͉i���ɏI���Ȃ�
			printf("Case #%d: INSOMNIA\n",t);
		}
		else{
			// 1�ȏ�ł���΁A�J�E���g���Ă��邤���ɏ�ʂ̌���1������Ă����̂ł����1�`9�͒B�������B
			// �J�E���g���ׂ��ŏ��񐔂�100��(�ŏ�ʂ�1�̏ꍇ�A���̏オ�������̂�100�񂩂���)
			// 0��10����ΕK���o�Ă���
			// �l�͈̔͂�10^6 * 100 = 10^8 < 2^31
			int appear[10];
			int a_cnt = 0;
			int step = N;
			memset(appear,0,sizeof(appear));
			int i;
			for (i=0;i<200;i++){
				// �o�����鐔���`�F�b�N
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
