/* Author: Fleseriu Cristian Valentin
 * Mail: fleseriu.cristian@webmonsters.ro
 * Google Jam - Qualification Round - Ominous Omino
 */

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using std::max;
using std::min;

int main(int argc, char* argv[]) {
    if(argc < 2) {
        printf("Error: not enough parameters\n");
        printf("Info: usage: ./stading input_file output_file\n");
        return 0;
    }

    FILE *input;
    FILE *output;

    char inputFile[10];
    char outputFile[10];

    int numberOfCases;

    strcpy(inputFile, argv[1]);
    strcpy(outputFile, argv[2]);

    input = fopen(inputFile, "r");
    output = fopen(outputFile, "w");

    if(input == NULL) {
        printf("Error on opening input file\n");
        return 0;
    }

    if(output == NULL) {
        printf("Error on opening output file\n");
        return 0;
    }

    fscanf(input, "%d", &numberOfCases);

    for(int i = 1; i <= numberOfCases; i++) {
	int X,R,C;
	bool winRichard = false; //Richard wins?
	//Go go Gabriel, by default

        fscanf(input, "%d", &X);
        fscanf(input, "%d", &R);
        fscanf(input, "%d", &C);

	if (X==1) { //Srsly..
		winRichard = false;
	}
	else if (X>=7) { //sure edgecase: there is one 7omino that leaves a GO lock
		winRichard = true;
	}
	else if (max(R,C)<X) { //sure edgecase: can choose bigger than either size
		winRichard = true;
	}
	else if((R*C)%X > 0) { //sure edgecase: grid nofill
		winRichard = true;
	}
	else if(X==2) { //sure edgecase: will always fill
		winRichard = false;
	}
	else if(min(R,C)<((float)(X)/2)) { //sure edgecase: can find a cute blocker
		winRichard = true;
	}
	else if(
		(X%2==1 && 
			( 
				((X+1)/2)>C || 
				((X+1)/2)>R
			) 
		) || 
		( X%2==0 && 
			( 
				(X/2)>C || 
				(X/2)>R || 
				(X/2)+1>C || 
				(X/2)+1>R
			)
		)
	) { //diagonal block
		winRichard = true;	
	}

	

	/*
	else if(X==4 or X==5 or X==6) { //tetris S or Z
		winRichard = true;
	}
	else if (X==3 && (R%2>0 || C%3>0) && (R%3>0 || C%2>0) ) {
		winRichard = true;
	}
	else if(X==3) { //sure edgecase: will always fill by this point
		winRichard = false;
	}
	*/

        fprintf(output, "Case #%d: ",i);
	if (winRichard) {
        	fprintf(output, "RICHARD");
	} else {
        	fprintf(output, "GABRIEL");
	}	
        //fprintf(output, " %d %d %d",X,R,C);
        fprintf(output, "\n");
    }

    fclose(input);
    fclose(output);

    return 0;
}

