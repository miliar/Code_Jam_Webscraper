#include <cstdio>
#include <iostream>

#define DEBUG

/*
 * Files are assigned to stdin and stdout,
 * which allows for console level interaction.
 * Great for debugging.
 */

int main(int argc, char* argv[]) {
	int T; // number of cases (1 <= T <= 100)
	int answer1; // store first answer (1 <= A1 <= 16)
	int answer2; // items in store (1 <= A2 <= 16)
	int firstRow[4]; //row selected by answer A1
	int fromSecondRow;
	int result = 0; //result to output
	int resultFlag = 0;
	int blank;

	//selecting and opening files
	if (argc > 3 || argc == 1) {
		std::cout << "Usage is <inputFile> [<outputFile>]\n";
		return 1;
	}

    freopen(argv[1], "r", stdin);

	if (argc == 3) {
	    freopen(argv[2], "w", stdout);
	} else {
	    freopen("a.out", "w", stdout);
	}

    //Start getting input
    std::cin >> T;

#ifdef DEBUG
std::cerr << "T is  : " << T << "\n";
#endif

    for (int countT = 1; countT <= T; countT++) {
		resultFlag = 0;
    	std::cin >> answer1;

#ifdef DEBUG
std::cerr << "A1 is : " << answer1 << "\n";
#endif

		//load and parse the first row
    	for (int row = 1; row <=4; row++) {
    		if (row == answer1) {
    			for (int col = 1; col <= 4; col++) {
	    			std::cin >> firstRow[col-1];
#ifdef DEBUG
std::cerr << "found " << firstRow[col-1] << "\n";
#endif
       			}
    		} else {
    			for (int countCols = 1; countCols <= 4; countCols++) {
	    			std::cin >> blank; // just skip the row
    			}
    		}
    	}

		std::cin >> answer2;
#ifdef DEBUG
std::cerr << "A2 is : " << answer2 << "\n";
#endif

    	for (int row = 1; row <=4; row++) {
    		if (row == answer2) {
    			for (int cols = 1; cols <= 4; cols++) {
	    			std::cin >> fromSecondRow;
	    			for (int elem = 0; elem <= 3; elem++) {
	    				if (fromSecondRow == firstRow[elem]) {
	    					resultFlag++;
	    					result = fromSecondRow;
	    				}
	    			}
#ifdef DEBUG
std::cerr << "found " << fromSecondRow << "\n";
#endif
       			}
    		} else {
    			for (int countCols = 1; countCols <= 4; countCols++) {
	    			std::cin >> blank; // just skip the row
    			}
    		}
    	}


    	switch (resultFlag) {
    	case 0:
    		std::cout << "Case #" << (countT) << ": Volunteer cheated!\n";
    		break;
		case 1:
			std::cout << "Case #" << (countT) << ": "  << result << "\n";
    		break;
    	default:
    		std::cout << "Case #" << (countT) << ": Bad magician!\n";
    	}
    }
    return 0;
}
