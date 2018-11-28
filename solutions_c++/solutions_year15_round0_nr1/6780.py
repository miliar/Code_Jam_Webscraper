#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<sstream>
using namespace std;


int testCase;
int N;
string shyness;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("outputA_Large.txt", "w", stdout);

	scanf("%d", &testCase);
	
	for(int caseId = 1; caseId <= testCase; caseId ++) {
		cin >> N >> shyness;
		int result = 0;
		int currentCount = 0;
		for(int i = 0; i <= N; i ++) {
			if(currentCount < i){
				result += (i - currentCount);
				currentCount += i - currentCount;
			}
			currentCount += shyness[ i ] - '0';
		}

		printf("Case #%d: %d\n", caseId, result);
	}
	return 0;
}