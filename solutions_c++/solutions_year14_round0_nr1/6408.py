#include <iostream>
#include <cstdio>

int main()
{
	freopen("A-small-attempt0.in","r",stdin) ;
	freopen("output.out","w",stdout) ;

	int get ;		// �f�[�^�̑�����\��

	int matrix[4][4] ;		// �J�[�h�z��̒��g
	int answer1[4] ;		// ��ڂ̃J�[�h��
	int answer2[4] ;		// ��ڂ̃J�[�h��

	scanf("%d",&get) ;

	for( int i = 0 ; i < get ; i ++ )
	{
		int count = 0 ;
		int ans = 0 ;

		int tmp ;
		scanf("%d",&tmp) ;

		for( int x = 0 ; x < 4 ; x ++ )
		{
			for( int y = 0 ; y < 4 ; y ++ )
			{
				scanf("%d",&matrix[x][y]) ;

				if( tmp == x+1 )
				{
					answer1[y] = matrix[x][y] ;
				}
			}
		}

		int tmp2 ;
		scanf("%d",&tmp2 ) ;

		for( int x = 0 ; x < 4 ; x ++ )
		{
			for( int y = 0 ; y < 4 ; y ++ )
			{
				scanf("%d",&matrix[x][y]) ;

				if( tmp2 == x+1 )
				{
					answer2[y] = matrix[x][y] ;
				}
			}
		}

		for( int x = 0 ; x < 4 ; x ++ )
		{
			for( int y = 0 ; y < 4 ; y ++ )
			{
				if( answer1[x] == answer2[y] )
				{
					if( count == 0 )
					{
						ans = answer1[x] ;
					}
					count ++ ;
				}
			}
		}

		// �ǂ����v���Ȃ�
		if( count == 0 )
		{
			printf("Case #%d: Volunteer cheated!\n",i+1 ) ;
		}
		else if( count == 1 )
		{
			printf("Case #%d: %d\n",i+1, ans) ;
		}
		else
		{
			printf("Case #%d: Bad magician!\n",i+1) ;
		}
	}

	return 0 ;
}