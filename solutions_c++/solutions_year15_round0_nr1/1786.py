#include <iostream>
#include <string>
#include <memory.h>

using namespace std;

const int MAX = 1024;

int pShy[MAX];

int main()
{
	int T, S, nSum, ans;
	string A;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		ans = 0; nSum = 0;
		memset(pShy, 0, sizeof(pShy));
		cin >> S >> A;
		for(int j = 0; j < A.length(); j++)
		{ pShy[j] = A[j] - '0'; }
		for(int j = 0; j <= S; j++)
		{
			if(nSum >= j) { nSum += pShy[j]; }
			else if(pShy[j]) { ans += j - nSum; nSum = j + pShy[j]; }
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
