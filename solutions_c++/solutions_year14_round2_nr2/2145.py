using namespace std;
#include <fstream>

int min(int a, int b){
	if (b < a) return b;
	return a;
}

int difference(int a, int b){
	if (a >= b) return a - b;
	return b - a;
}

int myPow(int x, int p) {
	if (p == 0) return 1;
	if (p == 1) return x;
	return x * myPow(x, p - 1);
}


int significantDigits(unsigned int n, int L){
	int ret = 0;
	while (n){
		n = n >> 1;
		ret++;

	}
	return ret;

}

int CountONES(unsigned int n, int L){
	int ret = 0;
	for (int i = 0; i < L; i++)
	{
		if (1 << i & n) ret++;

	}
	return ret;
}

int main(int argc, char * argv[])
{
	long icase = 0;
	int T = 0;
	unsigned int A, B, K = 0;

	std::fstream infile;
	infile.open("C:\\Users\\Nacho\\Desktop\\input.in", ios_base::in);
	std::fstream outfile;
	outfile.open("C:\\Users\\Nacho\\Desktop\\output.txt", ios_base::out);

	if (infile >> T){
		while (icase < T){
			if (infile >> A){
				if (infile >> B){
					if (infile >> K){

						//int maxResultNumber = min(A,B); //this is the maximum number that we can get from the & operation
						//int maxNumber = min(maxResultNumber, K);

						//													 // IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
						//int usefulDigits = significantDigits(maxResultNumber, 10); // 10 IS BECAUSE NO NUMBER IS BIGGER THAN 1000
						//													// CHANGE FOR LARGE INPUT
						//													// DO THIS FOR ALL significantDigits

						//

						//int Adigits = significantDigits(A, 10);
						//int Bdigits = significantDigits(B, 10);
						//int digitDifference = difference(Adigits, Bdigits);
						//int digitDifferenceCombinations = myPow(2, digitDifference);
						//
						//
						//int combinations = 0;
						//for (int i = 1; i <= maxNumber; i++){
						//	int fixedOnes = CountONES(i, 10); // CHANGE FOR LARGE INPUT

						//	combinations += myPow(3, usefulDigits - fixedOnes) * digitDifferenceCombinations;
						//}

						int combinations = 0;
						for (unsigned int j = 0; j < A; j++){
							for (unsigned int i = 0; i < B; i++){
								if ( (j&i) < K) combinations++;
							}
						}

						if (icase > 0) outfile << endl;

						outfile << "Case #" << icase + 1 << ": " << combinations;

						icase++;
						continue;

					}
				}
			}
		}
	}
}