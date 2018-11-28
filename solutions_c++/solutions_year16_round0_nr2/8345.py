#include <iostream>
#include <cstring>

using namespace std;

uint64_t numPancakes(char *arr, int n) {
	int i = 0;
	char st = arr[0];
	while(i<n && arr[i]==st) {
		i++;
	}
	if (st=='+' && i==n) {
		return 0;
	}
	else {
		if (st=='+') {
			st = '-';
		}
		else {
			st = '+';
		}
		for(int j=0; j<i; j++) {
			arr[j] = st;
		}
		return 1+numPancakes(arr, n);
	}
	return 0;
}

int main(int argc, char *argv[]) {
	int cases;
	cin>>cases;
	int ind = 1;
	while(ind <= cases) {
		char *input = new char[100];
		cin>>input;
		cout<<"Case #"<<ind<<": "<<numPancakes(input, strlen(input))<<endl;
		ind++;
		delete input;
	}
	return 0;
}
