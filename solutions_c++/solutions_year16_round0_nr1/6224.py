#include <iostream>
#include <fstream>
using namespace std;

int main() {
	// your code goes here
	ofstream outfile;
	ifstream infile ("A.in");
	outfile.open("A.out");
	int T;
	infile >> T;
	for (int i = 0; i < T; i++){
		unsigned long long sum = 0;
		int N;
		infile >> N;
		if (N==0){
			outfile << "Case #" << (i+1) << ": INSOMNIA" << endl;
			continue;
		}
		sum = N;
		//string currNum = to_string(sum);
		bool hash[10];
		for (int j = 0; j< 10; j++){
			hash[j] = false;
		}
		bool finished = false;
		while (!finished){
			unsigned long long temp = sum;
			while (temp>0){
				hash[temp%10]=true;
				temp/=10;
			}
			finished = true;
			for (int j = 0; j < 10; j++){
				if (hash[j] == false){
					finished=false;
					break;
				}
			}
			if (finished){
				outfile << "Case #" << (i+1) << ": " << sum << endl;
			}
			sum+=N;
		}
	}
	outfile.close();
	infile.close();
	return 0;
}
