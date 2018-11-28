#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned long long Number;

bool palindrome(Number n){
	Number t, r, sum = 0;
	t = n;
	while(n){
		r = n % 10;
		n /= 10;
		sum = sum * 10 + r;
	}
	return t == sum;
}

int main(){
	ifstream input("input.txt");
	if (!input){
		cerr << "Failed to open file";
		return 1;
	}
	ofstream output("output.txt");
	
	int lines;
	input >> lines;

	for (int i = 0; i < lines; i++){
		Number a, b;
		input >> a;
		input >> b;

		Number start = (Number)ceil(sqrt((double)a));
		Number squared = start * start;

		int sum = 0;
		while(squared <= b){
			//cout << "Compare " << squared << " and " << start << endl;
			if (palindrome(squared) && palindrome(start)){
				//cout << "Found!" << endl;
				sum++;
			}
			
			start++;
			squared = start * start;
		}

		output << "Case #" << (i + 1) << ": " << sum << endl;
	}

	output.close();
	input.close();

	system("pause");

	return 0;
}