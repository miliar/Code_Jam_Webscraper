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
	for (int C = 1; C <= T; C++){
		int L;
		scanf("%d", &L);

		int sum = 0;
		int add = 0;

		for (int i = 0; i <= L; i++){
			int number;
			scanf("%1d", &number);
			if (i <= sum) {
				sum += number;
			}
			else {
				add += i - sum;
				sum = i;
				sum += number;
			}
		}

		printf("Case #%d: %d\n", C, add);


	}
	return 0;
}

/* printf("Case #%d:",C); */