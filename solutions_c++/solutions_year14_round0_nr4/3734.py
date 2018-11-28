#include <iostream>
#include <algorithm>    // std::sort
#include <vector>  
#include <stdio.h>
using namespace std;

int N;
double Ken[1000];
double Naomi[1000];

bool check(int c) {
	if (c==0) {
		return true;
	}

	for (int i=0; i<c; i++) {
		if (Naomi[N-c+i] < Ken[i]) {
			return false;
		}
	}
	return true;
}

void solve()
{
	cin >> N;
	for (int i=0; i<N; i++) {
		cin >> Naomi[i];
	}
	for (int i=0; i<N; i++) {
		cin >> Ken[i];
	}

	std::sort(Ken,Ken+N);
	std::sort(Naomi,Naomi+N);

/*
	for (int i=0; i<N; i++) {
		cout << Naomi[i] << " ";
	}
	cout << endl;
	for (int i=0; i<N; i++) {
		cout << Ken[i] << " ";
	}
*/
	for (int i=N; i>=0; i--) {
		if (check(i)) {
			cout << i;
			break;
		}
	}

	int s = 0;
	int iK = N-1;
	int iN = N-1;
	while (iN>=0) {
		if (Naomi[iN] > Ken[iK]) {
			s++;
			iN--;
		} else {
			iN--;
			iK--;
		}
	}
	cout << " " << s;

	return;
}

int main() {
	int T;

	cin >> T;

	for (int i=1; i<=T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	// your code goes here
	return 0;
}
