#include <iostream>

using namespace::std;

#define NMAX 101

void init_pancakes(int pancakes[]) {
	for(int i=0; i<NMAX; i++) {
		pancakes[i] = 0;
	}
}

// N -> number of pancakes
// p -> pivot point
// ---+-- at p=2 becomes ++++--, at p=4 becomes +-+++- etc
void flip(int p, int N, int pancakes[]) {
	int temp[NMAX];

	for(int i=0; i<=p; i++) {
		temp[i] = (1+pancakes[p-i])%2;	//flip the pancake. 0<->1
	}

	for(int i=0; i<=p; i++)
		pancakes[i] = temp[i];
}

// scan the stack for the first discontinuity
// for ----++ return 3, for +-+ return 1, +++ return 2 etc
int scan(int N, int pancakes[]) {
	int p = 0;
	int state = pancakes[0];

	for(int i=1; i<N; i++) {
		if(state != pancakes[i])
			return (i-1);
	}
	return (N-1);
}

int calculate_min_number_of_flips(int N, int pancakes[]) {
	int pivot = 0;

	for(int operations=0;;operations++) {
		pivot = scan(N, pancakes);
		if (pivot == N-1 && pancakes[0] == 1)
			return operations;
		flip(pivot, N, pancakes);
	}
	return -1;
}

int revenge_of_pancakes() {
	string input = "";
	int pancakes[NMAX] = {0};
	int length;

	getline(cin, input);
	length = input.length();

	//initialize pancakes stack
	for(int i=0; i<length; i++) {
		if(input[i] == '+')
			pancakes[i] = 1;
	}

	return calculate_min_number_of_flips(length, pancakes);

}

void print_output(int T, int counter) {
	 	cout << "Case #" << T << ": " << counter << endl;
}

int main() {
	string input = "";
	int T=0;
	int result = 0;

	getline(cin, input);
	T = stoi(input);

	for(int t=0; t<T; t++) {
		result = revenge_of_pancakes();
		print_output(t+1, result);
	}
	return 0;
}
