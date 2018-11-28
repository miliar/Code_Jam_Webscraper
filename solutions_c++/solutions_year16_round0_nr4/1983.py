#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <vector>

using namespace std;

#define LL long long

int main(int argc,char **argv)
{
	int T;
	scanf("%d\n",&T);
	for (int t=1;t<=T;t++){
		int K,C,S;
		scanf("%d %d %d\n",&K,&C,&S);
#if 1
		// large�_���B����ʒu��L�������Ƃ��A���ꂪ�܂܂��O���[�v�͌��{�̕����B
		// �Ȃ̂ł��̐e�ɂ����镔����L�ɂȂ�A������܂����{�̕����B������ċA�I�ɌJ��Ԃ��̂ŁA�K�؂ɐ��l��I�ׂ΍ő�C�ӏ���L����x�Ɋm�肳�����邱�Ƃ��킩��B
		// S���̃^�C���̓��e���킩��̂ŁAC*S>=K���m�肳����������A�t��C*S<K�̂Ƃ��͂킩��Ȃ��B
		printf("Case #%d:",t);
		if (C*S<K){
			printf(" Impossible");
		}
		else{
			// C�{���Ċm�F�������ʒu�̔ԍ������Z����̂��J��Ԃ����Ƃɂ��A�������܂Ƃ߂ă`�F�b�N�ł���C���f�b�N�X����������
			// �؂����ɉ���Ă����̂ɑ���
			int target = 0;
			LL ans_idx[S];
			int ai_num=0;
			for (int i=0;i<S;i++){ans_idx[i]=-1;}
			while (1){
				LL idx=0;
				for (int i=0;i<C;i++){
					//printf("idx %lld * %d => %lld\n",idx,K,idx*K);
					idx*=K;
					if (target<K){
						//printf("idx %lld + %d => %lld\n",idx,target,idx+target);
						idx+=target;
						target++;
					}
				}
				ans_idx[ai_num]=idx;
				//printf("ans[%d]=%lld\n",ai_num,idx);
				ai_num++;
				if (target==K)break;
			}
			for (int i=0;i<ai_num;i++){
				assert(ans_idx[i]>=0);
				for (int j=0;j<ai_num;j++){
					assert(ans_idx[j]>=0);
					if (i==j)continue;
					assert(ans_idx[i]!=ans_idx[j]);
				}
			}
			for (int i=0;i<ai_num;i++){
				if (ans_idx[i]<0)continue;
				printf(" %lld",ans_idx[i]+1);
			}
		}
		printf("\n");
#else
		// small�_���BS=K�Ȃ̂ō��[K���͍��[��G�Ȃ�G��K��J��Ԃ��A�����łȂ���΃I���W�i���̃R�s�[
		// �Ȃ̂ł��̒���G���Ȃ���΃I���W�i���͑S��L=G�͑��݂��Ȃ�
		// ���������āA�����l������[1,S]���o�͂���΂悢
		printf("Case #%d:",t);
		for (int i=1;i<=S;i++){
			printf(" %d",i);
		}
		printf("\n");
#endif
	}
	return 0;
}
