#include <stdio.h>
#include <math.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <functional>


using namespace std;

typedef long long int int64;



//jamA
int main(void)
{
	int nTestCase, repeat;
	int i;

//	int64 v1[800], v2[800];
	vector<int64> v1, v2;
	int64 r, t;
	int64 S, N, a, b, c;

	cin >> nTestCase;
	for(repeat = 1; repeat <= nTestCase; repeat++){
		cin >> r;
		cin >> t;

		// N�̃����O��h��Ԃ����߂ɕK�v�ȗe�ʂ́A
		// N(2r+2N-1) mL�@�ł���B
		// N(2r+2N-1) <= t�@�𖞂����ő��N�����߂�B
		// �ŏ��́A������x�̌덷��������ŏ����l�����߂�

//		double t = sqrt(pow(r / 2.0, 2) + 

		N = 1;
		for(i = 0; i < 64; i++){
			S = N * (2 * r + 2 * N - 1);
			if(S >= t){
				break;
			}
			N *= 2;
//			cerr << "Case #" << repeat << ": searching...N=" << N << ", S=" << S << ", t=" << t << endl;
		}
		// �����ŁAS(N) >= t�ƂȂ��Ă���͂�
		if(S == t){ // ���łɂ҂����蓚�����o����A���I��
			cout << "Case #" << repeat << ": " << N << endl;
			continue;
		}

		// �Q�������Ȃ���A�T�[�`
		// a�`b�܂ł̊Ԃ����X�ɋ��߂�
		// a�͊܂ނ��Ab�͊܂܂Ȃ�
		// b - a = 1�@�̂Ƃ���a�������B
		a = N / 2;
		b = N;
		while(1){
			if(b - a == 1){ // OK
				cout << "Case #" << repeat << ": " << a << endl;
				break;
			}
			c = (a + b) / 2; // �^��
			S = c * (2 * r + 2 * c - 1); // c��̉~��`���Ƃ��ɕK�v�ȗe��

//			cerr << "Case #" << repeat << ": searching...N=[" << a << ", " << b << "), S=" << S << ", t=" << t << endl;
			if(S == t){
				cout << "Case #" << repeat << ": " << c << endl;
				break;
			}
			if(S > t){ // �͈͍X�V
				b = c;
			}else{
				a = c;
			}
		}
	}

	return 0;
}

