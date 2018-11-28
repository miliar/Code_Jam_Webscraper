#include <fstream>
#include <iostream>

using namespace std;
void FairAndSquare(char * fileInput, char * fileOutput, bool large) {
	ifstream input(fileInput);
	ofstream output(fileOutput);

	char buffer[256];
	input.getline(buffer, 256);
	int testcaseCount = atoi(buffer);

	for (int i = 0; i < testcaseCount; i++) {
		if (large) {
			char *left, *right;
			input.getline(buffer, 256);
			left = strtok(buffer, " ");
			right = strtok(NULL, " ");
			
			large_int leftLarge(left);
			large_int rightLarge(right);
			large_int number = 0;
			for (large_int j = rightLarge; j >= leftLarge; j = j - 1) {
				string str = j.str();
				bool valid = true;
				//cout << i << endl;
				for (size_t k = 0; k < str.size() / 2; k++) {
					if (str.at(k) != str.at(str.size() - 1 - k)) {
						valid = false;
						break;
					}
				}
				
				//cout << i << endl;
				if (valid == false) continue;

				size_t length = (strlen(right) + 1) / 2;
				char *sqrtNum = new char[length + 2];
				sqrtNum[0] = '1';
				for (size_t i = 0; i < length; i++) {
					sqrtNum[i + 1] = '0';
				}
				sqrtNum[length + 1] = '\0';
				
				large_int sqr(sqrtNum);
				//cout << sqr << endl;
				//cout << j << endl;
				bool isSquare = false;
				while (sqr * sqr >= j) {
					if (sqr * sqr == j) {
						isSquare = true;
						break;
					}
					sqr = sqr - 1;
				}
				if (isSquare == false) continue;
				//cout << i << endl;
				string strSqrt = sqr.str();
				for (int k = 0; k < strSqrt.size() / 2; k++) {
					if (strSqrt.at(k) != strSqrt.at(strSqrt.size() - 1 - k)) {
						valid = false;
						break;
					}
				}
				if (valid) number = number + 1;

			}
			
			output << "Case #" << (i + 1) << ": " << number << endl;

		} else {
			char *left, *right;
			long long leftNum, rightNum;
			input.getline(buffer, 256);
			left = strtok(buffer, " ");
			right = strtok(NULL, " ");
			leftNum = _atoi64(left);
			rightNum = _atoi64(right);

			long long number = 0;
			
			long long leftSqrt = (long long)sqrt(leftNum);
			long long rightSqrt = (long long)sqrt(rightNum) + 1;
			for (long long j = leftSqrt; j <= rightSqrt; j++) {
				long long jSquare = j * j;
				if (!(jSquare >= leftNum && jSquare <= rightNum)) continue;
				char l[128];
				_i64toa(j, l, 10);
				bool valid = true;
				for (size_t k = 0; k < strlen(l) / 2; k++) {
					if (l[k] != l[strlen(l) - k - 1]) {
						valid = false;
						break;
					}
				}
				if (valid == false) continue;

				char sqr_[128];
				_i64toa_s(jSquare, sqr_, 128, 10);
				for (size_t k = 0; k < strlen(sqr_) / 2; k++) {
					if (sqr_[k] != sqr_[strlen(sqr_) - k - 1]) {
						valid = false;
						break;
					}
				}

				if (valid) {
					number++;
				}
			}
			
			output << "Case #" << (i + 1) << ": " << number << endl;

		}
	}
	
	input.close();
	output.close();
}

int main() {
	FairAndSquare("C-small-attempt0.in", "C-test.out", false);
	
}

