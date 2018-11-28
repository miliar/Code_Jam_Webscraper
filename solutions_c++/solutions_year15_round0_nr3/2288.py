#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string input;
int L;
long long X;

int quatMatrix[5][5];

void initializeMatrix() {
	quatMatrix[1][1] = 1;
	quatMatrix[1][2] = 2;
	quatMatrix[1][3] = 3;
	quatMatrix[1][4] = 4;

	quatMatrix[2][1] = 2;
	quatMatrix[2][2] = -1;
	quatMatrix[2][3] = 4;
	quatMatrix[2][4] = -3;

	quatMatrix[3][1] = 3;
	quatMatrix[3][2] = -4;
	quatMatrix[3][3] = -1;
	quatMatrix[3][4] = 2;

	quatMatrix[4][1] = 4;
	quatMatrix[4][2] = 3;
	quatMatrix[4][3] = -2;
	quatMatrix[4][4] = -1;

}

int multiply(int a,int b) {
	int sign = 1;
	if (a<0) {
		sign *= -1;
		a *= -1;
	}
	if (b<0) {
		sign *= -1;
		b *= -1;
	}
	return sign * quatMatrix[a][b];
}

int convertCtoI(char c) {
	if (c=='1') return 1;
	else if (c=='i') return 2;
	else if (c=='j') return 3;
	else if (c=='k') return 4;
	else return -1;
}

int countValue(string &str) {
	int current = 1;
	for (int i=0;i<str.length();i++) {
		current = multiply(current,convertCtoI(str[i]));
	}
	return current;
}

bool caraSatu() {
	string endString = "";
	for (int i=0;i<X;i++) {
		endString += input;
	}
	int current = 1;
	int phase = 1;
	for (int i=0;i<endString.length();i++) {
		current = multiply(current,convertCtoI(endString[i]));
		if (current == 2 && phase == 1) {
			phase = 2;
			current = 1;
		} else if (current == 3 && phase ==2) {
			phase = 3;
			current = 1;
		} else if (current == 4 && phase ==3) {
			phase = 4;
			current = 1;
		}
	}
	if (phase == 4 && current == 1) return true;
	else return false;

}

bool caraDua() {
	string endString = "";
	for (int i=0;i<28;i++) {
		endString += input;
	}
	int current = 1;
	int phase = 1;
	for (int i=0;i<endString.length();i++) {
		current = multiply(current,convertCtoI(endString[i]));
		if (current == 2 && phase == 1) {
			phase = 2;
			current = 1;
		} else if (current == 3 && phase ==2) {
			phase = 3;
			current = 1;
		} else if (current == 4 && phase ==3) {
			phase = 4;
			current = 1;
		}
	}
	if (phase < 4) return false;
	int next = countValue(input);
	if (next == 1) {
		current = current;
	} else if (next == -1) {
		if (!((X-28LL)%2LL == 0)) current = multiply(current,-1);
	} else if (next>0) {
		long long rem = ((X-28LL)%4LL);
		if (rem==1) current = multiply(current,next);
		else if (rem==2) current = multiply(current,-1);
		else if (rem==3) current = multiply(current,-1 * next);
	} else {
		long long rem = ((X-28LL)%4LL);
		if (rem==1) current = multiply(current,next);
		else if (rem==2) current = multiply(current,-1);
		else if (rem==3) current = multiply(current,next);
	}
	return (current == 1);
}

int main() {
	int t;
	scanf("%d",&t);
	initializeMatrix();
	for (int tc=1;tc<=t;tc++) {
		scanf("%d %lld",&L,&X);
		cin>>input;
		bool result;
		if (X<=28LL) {
			result = caraSatu();
		} else {
			result = caraDua();
		}
		printf("Case #%d: ",tc);
		if (result) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
	return 0;
}