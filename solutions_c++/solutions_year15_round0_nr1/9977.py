#include<iostream>
using namespace std;
#pragma warning(disable:4996)
int main()
{
int T;
cin >> T;
int* r = new int[T];
for (int t = 1; t <= T; t++)
{
	int Smax;
	char* S = new char[1000];
	scanf("%d %s", &Smax, S);
	int cnt = 0;
	int ans = 0;
	for (int i = 0; i < Smax; i++)
	{
		int ss = S[i] - '0';
		int sss = S[i+1] -'0';
		cnt += ss;
		if (sss > 0)
		{
			if (cnt < i + 1)
			{
				int t = (i + 1) - cnt;
				cnt += t;
				ans += t;
			}
		}
			 
	}
	delete []S;
	r[t] = ans;
}
for (int i = 1; i <= T; i++)
cout << "Case #" << i << ": "<<r[i]<<endl;
}