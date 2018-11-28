#include <iostream>
#include <iomanip>

using namespace std;

typedef long long int int64;


//jamA
int main(void)
{
	int nTestCase, repeat;
	int i, j;

	double C, F, X;
	int N, M;

	cin >> nTestCase;
	for(repeat = 1; repeat <= nTestCase; repeat++){

		// �e�X�g�P�[�X�ԍ��o��
		cout << "Case #" << repeat << ": ";

		// �f�[�^�ǂݍ���
		cin >> C >> F >> X;

		// ����X<=C�Ȃ�A�������ĂȂ��Ōp��
		if(X <= C){
			cout << fixed << setprecision(8) << (X / 2) << endl;
			continue;
		}

		// �����Ȃ�A1��ȏ�Farm�����Ă邱�Ƃ��O��ƂȂ�
		// N��Farm�����Ă��Ƃ��ƁAN+1��Farm�����Ă����́A�ǂ��炪���������r����B
		// N = 0����X�^�[�g
		N = 0;
		double total_time = 0;
		double next_farm_time = 0, s = 0, p0, p1;
		double t0 = 0, t1 = 0, a0 = 0, a1 = 0, X0 = 0, X1 = 0;
		while(1){
			M = N + 1;
			a0 = 2 + N * F;
			a1 = 2 + M * F;

			next_farm_time = C / a0;
			s = C / F;
			p1 = a1 * s;

			if(p1 >= X){ // ��_�̍�����X�𒴂����̂ŁAa0�̂Ƃ����ŒZ���ԂƂȂ�
				total_time += X / a0;
				cout << fixed << setprecision(8) ; // �������̐��x�w��Ƃ���B
				cout << total_time << endl;
				break;
			}
			// ��_�̍�����X�𒴂��Ȃ��̂ŁAa1��a0�Ƃ��čČ��؂���
			a1 = a0;
			total_time += C / a0;
			N++;
		}

	}

	return 0;
}

