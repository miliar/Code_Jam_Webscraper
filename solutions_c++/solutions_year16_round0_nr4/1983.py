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
		// large狙い。ある位置がLだったとき、それが含まれるグループは原本の複製。
		// なのでその親にあたる部分もLになり、これもまた原本の複製。これを再帰的に繰り返すので、適切に数値を選べば最大C箇所のLを一度に確定させられることがわかる。
		// S枚のタイルの内容がわかるので、C*S>=Kが確定させられる条件、逆にC*S<Kのときはわからない。
		printf("Case #%d:",t);
		if (C*S<K){
			printf(" Impossible");
		}
		else{
			// C倍して確認したい位置の番号を加算するのを繰り返すことにより、それらをまとめてチェックできるインデックスを見つけられる
			// 木を下に下りていくのに相当
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
		// small狙い。S=Kなので左端K枚は左端がGならGのK回繰り返し、そうでなければオリジナルのコピー
		// なのでその中にGがなければオリジナルは全部L=Gは存在しない
		// したがって、何も考えずに[1,S]を出力すればよい
		printf("Case #%d:",t);
		for (int i=1;i<=S;i++){
			printf(" %d",i);
		}
		printf("\n");
#endif
	}
	return 0;
}
