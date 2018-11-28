// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

long long composite(long long x);
long long findDivisor(long long binary, long long base);

int main () {
	string line;
	ifstream myfile ("C-small-attempt1.in");
	ofstream outfile;
	outfile.open ("output.txt");
	
	if (myfile.is_open())
	{
		getline (myfile,line);
		long long caseNum = 1;
		
		while ( getline (myfile,line))
		{
			outfile << "Case #" << caseNum << ":\n";
			cout << "Case #" << caseNum << ":\n";
			
			bool hitSpace = false;
			long long N = 0, J = 0;
			for(long long i = 0; i < line.size(); i++) {
				
				if(line[i] == ' ') {
					hitSpace = true;
					
				} else if(hitSpace) {
					J *= 10;
					J += line[i] - '0';
					
				} else {
					N *= 10;
					N += line[i] - '0';
				}
			}
			
			long long binaryRep = pow(2, N-1) + 1, tempBinary, max = pow(2, N), lcd, found = 0;
			bool bits[N];
			long long divisors[9];
			
			while(binaryRep < max && found < J) {
				tempBinary = binaryRep;
				
				long long i = N-1;
				while(tempBinary) {
					bits[i] = tempBinary&1;
					tempBinary = tempBinary >> 1;
					i--;
				}
				
				for(long long i = 2; i <= 10; i++) {
					lcd = findDivisor(binaryRep, i);
					if(lcd == -1) {
						break;
					} else {
						divisors[i-2] = lcd;
					}
					
					if(i == 10) {
						found++;
						
						for(long long j = 0; j < N; j++) {
							outfile << bits[j];
						}
						
						for(long long j = 0; j < 9; j++) {
							outfile << " " << divisors[j];
						}
						
						outfile << endl;
					}
				}
				
				
				//cout << std::endl;
				
				binaryRep += 2;
			}
			
			
			
			caseNum++;
		}
		myfile.close();
	}
	else cout << "Unable to open file"; 
	
	return 0;
}

long long findDivisor(long long binary, long long base) {
	long long decimalForm = 0, i = 0;
	while(binary) {
		decimalForm += pow(base, i)*(binary&1);
		binary = binary >> 1;
		i++;
	}
	
	//cout << decimalForm
	
	return composite(decimalForm);
}

long long composite(long long x) {
  if (x < 2) return x;
  for(long long i=2; i<= sqrt(x); i++) {
    if ((x%i) == 0) return i;
  }
  
  return -1;
}
