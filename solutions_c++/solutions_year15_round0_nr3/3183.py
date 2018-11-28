/*#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	int T; cin >> T;
	for (int k = 1; k <= T; k++)
	{
		int smax; cin >> smax;
		string input; cin >> input;
		long long sum = 0, needed = 0;
		for (int i = 0; i <= smax; i++)
		{
			if (sum < i)
			{
				needed += i - sum; sum = i;
			}
			int num = input.at(i) - '0';
			sum += num;
		}
		cout << "Case #" << k << ": " << needed << endl;
	}
	return 0;
}*/
#include<iostream>
#include<string>
#include<cmath>
using namespace std;

//int n[5][5] = { { 0, 0, 0, 0, 0 }, { 0, 1, 2, 3, 4 }, { 0, -2, 1, -4, 3 }, { 0, -3, 4, 1, -2 }, { 0, -4, -3, 2, 1 } };//1for 1,2for i,3 for j,4 for k
int cal[5][5] = { { 0 }, { 0, 1, 2, 3, 4 }, { 0, 2, -1, 4, -3 }, { 0, 3, -4, -1, 2 }, { 0, 4, 3, -2, -1 } };
int main()
{
	freopen("C-small-attempt3.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int T; cin >> T;
	for (int k = 1; k <= T; k++)
	{
		long long l, x; cin >> l >> x;
		l *= x;
		string a, f; cin >> a;
		while (x--)
			f += a;
		long long i = 0; int now = 1;
		for (i = 0; i < l; i++)
		{
			int t = 0;
			switch (f.at(i))
			{
			case 'i': t = 2; break;
			case 'j': t = 3; break;
			case 'k': t = 4; break;
			}
			bool minus = false; if (now < 0) minus = true;
			now = cal[abs(now)][t];
			if (minus) now = -now;
			if (now == 2) break;
		}
		if (i == l)
		{
			cout << "Case #" << k << ": NO" << endl;
			continue;
		}
		i++;
		now = 1;
		for (; i < l;i++)
		{
			int t = 0;
			switch (f.at(i))
			{
			case 'i': t = 2; break;
			case 'j': t = 3; break;
			case 'k': t = 4; break;
			}
			bool minus = false; if (now < 0) minus = true;
			now = cal[abs(now)][t];
			if (minus) now = -now;
			if (now == 3) break;
		}
		if (i == l)
		{
			cout << "Case #" << k << ": NO" << endl;
			continue;
		}
		i++; now = 1;
		for (; i < l; i++)
		{
			int t = 0;
			switch (f.at(i))
			{
			case 'i': t = 2; break;
			case 'j': t = 3; break;
			case 'k': t = 4; break;
			}
			bool minus = false; if (now < 0) minus = true;
			now = cal[abs(now)][t];
			if (minus) now = -now;
			
		}
		if (now==4)
		{
			cout << "Case #" << k << ": YES" << endl;
			continue;
		}
		else
		{
			cout << "Case #" << k << ": NO" << endl;
		}
	}
	return 0;
}