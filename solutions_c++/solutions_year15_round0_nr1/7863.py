#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

void solve(int caseNum, int shyCount, string shyneses){
	int additionalGuys = 0;
	int prefixSum = 0;

	for (int i = 0; i < shyneses.length(); ++i){
		int curShynesCount = shyneses[i] - '0';
		if (curShynesCount > 0 && prefixSum < i){
			additionalGuys += i - prefixSum;
			prefixSum = i + curShynesCount;
		}
		else{
			prefixSum += curShynesCount;
		}
	}
	printf("Case #%d: %d\n", caseNum, additionalGuys);
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;

	for(int q = 1; q <= t; ++q){
		int count;
		string shyneses;
		cin >> count >> shyneses;

		solve(q, count, shyneses);
	}
	return 0;
}