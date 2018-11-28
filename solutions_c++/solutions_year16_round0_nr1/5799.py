#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;

int case_i, case_n;
int a[10];

bool check()
{
	bool ans = true;
	for (int i=0;i<10;i++)
		if (a[i] == 0)
			ans = false;
	return ans;
}

int main()
{
	int n;
	int l;
	string s;
	bool solved;
	char str[20];
	cin >> case_n;
	int k;
	for (case_i=1;case_i<=case_n;case_i++)
	{
		solved = false;
		cin >> n;
		memset(a,0,sizeof(a));
		for (k=1;k<100;k++)
		{
			sprintf(str,"%d",k*n);
			s = str;
			l = s.length();
			for (int i=0; i<l;i++)
			{
				a[s[i] - 48]++;
			}
			if (check()) {
				solved = true;
				break;
			}
		}
		if (solved)
			printf("Case #%d: %d\n", case_i, k*n);
		else
			printf("Case #%d: INSOMNIA\n", case_i);
	}
	return 0;
}