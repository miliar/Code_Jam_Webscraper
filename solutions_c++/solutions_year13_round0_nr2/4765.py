#include <iostream>


using namespace std;

typedef long long int int64;


//jamB
int main(void)
{
	int nTestCase, repeat;
	int i, j;

	int field[100][100]; // �ő��100x100
	int N, M;
	int arNmax[100], arMmax[100];
	bool result;

	cin >> nTestCase;
	for(repeat = 1; repeat <= nTestCase; repeat++){
		// �e�X�g�P�[�X�ԍ��o��
		cout << "Case #" << repeat << ": ";

		// �s�Ɨ�̐����擾����
		cin >> N;
		cin >> M;

		// ���ꂼ��̍s��̒l���擾����
		for(i = 0; i < N; i++){
			for(j = 0; j < M; j++){
				cin >> field[i][j];
			}
		}

		// �s�Ɨ�̂��ꂼ��̍ő�l���擾����
		// �܂��͏�����
		for(i = 0; i < 100; i++){
			arNmax[i] = 0;
			arMmax[i] = 0;
		}

		// ���ׂĂ̒l���r���āA�s���ƁA�񂲂Ƃ̍ő�l�����߂�
		for(i = 0; i < N; i++){
			for(j = 0; j < M; j++){
				if(field[i][j] > arNmax[i]){
					arNmax[i] = field[i][j];
				}
				if(field[i][j] > arMmax[j]){
					arMmax[j] = field[i][j];
				}
			}
		}

		// ���ׂẴt�B�[���h�̒l�ɑ΂��āA�s������������̂����ꂩ�̍ő�l�����A�l�������������Ȃ��OK.
		// ���̏ꍇ�A�����ƎŊ���@�Ŋ���܂��B
		// �����ꂩ�̍ő�l�����Ⴂ�ꍇ�A�s�����Ɋ����Ă�������Ɋ����Ă��A���̍����܂ł͊�����܂���B
		result = true;
		for(i = 0; i < N; i++){
			for(j = 0; j < M; j++){
				if(field[i][j] < arNmax[i] && field[i][j] < arMmax[j]){
					result = false;
				}
			}
		}

		// �������o��
		if(result){
			cout << "YES" << endl;
		}else{
			cout << "NO" << endl;
		}
	}

	return 0;
}

