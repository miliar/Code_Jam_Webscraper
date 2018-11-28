#include <string>
#include <iostream>
#include <fstream>

using namespace std;



bool seenall(int *seen){
	for(int i = 0; i < 10; i++){
		if(seen[i] != 1)
			return false;
	}
	return true;
}

int updateseen(int *seen, int num){

	int ndigits = 0;
	while(num > 0){
		int digit = num % 10;
		seen[digit] = 1;
		num = num / 10;
		ndigits++;
	}

	return ndigits;
}

int getbound(int ndigits){
	int bound = 10;
	for(int i = 0; i < ndigits; i++){
		bound *= 10;
	}

	return bound;
}

void docount(int num){
	int seen[] = {0,0,0,0,0,0,0,0,0,0};

	if(num != 0){

		int ndigits = updateseen(seen, num);
		int bound = getbound(ndigits);

		for(int i = 2; i < bound; i++){

			updateseen(seen, num*i);

			if(seenall(seen)){
				cout << num*i;
				return;
			}
		}

	}

	cout << "INSOMNIA";

}


int main(int argc, char *argv[]){


	ifstream file(argv[1]);

	int n;
	file >> n;

	for(int i = 0; i < n; i++){

		int num;
		file >> num;

		cout << "Case #" << (i+1) << ": ";
		docount(num);
		cout << endl;
	}
}
