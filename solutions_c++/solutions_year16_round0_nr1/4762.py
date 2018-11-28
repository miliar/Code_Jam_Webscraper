#include <iostream>

using namespace std;

int sequence_count(int N, bool* seen);
void process_digit(int N, bool* seen, int& count);
void initialize_false(bool *array, int n);

int main(){
	int testNum;
	int N;
	int count;
	int lastNum;
	bool digit_seen[10] = { false }; 

	cin >> testNum;

	for(int i = 0; i < testNum; i++){

		cin >> N; 
		lastNum = sequence_count(N, digit_seen);
		if(lastNum == 0){
			cout << "Case #" << i+1 <<": INSOMNIA" <<endl;
		}
		else{
			cout << "Case #" << i+1 <<": " << lastNum <<endl;
		}

		initialize_false(digit_seen, 10);
	}
}

int sequence_count(int N, bool* seen){
	int count = 0;
	int factor = 0;

	if(N == 0){
		return 0;
	}

	while(count < 10){
		factor++;
		process_digit(N * factor, seen, count);
	}
	return N*factor;
}

void process_digit(int N, bool* seen, int& count){
	while(N != 0){
		if(seen[N % 10] == false){
			seen[N % 10] = true;
			count++;
		}
		N /= 10;
	}
}

void initialize_false(bool *array, int n){
	for(int i = 0; i < n; i++){
		array[i] = false;
	}
}

