#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using std::max;
using std::min;

int main() {
    FILE *input;
    FILE *output;

    int numberOfCases;

    input = fopen("input.txt", "r");
    output = fopen("output.txt", "w");

    fscanf(input, "%d", &numberOfCases);

    for(int i = 1; i <= numberOfCases; i++) {
	    int X,R,C;
	    bool winRichard = false; // gabriel

        fscanf(input, "%d", &X);
        fscanf(input, "%d", &R);
        fscanf(input, "%d", &C);

	    if (X==1) { //Srsly..
		    winRichard = false;
	    }
	    else if (X>=7) { // there is one 7 omino that leaves a go
		    winRichard = true;
	    }
	    else if (max(R,C)<X) { // can choose bigger than either size
		    winRichard = true;
	    }
	    else if((R*C)%X > 0) { // grid no fill
		    winRichard = true;
	    }
	    else if(X==2) { // will always fill
		    winRichard = false;
	    }
	    else if(min(R,C)<((float)(X)/2)) { // can find a cute blocker
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

	


        fprintf(output, "Case #%d: ",i);
	    if (winRichard) {
            	fprintf(output, "RICHARD");
	    } else {
            	fprintf(output, "GABRIEL");
	    }	
        fprintf(output, "\n");
    }

    fclose(input);
    fclose(output);

    return 0;
}

