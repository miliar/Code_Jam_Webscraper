// cj.cpp : Defines the entry point for the console application.
//

#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"

int arr[100][100];
int v[100][100];



void isReachable(int N, int M, int i, int j, int value) {
	if( arr[i][j] < value ) {
		return;
	}

	if ( v[i][j] > value ) {
		v[i][j] = value;
	}
	
	
	if( i + 1 < N && v[i+1][j] > value ) {
		isReachable(N,M,i+1,j,value);
	}
	if( j + 1 < M && v[i][j+1] > value ) {
		isReachable(N,M,i,j+1,value);
	}

	if( i > 0 && v[i-1][j] > value ) {
		isReachable(N,M,i-1,j,value);
	}
	if( j > 0 && v[i][j-1] > value ) {
		isReachable(N,M,i,j-1,value);
	}

	
}

typedef long long ll;

int main(int argc, char* argv[])
{
	FILE *in = fopen("D:/codejam/cj/cj/a.in","r");
	FILE *out = fopen("D:/codejam/cj/cj/a.out","w");

	int TC = 0 ;
	fscanf(in,"%d",&TC);
	
	


	for( int t = 1 ; t <= TC ; t++ ) {
		ll A = 0 ;	
		ll B = 0 ;	
		
		char str[100];
		char tstr[100];

		
		fscanf(in,"%lld%lld",&A,&B);
		
		ll rootA = (ll) sqrt((double)A);
		ll rootB = (ll) (sqrt((double)B) + 1);
		int count=0;
		for( ll i = rootA ; i <= rootB ; i++ ) {
			ll sq = i*i;
			if( sq >= A && sq <= B ) {

				sprintf(str,"%lld",sq);
				strcpy(tstr,str);
				strrev(tstr);

				if( strcmp(str,tstr) == 0) {
					sprintf(str,"%lld",i);
					strcpy(tstr,str);
					strrev(tstr);
					if( strcmp(str,tstr) == 0) {
						count++;
					}
				}
			}
		}


		fprintf(out,"Case #%d: %d\n",t,count);
			

	}
	
	fclose(in);
	fclose(out);
	return 0;
}

