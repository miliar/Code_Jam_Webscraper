#include <iostream>
#define LIMIT (10000000000LL)
using namespace std;

//char ans[100];
bool numbers[10];
int count = 10;
void countNumbers(int n);

int main(int argc, char const *argv[]) {
	int numTests, currNum;
	cin >> numTests;

	for(int i = 1; i <= numTests; ++i){
		for(int j =0; j<10; ++j)
			numbers[j] = false;
		count = 10;


		cin >> currNum;
		int temp = currNum;
		long long int index = 0;
		while(count != 0 && index < LIMIT){
			++index;
			countNumbers(temp);
			temp = temp + currNum;
		}

		cout << "Case #" << i << ": ";
		if(index < LIMIT)
			cout << temp - currNum <<"\n";
		else cout << "INSOMNIA\n";
	}
	return 0;
}


void countNumbers(int n){
	while(n > 0){
		int temp = n%10;
		n = n/10;
		if(!numbers[temp]){
			--count;
			numbers[temp] = true;
		}
	}
}
