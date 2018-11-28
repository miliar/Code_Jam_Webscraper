#include <iostream>
#include <fstream>
#include <string>

void printIndices(unsigned K, unsigned C, std::ofstream& outFile);
unsigned long long uipow(unsigned base, unsigned exp);


const std::string inFileName = "D-small-attempt0.in";
const std::string outFileName = "fractilesShortOUT.txt";


int main() {

    std::ifstream inFile(inFileName);
    std::ofstream outFile(outFileName);



    unsigned T;
    inFile >> T;

    unsigned K, C, S;

    for (unsigned i = 1; i <= T; i++) {

        inFile >> K >> C >> S;
        outFile << "Case #" << i << ":";
        printIndices(K, C, outFile);
        outFile << std::endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}


unsigned long long uipow(unsigned base, unsigned exp) {

    unsigned long long b = base; //resize to fit sizeof result
    unsigned long long result = 1;

    while (exp) {

        if (exp & 1)
            result *= b;

        exp >>= 1;
        b *= b;
    }

    return result;
}

void printIndices(unsigned K, unsigned C, std::ofstream& outFile) {

	unsigned long long len = uipow(K, C);
	unsigned long long diff = len/K; //= uipow(K, C-1)

	unsigned long long ind = 1;
	for (int i = 1; i <= K; i++) {

		outFile << " " << ind;
		ind += diff;
	}
}
