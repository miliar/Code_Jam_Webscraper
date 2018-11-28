#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <vector>

using namespace std;

int brother(int *board, int B, int W, int idx)
{
	// ��̎v�l: �\�����ő剻����
	// i�Ԗڂ�hit�Ƃ���Ƃ�
	int n_hit=0, n_miss=0;
	board[idx]=1;
	int i;
	for (i=0;i<B-W+1;i++){
		// consistent���ǂ����m���߂�
		int j;
		int flag=1;
		for (j=i;j<i+W;j++){
			if (board[j]!=0 && board[j]!=1)flag=0;
		}
		if (flag)n_hit = 1;
	}
	board[idx]=2;
	for (i=0;i<B-W+1;i++){
		// consistent���ǂ����m���߂�
		int j;
		int flag=1;
		for (j=i;j<i+W;j++){
			if (board[j]!=0 && board[j]!=1)flag=0;
		}
		if (flag)n_miss = 1;
	}
	board[idx]=0;
	assert(n_hit>0 || n_miss>0);
	if (n_hit>n_miss)return 1;
	return 2;
}

int search(int *board, int B, int W, int dmg)
{
	int i;
	int min_ret=-1;
	if (dmg==W)return 0;
	// i�Ԗڂ��������ɍs��
	for (i=0;i<B;i++){
		if (board[i]!=0)continue;
		board[i]=brother(board,B,W,i);
		int ret = search(board,B,W, dmg + ((board[i]==1)?1:0) );
		if (min_ret<0 || ret<min_ret)min_ret = ret;
		board[i]=0;
	}
	return min_ret + 1;
}

int main(void)
{
	int T;
	scanf("%d\n",&T);
	int t;
	for (t=1;t<=T;t++){
		int R,C,W;
		int ans=0;
		scanf("%d %d %d\n",&R,&C,&W);
		// ��ɑ��݂����Ȃ����邽�߂ɕK�v�Ȏ��=�󂫗̈悪W����
		// W-1�Ԋu�Ŕ�΂��Ă����΂���
		int h_per_row = C/W;
		int patterns = C%W + 1;
		//fprintf(stderr,"pattern = %d\n",patterns);
		ans = h_per_row * (R-1);
		ans += h_per_row - 1;
		//if (C%W!=0){
			// �����ŒT��
			int B=W+C%W;
			int board[B];
			int dmg=0;
			// 0...�킩��Ȃ� 1...hit�m�� 2...miss�m��
			int i;
			for (i=0;i<B;i++){
				board[i]=0;
				if (i<W && B-W<=i){
					board[i]=1;
					ans++;
					dmg++;
					//fprintf(stderr,"board[%d]=1\n",i);
				}
			}
			//fprintf(stderr,"dmg=%d,W=%d\n",dmg,W);
			ans+=search(board,B,W,dmg);
		//}
		//else ans += W;
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
