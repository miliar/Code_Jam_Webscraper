#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

#define REP(i,n) for (int i=0;i<(n);i++)

/*�O���[�o���ϐ���0�ŏ����������*/
/*�e�X�g�P�[�X�ϐ�*/
int T;

int main() {
	scanf("%d", &T);
	/*�J��Ԃ����̕ϐ��������Y��ɋC��t����*/
	for (int Case = 1; Case<= T; Case++){
		int X, R,C;
		scanf("%d", &X);
		scanf("%d", &R);
		scanf("%d", &C);

		if (X >= 7) { printf("Case #%d: RICHARD\n", Case); }//�͂�
		else if (X >= (min(R, C) + 1) * 2 - 1) {
			printf("Case #%d: RICHARD\n", Case);//�k��
		}
		else if (X > max(R, C)) {
			printf("Case #%d: RICHARD\n", Case);//�c�_
		}
		else if ((R*C) % X != 0) {
			printf("Case #%d: RICHARD\n", Case);
		}
		//�ŏ�����min(R,C)�𒴂��Ă�����C��t����B
		//L���͒[�����Ɋ񂹂邾��
		else if(min(R,C) == 2 && X>=4){//3�͒����`����
			printf("Case #%d: RICHARD\n", Case);
		}
		//2�̏ꍇ�͗]�����̈�̋��m�肷��̂ł킩��₷�������B
		//�T�~�m�ō���ŏ��̒����`��15�i�ő���{���j
		//�U�~�m�̎���t�`�̎��ɗ�����mod3������Ȃ�
		else if (min(R, C) == 3 && X==5 && R*C % 15 == 0){ //X=4�Ȃ�ŏ�����2
			printf("Case #%d: RICHARD\n", Case);
		}
		else if (min(R, C) == 3 && X == 6){
			printf("Case #%d: RICHARD\n", Case);
		}
		else {
			printf("Case #%d: GABRIEL\n", Case);
		}
	}
	return 0;
}

/* printf("Case #%d:",C); */