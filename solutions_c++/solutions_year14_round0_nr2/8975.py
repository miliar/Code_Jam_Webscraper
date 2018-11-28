#include <cstdio>
#include <iostream>
#include <iomanip>

/*
 * Files are assigned to stdin and stdout,
 * which allows for console level interaction.
 * Great for debugging.
 */

int main(int argc, char* argv[]) {
	int T; 			// cases 		(1 <= T <= 100)
	double C;		// farm cost	(1 ≤ C ≤ 50 / 1 ≤ C ≤ 10000)
	double F;	 	// farm prod	(1 ≤ F ≤ 4 / 1 ≤ F ≤ 100)
	double X; 		// target		(1 ≤ X ≤ 2000 / 1 ≤ X ≤ 100000)
	const int BASE_PROD = 2;

	//selecting and opening files
	if (argc > 3 || argc == 1) {
		std::cout << "Usage is <inputFile> [<outputFile>]\n";
		return 1;
	}

    freopen(argv[1], "r", stdin);

	if (argc == 3) {
	    freopen(argv[2], "w", stdout);
	} else {
	    freopen("b.out", "w", stdout);
	}

    //Start getting input
    std::cin >> T;

    for (int countT = 1; countT <= T; countT++) {
    	//input
        std::cin >> C;
        std::cin >> F;
        std::cin >> X;

        bool done = false;
    	double time = 0;
        int farms = 0;
        //process
        while (!done) {
        	double tX0 = X / ( BASE_PROD + (farms * F) );
        	double tX1 = X / ( BASE_PROD + ((farms+1) * F) );
        	double tC = C / ( BASE_PROD + ((farms) * F) );

        	if ( tX0 > (tC + tX1) ) {
        		//better to build a farm, than wait
        		farms++;
        		time+=tC;
        	} else {
        		time+=tX0;
        		done=true;
        	}
        }

    	//output
    	std::cout << "Case #" << (countT) << ": " << std::fixed << std::setprecision(7) << time << "\n";
    }
    return 0;
}
