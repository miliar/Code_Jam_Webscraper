/**
* Sample solution.
* Problem: Standing Ovation.
* Author: Yu GU (ygu16@hawk.iit.edu)
**/
#include <iostream>
using namespace std;

#define MAX 10

int main()
{
	int T, S_max,k;

	cin >> T;
	k = T;
	while (T)
	{
		cin >> S_max;
		int S[MAX],req = 0, cnt = 0;
		char A[MAX];
		cin >> A;
		for (int i = 0; i < S_max+1; i++)
		{
			S[i] = A[i]-'0';
		}

		for (int i = 1; i < S_max+1; i++)
		{
			cnt += S[i-1];
			if ((i>cnt)&&(S[i]!=0))//more req then present
			{
				req += (i - cnt);
				cnt += req;
			}
		}
		cout << "Case #" << (k - T + 1) << ": " << req << endl;
		T--;
	}
	return 0;
}