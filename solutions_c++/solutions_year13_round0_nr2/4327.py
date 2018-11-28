#include <stdio.h>


FILE *in;
FILE *out;

int grass[100][100];

int cases;
int rows, cols;

bool possible;
bool found;


int main()
{
	in = fopen("input", "r");
	out = fopen("output", "w");

	fscanf(in, "%d\n", &cases);

	for( int k = 0; k < cases; k++ ) {
		possible = true;
		fscanf(in, "%d %d\n", &rows, &cols);
		
		for( int i = 0; i < rows; i++ ) {
			for( int j = 0; j < cols; j++ ) fscanf(in, "%d", &grass[i][j]);
			fscanf(in, "\n");
		}


		// Solve
		for( int i = 0; i < rows; i++ ) {
		for( int j = 0; j < cols; j++ ) {

			found = false;
			if( i == 0 && j == 2 ) {
				i = 0;
			}

			for( int h = 0; h < rows; h++ ) {
				if( grass[h][j] > grass[i][j] ) {
					h = rows;
				}
				if( h == rows - 1 ) found = true;
			}

			for( int h = 0; h < cols; h++ ) {
				if( grass[i][h] > grass[i][j] ) {
					h = cols;
				}
				if( h == cols - 1 ) found = true;
			}

			if( !found ) {
				possible = false;
				i = rows;
				j = cols;
			}

		}}



		// Print out the solution
		if(possible) fprintf(out, "Case #%d: YES\n", k+1);
		else fprintf(out, "Case #%d: NO\n", k+1);
	}

	fclose( out );
	fclose( in );

	return 0;
}
