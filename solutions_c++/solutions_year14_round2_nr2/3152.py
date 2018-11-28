#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream inData("input-small.in");
	ofstream outData("output-small.txt");
	int num;
	inData >> num;
	for(int i = 0; i < num; i++){
		
		long int A;
		long int B;
		long int K;
		inData >> A >> B >> K;

		int count = 0;

		for(long int a = A-1; a >= 0; a-- ){
			for(long int b = B-1; b >= 0; b-- ){
				if((a & b) < K){
					count++;
				}
			}
		}

		outData << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}