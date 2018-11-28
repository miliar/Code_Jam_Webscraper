#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
using namespace std;

int main()
{
	freopen("input.txt","r", stdin);
	freopen("output.txt", "w", stdout);
	string S;
	int N;
	int Loo, Loop;
	cin >> Loop;
	for (Loo = 1; Loo <= Loop; Loo++)
	{
		cin >> N >> S;
		int Cur = S[0]-'0';
		int Ans = 0;
		for (int i = 1; i <= N; i++)
		{
			if (S[i] - '0' != 0)
			{
				if (Cur < i)
				{
					Ans += i - Cur;
					Cur = i;
				}
				Cur += S[i] - '0';
			}
		}
		cout << "Case #" << Loo << ": " << Ans << endl;

	}
	fclose(stdout);
	return 0;
	

}
