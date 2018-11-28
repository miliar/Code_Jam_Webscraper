#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int N,M;
string tstr;
 
 

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int nTestCase = 0; 
	cin >> nTestCase;

	for (int iTestCase = 1; iTestCase <= nTestCase; iTestCase++){
		printf("Case #%d: ",iTestCase);
		string answer ="";

		cin >> tstr;
		N = tstr.length();

		answer = tstr[0];
		for (int i = 1; i < N; i++){
			if (tstr[i] >= answer[0])
				answer = tstr[i] + answer;
			else
				answer = answer + tstr[i];
		}
		cout << answer << endl;

	}
	return 0;
}