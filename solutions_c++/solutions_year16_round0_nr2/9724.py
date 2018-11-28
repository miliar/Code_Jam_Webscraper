#define _CRT_SECURE_NO_WARNINGS

#include <iostream> 
#include <stdio.h>
#include <algorithm>
#include <string>

using namespace std;
  
string token;
 

int D[200][2] = { 0, };
int solve()
{
	int nLen = token.length();
 	D[0][0] = D[0][1] = 0;
	for (int i = 1; i <= nLen; i++){
		if (token[i-1] == '+'){
			D[i][1] = D[i - 1][1];
			D[i][0] = min(D[i - 1][0] + 2, D[i][1] + 1);
		}
		else{
			D[i][0] = D[i - 1][0];
			D[i][1] = min(D[i][0] + 1, D[i-1][1] + 2);
		}
//		cout << token[i-1] << " " << D[i][0] << " " << D[i][1] << endl;
	}
//	for (int i = 1; i <= nLen; i++)		cout << D[i][0] << " "; cout << endl;
//	for (int i = 1; i <= nLen; i++)		cout << D[i][1] << " "; cout << endl;

		
	return min(D[nLen][1], D[nLen][0] + 1);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "r", stdin);

	int nTestCase = 1; cin >> nTestCase;
 	for (int iTestCase = 0; iTestCase < nTestCase; iTestCase++){ 
		cin >> token;
		printf("Case #%d: %d\n", iTestCase+1,solve());
	}
	return 0;	
}