#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
ofstream outFile("C-small-attempt2.out");
ifstream inFile("C-small-attempt2.in");

#define I 2
#define J 3
#define K 4
#define PLUS 1
#define MINUS -1

int T;
int L, X;
string S;

int main()
{
	inFile >> T;
	bool Output = false;
	for (int testcase = 0; testcase < T; testcase++){
		Output = false;
		inFile >> L >> X;
		inFile >> S;

		int Current = 1;
		int Sign = PLUS;
		int Result = I;
		for (int n = 0; n < X; n++){
			for (int i = 0; i < L; i++){
				if (Current == 1){ // 1
					Current = S[i] - 'i' + I;
				}
				else if (Current == I){ // i
					if (S[i] == 'i'){
						Current = 1;
						Sign *= MINUS;
					}
					else if (S[i] == 'j'){
						Current = K;
					}
					else if (S[i] == 'k'){
						Current = J;
						Sign *= MINUS;
					}
				}
				else if (Current == J){ // j 
					if (S[i] == 'i'){
						Current = K;
						Sign *= MINUS;
					}
					else if (S[i] == 'j'){
						Current = 1;
						Sign *= MINUS;
					}
					else if (S[i] == 'k'){
						Current = I;
					}

				}
				else if (Current == K){ // k
					if (S[i] == 'i'){
						Current = J;
					}
					else if (S[i] == 'j'){
						Current = I;
						Sign *= MINUS;
					}
					else if (S[i] == 'k'){
						Current = 1;
						Sign *= MINUS;
					}
				}

				if (Current == Result && Sign == PLUS){
					if (Result == K)
						Output = true;
					Current = 1;
					Result++;
				}
			}	
		}
		if (Output == true && (Current != 1 || Sign != 1))
			Output = false;

		outFile << "Case #" << testcase + 1 << ": ";
		if ( Output )
			outFile << "YES" << endl;
		else
			outFile << "NO" << endl;
	}
	outFile.close();
	return 0;
}
