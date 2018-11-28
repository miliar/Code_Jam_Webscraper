#include <iostream>


using namespace std;

typedef long long int int64;


//jamA
int main(void)
{
	int nTestCase, repeat;
	int i, j;

	int board1[4][4], board2[4][4];
	int compdata[17];
	int ch, line1, line2, ansnum, ans;

	cin >> nTestCase;
	for(repeat = 1; repeat <= nTestCase; repeat++){

		// �e�X�g�P�[�X�ԍ��o��
		cout << "Case #" << repeat << ": ";

		// 1��߂̎w��s�ǂݍ���
		cin >> line1;

		// �{�[�h�ǂݍ���
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++){
				cin >> ch;
				board1[i][j] = ch;
			}
		}

		// 2��߂̎w��s�ǂݍ���
		cin >> line2;

		// �{�[�h�ǂݍ���
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++){
				cin >> ch;
				board2[i][j] = ch;
			}
		}

		// �����f�[�^������������
		for(i = 0; i < 17; i++){
			compdata[i] = 0;
		}

		// 1��ڂ̎w��s�Ɋ܂܂�鐔��compdata�ɓo�^����
		for(i = 0; i < 4; i++){
			compdata[ board1[line1 - 1][i] ] = 1;
		}

		// 2��ڂ̎w��s�Ɋ܂܂�鐔��compdata���猟������
		// �܂܂�Ă��鐔��1�ł���ΐ����B
		ansnum = 0;
		ans = 0;
		for(i = 0; i < 4; i++){
			if(compdata[ board2[line2 - 1][i] ] == 1){
				ansnum++;
				ans = board2[line2 - 1][i];
			}
		}

		// �����蔻��
		if(ansnum == 0){
			cout << "Volunteer cheated!" << endl;
		}else if(ansnum == 1){
			cout << ans << endl;
		}else{
			cout << "Bad magician!" << endl;
		}

	}

	return 0;
}

