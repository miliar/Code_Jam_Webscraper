#include <iostream>
#include <cstdio>

using namespace std;

string a;
int l;
int case_i, case_n;
char p;
int ans;

int main()
{
	cin >> case_n;
	for (case_i = 1; case_i <= case_n; case_i++)
	{
		ans = 0;
		cin >> a;
		l = a.length();
		p = a[0];
		for (int i = 1; i<l; i++)
		{
			if (a[i] != p)
			{
				p = a[i];
				ans++;
			}
		}
		if (p == '-') ans++;
		printf("Case #%d: %d\n", case_i, ans);
	}
	return 0;
}