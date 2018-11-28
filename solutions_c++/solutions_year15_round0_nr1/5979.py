#include <iostream>
#include <string>

using namespace std;

int main(){

	int T, N;
	int Answer = 0;
	int input[1001];

	cin >> T;

	for(int TC = 1; TC <=T; TC++){

		cin >> N;

		int size = N+1;

		string Si;
		cin >> Si;

		for(int i=0; i<size; i++)
			input[i] = Si.at(i) - '0';

		Answer = 0;
		int sum = 0;
		for(int i=0; i<size; i++){
			sum += input[i];
			if(i>=sum){
				Answer++;
				sum += 1; 
			}
		}

		cout << "Case #" << TC << ": ";
		cout << Answer << " " << endl;
	}
	return 0;
}