
#include <iostream>
#include <vector>

int main(int argc, char *argv[]) {
    int numCases;
    std::cin >> numCases;

    for (int thisCase = 1; thisCase <= numCases; thisCase++) {
	std::cout << "Case #" << thisCase << ": ";
	
	int N, M;
	std::cin >> N >> M;

	std::vector< std::vector<int> > request;
	request.resize(N);
	for (std::vector<int> &row : request) {
	    row.resize(M, 0);
	    for (int &height : row) {
		std::cin >> height;
	    }
	}

	//std::cout << std::endl;

	bool stillGood = true;
	for (int i = 0; i < N; i++) {
	    for (int j = 0; j < M; j++) {
		int thisSquare = request[i][j];

		//std::cout << thisSquare;

		bool rowIsGood = true;
		// Check if it's possible to go along the i-axis the lawn
		for (int a = 0; a < N; a++) {
		    if (request[a][j] > thisSquare) {
			rowIsGood = false;
			break;
		    }
		}
		if (rowIsGood == false) {
		    // It's not so lets check going along the j-axis.
		    for (int b = 0; b < M; b++) {
			if (request[i][b] > thisSquare) {
			    stillGood = false;
			    break;
			}
		    }
		}
	    }
	    //std::cout << std::endl;
	}

	if (stillGood) {
	    std::cout << "YES";
	} else {
	    std::cout << "NO";
	}
	
	std::cout << std::endl;
    }
    
}
