#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<assert.h>

// N:�c��_�C�������h�� l:���ɃX���C�h�ł��鐔�@r:�E�ɃX���C�h���Ȃ��ƂȂ�Ȃ���
double F(int N, int l, int r){
	if(!r)return 1;
	if(!N)return 0;
	if(l==0)return F(N-1, l, r-1);
	else return (F(N-1,l-1,r) + F(N-1,l,r-1))/2;
}

double Solve(int N, int x, int y){
	// �O�p��������Εs�\�@����ΕK���\
	if(x==0){
		return (N >= (((y+2)*(y+1)/2)));
	}
	// �m��Ŗ��܂�s���~�b�h���̍���(�V��������y���W)
	int h=1;
	while( (h*(h+1))/2 <= N){
		h+=2;
	}
	h-=2;
	int z = abs(x)+abs(y);
	if(z < h)return 1;
	int rest = N-(h*(h+1))/2;
	// �c��rest������̂ŁA���ꂪx,y�ɂ��Ԃ��邩����
	return F(rest, (h+1), (h+1)-x+1);

#if 0
	// ���_��@��_�����c�[
	const int DP_SIZE = 1024;
	static double dp[DP_SIZE][DP_SIZE] = {};	//[���܂ŉ��܂ꂽ][���ɐς܂�Ă����]�ɂȂ�m��
	for(int i=0; i<DP_SIZE; ++i)
		for(int j=0; j<DP_SIZE; ++j)
			dp[i][j] = 0;
	dp[0][0] = 1;
	dp[1][0] = dp[1][1] = 0.5;
	for(int i=1; i<=rest; ++i){
		for(int j=0; j<i; ++j){
			//���ɂ����l�߂Ȃ�
			if(j>=h){
				dp[i][j] = dp[i-1][j];
			}
			// �����E�ɋl�߂Ȃ�
			else if((i-j)>=h){
				dp[i][j] = dp[i-1][j-1];
			}
			// �ǂ���ɂ��X���C�h����\������
			else{
				if(j==0) dp[i][0] = dp[i-1][0]/2;
				else dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])/2;
			}
		}
	}
	return dp[rest][y];
#endif
}

int main() {
	int T, caseNum;
	scanf("%d",&T);
	for(caseNum=1; caseNum<=T; ++caseNum) {
		int N, x, y;
		scanf("%d%d%d",&N,&x,&y);
		assert(N<=20);

		printf("Case #%d: %.9f\n", caseNum, Solve(N, abs(x), y));
	}
	return 0;
}
