#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <utility>
#include <iomanip>
 
using namespace std;

double A[1010], B[1010];
int N;
bool used[1010];
 
int main() {
	ifstream cin("D-large.in");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		cin >> N;
		for(int i = 0; i < N; i++)
			cin >> A[i];
		for(int j = 0; j < N; j++)
			cin >> B[j];
		sort(A, A + N);
		sort(B, B + N);
		for(int i = 0; i < N; i++)
			used[i] = 0;
		int a = 0, b = 0, l, r;
		for(l = N - 1, r = N - 1; l >= 0 && r >= 0; ) {
			if(A[l] > B[r])
				a++, l--, r--;
			else
				r--;
		}
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(A[i] < B[j] && !used[j]) {
					used[j] = 1;
					break;
				}
			}
		}
		for(int i = 0; i < N; i++)
			if(!used[i])
				++b;
		cout << "Case #" << t + 1 << ": " << a << " " << b << endl;	
	}
	return 0;
}