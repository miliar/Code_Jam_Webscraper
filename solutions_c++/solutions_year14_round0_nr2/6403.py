#include <iostream>
#include <vector>
#include <cstdio>

int main()
{
	freopen("B-large.in","r",stdin) ;
	freopen("output_large.out","w",stdout) ;


	int get ;		// �f�[�^����

	double cost ;		// �N�b�L�[�t�@�[���������̃R�X�g
						// ��蕶���� C �ɂ�����

	double power ;		// �N�b�L�[�t�@�[���������̐��Y��
						// ��蕶���� F �ɂ�����

	double target ;		// �ڎw���N�b�L�[�̐�
						// ��蕶���� X �ɂ�����

	scanf("%d",&get) ;

	for( int i = 0 ; i < get ; i ++ )
	{
		scanf("%lf",&cost) ;
		scanf("%lf",&power) ;
		scanf("%lf",&target) ;

		double nowper ;
		double nowtime ;

		nowper = 2.0 ;
		nowtime = 0.0 ;
		double lastper = nowper ;
		double lasttime = nowtime ;

		double total ;				// ���݂̍ŒZ�̎���
		total = target / nowper ;

		// ����num���[�̂�������₵�Ă����t�@�[����
		for( int num = 1 ; ; num ++ )
		{
			double tmptime ;		// �t�@�[����num�Ɏ���܂ł̎��Ԃ��i�[����
			tmptime = cost / lastper ;
	//		time.push_back( tmptime ) ;
			nowtime = tmptime + lasttime ;

			// ����Ńt�@�[����num�Ɏ���܂ł̎��Ԃ͊i�[���ꂽ

			double tmppow ;			// �t�@�[����num�̑����Y��
			tmppow = lastper + power ;
	//		per.push_back( tmppow ) ;
			nowper = tmppow ;

			// ����Ńt�@�[����num�̑����Y�͂͊i�[���ꂽ

			// ���̓t�@�[����num�̏�Ԃ��� target ���̃N�b�L�[�𐶎Y����̂ɂ����鎞�Ԃ����߂�
			double tmp_totime ;
			tmp_totime = target / nowper ;

			if( total <= nowtime + tmp_totime )
			{
				break ;
			}
			else
			{
				total = nowtime + tmp_totime ;
			}

			lastper = nowper ;
			lasttime = nowtime ;
		}

		printf("Case #%d: %.7lf\n", i+1, total ) ;
	}

	return 0 ;
}