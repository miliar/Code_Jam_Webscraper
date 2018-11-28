#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

#define ANSWER(no, x) cout << "Case #" << no << ": " << x << '\n'; return;

bool isValid(const vector<bool> input){
	for(bool item : input){
		if(!item){
			return false;
		}
	}
	return true;
}
void flip(vector<bool> &input, int to){
	for(int i = 0; i <= to; i++){
		input[i] = !input[i];
	}
}
void printPancake(const vector<bool> input){
	for(bool item : input){
		cout << item;
	}
	cout << '\n';
}

void solve(const int no, vector<bool> input){
	int count = 0;
	while(!isValid(input)){
		int endAt = input.size() - 1;
		for(; endAt >= 0; endAt--){
			if(!input[endAt]){
				break;
			}
		}
		flip(input, endAt);

		count++;
	}
	ANSWER(no, count);
}

int main(const int argc, const char **argv){
	int count;
	cin >> count;
	char unused[2];
	cin.getline(unused, 2);

	for(int i = 0; i < count; i++){
		char buffer[101];
		cin.getline(buffer, 101);
		int size = strlen(buffer);

		vector<bool> input;
		input.reserve(size);
		for(int j = 0; j < size; j++){
			switch(buffer[j]){
				case '+':
					input.push_back(1);
					break;
				case '-':
					input.push_back(0);
					break;
			}
		}

		solve(i+1, input);
	}
}
