#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
int imax(int a, int b){
	if (a > b) return a;
	else return b;
}
int iabs(int t){
	if (t > 0) return t;
	else return -t;
}
int main(){
	int t;
	cin >> t;
	for (int ii = 0; ii < t; ii++){
		int n;
		cin >> n;
		int list[1001] = { 0 };
		for (int i = 0; i < n; i++){
			cin >> list[i];
		}
		int ans1 = 0, ans2 = 0;
		int max = 0;
		for (int i = 0; i < n-1; i++){
			if (list[i + 1] < list[i]){
				max = imax(max, iabs(list[i] - list[i + 1]));
				ans1 += iabs(list[i] - list[i + 1]);
			}
		}
		for (int i = 0; i < n-1; i++){
			if (list[i] < max) ans2 += list[i];
			else ans2 += max;
		}
		printf("Case #%d: %d %d\n", ii+1, ans1, ans2);
	}
	return 0;
}
