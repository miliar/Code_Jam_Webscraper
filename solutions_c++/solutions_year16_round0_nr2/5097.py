#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("B-large.in");
ofstream fout("b.out");

const int MAXN = 1000;
char arr[MAXN];

int getResult() {
	int result = 0;
	int len = 1;
	
	while (arr[len]) {
		if (arr[len - 1] != arr[len]) {
			result++;
		}
		
		len++;
	}
	
	if (arr[len - 1] == '-') {
		result++;
	}
	
	return result;
}

int main() {
	int cases;
	cin >> cases;
	
	for (int cnt = 1; cnt <= cases; cnt++) {
		cin >> arr;
		cout << "Case #" << cnt << ": " << getResult() << endl;
	}
	
	return 0;
}

