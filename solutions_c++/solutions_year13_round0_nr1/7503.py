#include <stdio.h>

int arr[5][5];

int main(void)
{
	int i,j,k;
	char temp;
	bool empty;
	bool flag;
	int test, test_case;

	FILE *fin = fopen("input","r");
	FILE *fout = fopen("output.txt","w");
	fscanf(fin,"%d",&test_case);

	for( test = 1 ; test <= test_case ; test ++ ){
		fscanf(fin,"\n");
		empty = false;
		for( i = 1 ; i <= 4 ; i ++ ){
			for( j = 1 ; j <= 4 ; j ++ ){
				fscanf(fin,"%c",&temp);
				switch( temp ){
					case 'X' : arr[i][j] = 1; break;
					case 'O' : arr[i][j] = 2; break;
					case '.' : arr[i][j] = 0; empty = true; break;
					case 'T' : arr[i][j] = 3; break;
					default : j--;
				}
			}
			fscanf(fin,"\n");
		}

		// 'X' - 01 'O' - 10 'T' - 11
		for( i = 1 ; i <= 4 ; i ++ ){
			for( k = 1 ; k <= 2 ; k ++ ){
				flag = true;
				for( j = 1 ; j <= 4 ; j ++ ){
					flag = flag && (arr[i][j] & k);
				}
				if( flag ) break;
			}
			if( flag ) break;
		}
		if( flag ){
			fprintf(fout,"Case #%d: %c won\n",test,(k-1)?'O':'X');
			continue;
		}

		for( i = 1 ; i <= 4 ; i ++ ){
			for( k = 1 ; k <= 2 ; k ++ ){
				flag = true;
				for( j = 1 ; j <= 4 ; j ++ ){
					flag = flag && (arr[j][i] & k);
				}
				if( flag ) break;
			}
			if( flag ) break;
		}

		if( flag ){
			fprintf(fout,"Case #%d: %c won\n",test,(k-1)?'O':'X');
			continue;
		}

		for( k = 1 ; k <= 2 ; k ++ ){
			flag = true;
			for( j = 1 ; j <= 4 ; j ++ ){
				flag = flag && (arr[j][j] & k);
			}
			if( flag ) break;
		}

		if( flag ){
			fprintf(fout,"Case #%d: %c won\n",test,(k-1)?'O':'X');
			continue;
		}

		for( k = 1 ; k <= 2 ; k ++ ){
			flag = true;
			for( j = 1 ; j <= 4 ; j ++ ){
				flag = flag && (arr[j][5-j] & k);
			}
			if( flag ) break;
		}
		if( flag ){
			fprintf(fout,"Case #%d: %c won\n",test,(k-1)?'O':'X');
			continue;
		}
		fprintf(fout,"Case #%d: %s\n",test,empty?"Game has not completed":"Draw");
	}

	return 0;
}
