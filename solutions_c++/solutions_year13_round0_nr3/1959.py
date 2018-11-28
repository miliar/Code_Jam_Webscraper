#include<iostream>
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
//This array is the sqare roots of all fair and square numbers up to 10^14 calculated over about 10 minutes.
long long magic[] = {1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};


int countFairNSquare(long long a, long long b) {
	int sum = 0;
	for(int i = 0; i < 39; i++) {
		if(magic[i]*magic[i] >= a && magic[i]*magic[i] <= b)
			sum ++;
		if(magic[i]*magic[i] > b)
			break;
	}
	return sum;
}


int main() {
	int T;
	cin >> T;
	long long A;
	long long B;
	for(int i = 0; i < T; i++) {
		cin >> A >> B;
		
		cout << "Case #" << i + 1 << ": " << countFairNSquare(A,B) << endl;
	}
	return 0;
}
