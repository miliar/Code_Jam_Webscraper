#define _CRT_SECURE_NO_WARNINGS

#include <iostream> 
#include <stdio.h>
#include <algorithm>

using namespace std;
  
long long solve(int N){
 	int A[10] = { 0, };
	int tSum = 0;
	long long token = N;

	if (N == 0) return -1;
	for (;;){
		for (int i = token; i > 0; i /= 10){
			if (A[i % 10] == 0){
				A[i % 10]++;
				tSum++;
			}
		}
		if (tSum == 10){
			break;
		}
	//	cout << token <<" "<<tSum<< endl;
		token += N;
 	}


	return token;
}
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int nTestCase = 1; cin >> nTestCase;
	for (int iTestCase = 0; iTestCase < nTestCase; iTestCase++)
	{ 
 		int N;
		cin >> N;

		long long answer = solve(N);
		if (answer == -1)
		{
			printf("Case #%d: INSOMNIA\n", iTestCase + 1);
		}
		else{
			printf("Case #%d: %lld\n", iTestCase + 1, answer);
		}
	}
	return 0;	
}