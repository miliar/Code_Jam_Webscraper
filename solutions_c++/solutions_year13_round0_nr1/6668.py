// cj.cpp : Defines the entry point for the console application.
//

#include "stdio.h"
#include "stdlib.h"
#include "string.h"


int main(int argc, char* argv[])
{
	FILE *in = fopen("D:/codejam/cj/cj/a.in","r");
	FILE *out = fopen("D:/codejam/cj/cj/a.out","w");

	int TC = 0 ;
	fscanf(in,"%d",&TC);
	
	char strfull[20];
	
	char arr[10][5];

	for( int t = 1 ; t <= TC ; t++ ) {
		
		strfull[0]=0;

		for( int i = 0 ; i < 4 ; i++ ) {
			fscanf(in,"%s",arr[i]);
			strcat(strfull,arr[i]);
		}
		for( int j = 0 ; j < 4; j++ ) {
			arr[4][j]=arr[j][j] ;
		}
		arr[4][4] = 0;

		for( int j = 0 ; j < 4; j++ ) {
			arr[5][j]=arr[3-j][j] ;
		}
		arr[5][4] = 0;

		for( int i = 0 ; i < 4 ; i ++ ) {
			for( int j = 0 ; j < 4; j++ ) {
				arr[i+6][j] = arr[j][i] ;
			}
			arr[i+6][4] = 0;
		}


		bool inComplete = true ;
		for( int k =0 ; k < 10 ; k++ ) {
			if ( strchr(arr[k],'.') == NULL )  {
				if( strchr(arr[k],'O') == NULL ) {
					inComplete = false ;
					fprintf(out,"Case #%d: X won\n",t);
					break;
				}
				
				if( strchr(arr[k],'X') == NULL ) {
					inComplete = false ;
					fprintf(out,"Case #%d: O won\n",t);
					break;
				}
			}
		}
		if( inComplete ) {
			if( strchr(strfull,'.') != NULL ) {
				fprintf(out,"Case #%d: Game has not completed\n",t);
			} else {
				fprintf(out,"Case #%d: Draw\n",t);
			}
		}

	}
	
	fclose(in);
	fclose(out);
	return 0;
}

