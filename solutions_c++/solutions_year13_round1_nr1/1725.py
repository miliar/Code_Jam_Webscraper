#define PI 3.141592654

#include <stdio.h>


int task_c;
int r;
double t;

double nextS;
int cur_r;
int rc;

int main()
{
	FILE *in = fopen( "input", "r" );
	FILE *out = fopen( "output", "w" );
	fscanf( in, "%d\n", &task_c );

	for( int k = 0; k < task_c; k++ ) {
		fscanf( in, "%d %lf\n", &cur_r, &t );
		rc = 0;

		nextS = (cur_r+1)*(cur_r+1) - cur_r*cur_r;
		while( t - nextS >= 0.0 ) {
			t -= nextS;

			cur_r = cur_r + 2;
			nextS = (cur_r+1)*(cur_r+1) - cur_r*cur_r;
			rc++;
		}


		fprintf( out, "Case #%d: %d\n", k+1, rc );
	}


	fclose( out );
	fclose( in );


	return 0;
}
