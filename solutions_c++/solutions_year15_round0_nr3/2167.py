#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<vector>
#include<map>

using namespace std;

map<pair<char, char>, string> mul;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	pair<char, char> p;
	p.first = '1';
	p.second = '1';
	mul[p] = "1";
	p.second = 'i';
	mul[p] = "i";
	p.second = 'j';
	mul[p] = "j";
	p.second = 'k';
	mul[p] = "k";

	p.first = 'i';
	p.second = '1';
	mul[p] = "i";
	p.second = 'i';
	mul[p] = "-1";
	p.second = 'j';
	mul[p] = "k";
	p.second = 'k';
	mul[p] = "-j";

	p.first = 'j';
	p.second = '1';
	mul[p] = "j";
	p.second = 'i';
	mul[p] = "-k";
	p.second = 'j';
	mul[p] = "-1";
	p.second = 'k';
	mul[p] = "i";

	p.first = 'k';
	p.second = '1';
	mul[p] = "k";
	p.second = 'i';
	mul[p] = "j";
	p.second = 'j';
	mul[p] = "-i";
	p.second = 'k';
	mul[p] = "-1";
	long long n,k,x;
	cin >> k;
	string s,t;
	char a;
	int sign;
	bool flag;
	for (int i = 1; i <= k; i++)
	{
		cin >> n;
		cin >> x;
		cin >> s;
		a = '1';
		sign = 1;
		flag = false;
		for (int j = 0; j < n; j++)
		{
			t = mul[make_pair(a, s[j])];
			if (t[0] == '-')
			{
				sign *= -1;
				a = t[1];
			}
			else a = t[0];
		}
		char b='1';
		int signb = 1;
		for (int j = 0; j < x; j++)
		{
			t = mul[make_pair(b, a)];
			signb *= sign;
			if (t[0] == '-')
			{
				signb *= -1;
				b = t[1];
			}
			else b = t[0];
		}
		flag = false;
		a = b;
		sign = signb;
		if ((a == '1') && (sign == -1))
		{
			int l = 0;
			int r = 0;
			int j = 0;
			sign = 1;
			a = '1';
			while (l < n*x)
			{
				t = mul[make_pair(a, s[j])];
				if (t[0] == '-')
				{
					sign *= -1;
					a = t[1];
				}
				else a = t[0];
				j++;
				if (j == n) j = 0;
				if ((a == 'i') && (sign == 1))
				{
					l++;
					break;
				}
				l++;
			}

			r = 0;
			j = n-1;
			sign = 1;
			a = '1';
			while ((l < n*x - r) && (r < n*x))
			{
				t = mul[make_pair(s[j], a)];
				if (t[0] == '-')
				{
					sign *= -1;
					a = t[1];
				}
				else a = t[0];
				j--;
				if (j == -1) j = n-1;
				if ((a == 'k') && (sign == 1))
				{
					r++;
					break;
				}
				r++;
			}
			if (l < n*x - r) flag = true;
			else flag = false;

		}
		cout << "Case #" << i << ": ";
		if (flag) cout << "YES";
		else cout << "NO";
		cout << endl;
	}
	return 0;
}
