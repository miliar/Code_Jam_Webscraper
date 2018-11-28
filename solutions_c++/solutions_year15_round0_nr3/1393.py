#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

#define REP(i,n) for (int i=0;i<(n);i++)
#define REP1(i,n) for (int i=1;i<=(n);i++)

#define MAX_L 10001

/*�O���[�o���ϐ���0�ŏ����������*/
/*�e�X�g�P�[�X�ϐ�*/
int T;

int dp[MAX_L][MAX_L];

/*�v�Z�p�z��쐬*/
int q[4][4] = { { 1, 2, 3, 4 },{ 2, -1, 4, -3 }, { 3, -4, -1, 2 }, { 4, 3, -2, -1 } };

int calc(int a,int b) {
//-1 * -1��0�ɂȂ��Ă��܂��Ă��� 1��-1�Ɋւ���ς̐����͕ۂ����B
	if (abs(a) == 1 || abs(b) == 1){
		return a * b;
	}
	else if (a * b > 0){
		return q[abs(a) - 1][abs(b) - 1];
	}
	else if (a * b < 0){
		return -q[abs(a) - 1][abs(b) - 1];
	}

}

int main() {
	
	
	scanf("%d", &T);
	/*�J��Ԃ����̕ϐ��������Y��ɋC��t����*/
	for (int C = 1; C<= T; C++){
		int L, X,rest;
		scanf("%d", &L);
		scanf("%d%*c", &X);

		rest = X % 4;

		int s[MAX_L];
		
		REP(i, L){
			char tmp;
			scanf("%c", &tmp);
			if (tmp == 'i') s[i] = 2; 
			if (tmp == 'j') s[i] = 3;
			if (tmp == 'k') s[i] = 4;
		}

		//��������dp�e�[�u�����߁B
		for (int i = 0; i < L; i++){
			dp[i][i] = s[i];
		}

		for (int i = 0; i < L-1; i++){
			for (int j = i+1; j < L; j++){
				dp[i][j] = calc(dp[i][j - 1], s[j]);
				/*printf("dp[%d][%d] %d \n",i,j,dp[i][j]);*/
			}
		}
		int cycle[4];

		cycle[0] = 1;
		cycle[1] = dp[0][L-1];

		for (int i = 2; i<= 3; i++){
			cycle[i] = calc(cycle[i - 1], cycle[1]);
			/*printf("cycle[%d] %d\n", i, cycle[i]);*/
		}

		bool yn[12]; // 1����11���g��
			REP(i, 12) { yn[i] = false; }

	    /*�[�����c�o��`
			dp[0][-1]
				dp[L][L-1]*/

		if (cycle[1] == 1) { //i�Ȃ̂Œ[�����ŋ�؂��Ă��Ӗ��Ȃ�
			//1�g�����ꍇ ���̂��߂�dp�e�[�u���K�v
			for (int i = 1; i < L - 1; i++){//2�Ԗڂ̐擪
				if (dp[0][i - 1] != 2) continue;
				for (int j = i + 1; j < L; j++){//�R�Ԗڂ̐擪
					if (dp[i][j - 1] != 3) continue;
					if (dp[j][L - 1] != 4) continue;
					REP(a, 4){
						REP(b, 4){
							if (1 + a + b > X) continue;
								yn[1 + a + b] = true;
								continue;
						}
					}
				}
			}

			//�Q�g�����ꍇ
			//������(L-1)*(L-1)��S�Ċm���ߐ��������ꍇ��mod4�����߂�rest�Ƃ̈�v���m���߂�B
			for (int i = 0; i < L - 1; i++){//�O���̋�؂�̎�O
				if (dp[0][i] != 2) continue;
				for (int j = 0; j < L - 1; j++){//�㔼�̋�؂�̎�O
					if (calc(dp[i + 1][L - 1], dp[0][j]) != 3) continue;
					if (dp[j + 1][L - 1] != 4) continue;
					REP(a, 4){
						REP(b, 4){
							REP(c, 4){
								if (2 + a + b + c > X) continue;
									yn[2 + a + b + c] = true;
									continue;
							}
						}
					}
				}
			}
			bool flag = true;

			if (X >= 12) { X = 11; }
			for (int r = rest; r <= X; r += 4){
				if (r > 0){
					if (yn[r]) {
						printf("Case #%d: YES\n", C);
						flag = false;
						break;
					}
				}
			}

			if (flag) printf("Case #%d: NO\n", C);
		}
		else if (cycle[1] == -1){
			//1�g�����ꍇ ���̂��߂�dp�e�[�u���K�v
			for (int i = 1; i < L - 1; i++){//2�Ԗڂ̐擪
				if (abs(dp[0][i - 1]) != 2) continue;
				for (int j = i + 1; j < L; j++){//�R�Ԗڂ̐擪
					if (dp[i][j - 1] != 3) continue;
					if (abs(dp[j][L - 1]) != 4) continue;
					REP(a, 4){
						REP(b, 4){
							if (1 + a + b > X) continue;
							if (dp[0][i - 1] > 0 && a % 2 != 0)continue;
							if (dp[0][i - 1] < 0 && a % 2 == 0)continue;
							if (dp[j][L - 1] > 0 && b % 2 != 0)continue;
							if (dp[j][L - 1] < 0 && b % 2 == 0)continue;
							yn[1 + a + b] = true;
							continue;
						}
					}
				}
			}

			//�Q�g�����ꍇ
			//������(L-1)*(L-1)��S�Ċm���ߐ��������ꍇ��mod4�����߂�rest�Ƃ̈�v���m���߂�B
			for (int i = 0; i < L - 1; i++){//�O���̋�؂�̎�O
				if (abs(dp[0][i]) != 2) continue;
				for (int j = 0; j < L - 1; j++){//�㔼�̋�؂�̎�O
					if (abs(calc(dp[i + 1][L - 1], dp[0][j])) != 3) continue;
					if (abs(dp[j + 1][L - 1]) != 4) continue;
					REP(a, 4){
						REP(b, 4){
							REP(c, 4){
								if (2 + a + b + c > X) continue;
								if (dp[0][i] > 0 && a % 2 != 0)continue;
								if (dp[0][i] < 0 && a % 2 == 0)continue;
								if (calc(dp[i + 1][L - 1], dp[0][j]) > 0 && b % 2 != 0) continue;
								if (calc(dp[i + 1][L - 1], dp[0][j]) < 0 && b % 2 == 0) continue;
								yn[2 + a + b + c] = true;
								continue;
							}
						}
					}
				}
			}
			bool flag = true;

			if (X >= 12) { X = 11; }
			for (int r = rest; r <= X; r += 4){
				if (r > 0){
					if (yn[r]) {
						printf("Case #%d: YES\n", C);
						flag = false;
						break;
					}
				}
			}

			if (flag) printf("Case #%d: NO\n", C);
		}
		else{
			//1�g�����ꍇ ���̂��߂�dp�e�[�u���K�v
			for (int i = 0; i <= L - 1; i++){//2�Ԗڂ̐擪
				if (i > 0 && (abs(dp[0][i - 1]) == 3 || abs(dp[0][i - 1]) == 4) && abs(cycle[1]) == 2) continue;
				if (i > 0 && abs(cycle[1]) != 2 && abs(cycle[1]) == abs(dp[0][i - 1]))continue;
				for (int j = i + 1; j <= L; j++){//�R�Ԗڂ̐擪
					if (abs(dp[i][j - 1]) != 3) continue;
					if (j < L && (abs(dp[j][L - 1]) == 2 || abs(dp[j][L - 1]) == 3 ) && abs(cycle[1]) == 4) continue;
					if (j < L && abs(dp[j][L - 1]) != 4 && abs(cycle[1]) == abs(dp[j][L-1]) ) continue;
					REP(a, 4){
						REP(b, 4){
							if (1 + a + b > X) continue;
							if (i - 1 == -1 && cycle[a] == 2 && dp[i][j - 1] == 3 && calc(dp[j][L - 1], cycle[b]) == 4) {
								yn[1 + a + b] = true;
								continue;
							}
							if (j == L && calc(cycle[a], dp[0][i - 1]) == 2 && dp[i][j - 1] == 3 && cycle[b] == 4) {
								yn[1 + a + b] = true;
								continue;
							}
							/*printf("1ko %d %d %d %d   %d %d %d\n", i, j, a, b, calc(cycle[a], dp[0][i - 1]), dp[i][j - 1], calc(dp[j][L - 1], cycle[b]));*/
							if (calc(cycle[a], dp[0][i - 1]) == 2 && dp[i][j - 1] == 3 && calc(dp[j][L - 1], cycle[b]) == 4) {
								yn[1 + a + b] = true;
							}
						}
					}
				}
			}

			//�Q�g�����ꍇ
			for (int i = 0; i <= L - 1; i++){//�O���̋�؂�̎�O
				if (abs(dp[0][i]) >= 3 && abs(cycle[1]) == 2) continue;
				if (abs(cycle[1]) != 2 && abs(cycle[1]) == abs(dp[0][i]))continue;
				for (int j = 0; j <= L - 1; j++){//�㔼�̋�؂�̎�O
					if (i + 1 < L && (abs(dp[i + 1][L - 1] * dp[0][j]) == 2 || abs(dp[i + 1][L - 1] * dp[0][j]) == 4) && abs(cycle[1]) == 3) continue;
					if (i + 1 < L && abs(cycle[1]) != 3 && abs(dp[i + 1][L - 1] * dp[0][j]) == abs(cycle[1]) )continue;
					if (j + 1 < L && (abs(dp[j + 1][L - 1]) == 2 || abs(dp[j + 1][L - 1]) == 3) && abs(cycle[1]) == 4 ) continue;
					if (j + 1 < L && abs(cycle[1]) != 4 && abs(dp[j + 1][L - 1]) == abs(cycle[1]))continue;
					REP(a, 4){
						REP(b, 4){
							REP(c, 4){
								if (2 + a + b + c > X) continue;
								if (j + 1 == L && calc(cycle[a], dp[0][i]) == 2 && calc(calc(dp[i + 1][L - 1], cycle[b]), dp[0][j]) == 3 && cycle[c] == 4) {
									yn[2 + a + b + c] = true;
									continue;
								}
								if (i + 1 == L && calc(cycle[a], dp[0][i]) == 2 && calc(cycle[b], dp[0][j]) == 3 && calc(dp[j + 1][L - 1], cycle[c]) == 4) {
									yn[2 + a + b + c] = true;
									continue;
								}
								/*printf("2ko %d %d %d %d %d  %d %d %d\n", i, j, a, b, c, calc(cycle[a], dp[0][i]), calc(calc(dp[i + 1][L - 1], cycle[b]), dp[0][j]), calc(dp[j + 1][L - 1], cycle[c]));*/
								if (calc(cycle[a], dp[0][i]) == 2 && calc(calc(dp[i + 1][L - 1], cycle[b]), dp[0][j]) == 3 && calc(dp[j + 1][L - 1], cycle[c]) == 4) {
									yn[2 + a + b + c] = true;
								}
							}
						}
					}
				}
			}
			bool flag = true;

			if (X >= 12) { X = 11; }
			for (int r = rest; r <= X; r += 4){
				if (r > 0){
					if (yn[r]) {
						printf("Case #%d: YES\n", C);
						flag = false;
						break;
					}
				}
			}

			if (flag) printf("Case #%d: NO\n", C);
		}


		/*//1�g�����ꍇ ���̂��߂�dp�e�[�u���K�v
		for (int i = 0; i <= L - 1; i++){//2�Ԗڂ̐擪
			if (i > 0 && abs(dp[0][i - 1]) >= 3 && abs(cycle[1]) <= 2) continue;
			for (int j = i + 1; j <= L; j++){//�R�Ԗڂ̐擪
				if (abs(dp[i][j-1]) != 3) continue;
				if (j < L && abs(dp[j][L - 1]) >= 2 && abs(dp[j][L - 1]) <= 3 && (abs(cycle[1]) == 4 || abs(cycle[1]) == 1) ) continue;
				REP(a, 4){
					REP(b, 4){
						if (1 + a + b > X) continue;
						if (i - 1 == -1 && cycle[a] == 2 && dp[i][j - 1] == 3 && calc(dp[j][L - 1], cycle[b]) == 4) {
							yn[1 + a + b] = true;
							continue;
						}
						if (j == L && calc(cycle[a], dp[0][i - 1]) == 2 && dp[i][j - 1] == 3 && cycle[b] == 4) {
							yn[1 + a + b] = true;
							continue;
						}*/
						/*printf("1ko %d %d %d %d   %d %d %d\n", i, j, a, b, calc(cycle[a], dp[0][i - 1]), dp[i][j - 1], calc(dp[j][L - 1], cycle[b]));*/
						/*if (calc(cycle[a], dp[0][i - 1]) == 2 && dp[i][j - 1] == 3 && calc(dp[j][L - 1], cycle[b]) == 4) {
							yn[1 + a + b] = true;
						}
					}
				}
			}
		}

		//�Q�g�����ꍇ
		//������(L-1)*(L-1)��S�Ċm���ߐ��������ꍇ��mod4�����߂�rest�Ƃ̈�v���m���߂�B
		for (int i = 0; i <= L-1; i++){//�O���̋�؂�̎�O
			if (i > 0 && abs(dp[0][i]) >= 3 && abs(cycle[1]) <= 2) continue;
			for (int j = 0; j <= L-1; j++){//�㔼�̋�؂�̎�O
				if ((abs(dp[i + 1][L - 1] * dp[0][j]) == 2 || abs(dp[i + 1][L - 1] * dp[0][j]) == 4)&& ( abs(cycle[1]) == 1 || abs(cycle[1]) == 3) ) continue;
				if (j < L && abs(dp[j+1][L - 1]) >= 2 && abs(dp[j+1][L - 1]) <= 3 && (abs(cycle[1]) == 4 || abs(cycle[1]) == 1) ) continue;
				REP(a, 4){
					REP(b, 4){
						REP(c, 4){
							if (2 + a + b + c > X) continue;
							if (j + 1 == L && calc(cycle[a], dp[0][i]) == 2 && calc(calc(dp[i + 1][L - 1], cycle[b]), dp[0][j]) == 3 && cycle[c] == 4) {
								yn[2 + a + b + c] = true;
								continue;
							}
							if (i+1 == L && calc(cycle[a], dp[0][i]) == 2 && calc(cycle[b], dp[0][j]) == 3 && calc(dp[j + 1][L - 1], cycle[c]) == 4) {
								yn[2+ a + b + c] = true;
								continue;
							}*/
							/*printf("2ko %d %d %d %d %d  %d %d %d\n", i, j, a, b, c, calc(cycle[a], dp[0][i]), calc(calc(dp[i + 1][L - 1], cycle[b]), dp[0][j]), calc(dp[j + 1][L - 1], cycle[c]));*/
							/*if (calc(cycle[a], dp[0][i]) == 2 && calc(calc(dp[i+1][L-1], cycle[b]), dp[0][j]) == 3 && calc(dp[j+1][L-1], cycle[c]) == 4) {
								yn[2 + a + b + c] = true;
							}
						}
					}
				}
			}
		}
		bool flag = true;

		if (X >= 12) { X = 11; }
			for (int r = rest; r <= X; r += 4){
				if (r > 0){
					if (yn[r]) {
						printf("Case #%d: YES\n", C);
						flag = false;
						break;
					}
				}
			}

			if(flag) printf("Case #%d: NO\n", C);*/

		}//for C

	return 0;
}

/* printf("Case #%d:",C); */