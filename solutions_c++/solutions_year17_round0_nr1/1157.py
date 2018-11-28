#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;

string s;
int n;
void ubah(int a, int b)
{
//	cout << a << " " << b << "\n";
	for(int i = a; i <= a+b; i++)
	{
		s[i] = (s[i] == '+')? '-' : '+';
	}
}

int main()
{
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for(int tc = 1; tc <= t; tc++)
	{
		cin >> s >> n;
		int res = 0;
		bool bol = 1;
		cout << "Case #" << tc << ": ";
		for(int i = 0; i < s.length(); i++)
		{
	//		cout << s << " " << i << " " << s[i] << "\n";
			if(s[i] == '-' && i+n-1 >= s.length())
			{
				cout << "IMPOSSIBLE\n";
				bol = 0;
				break;
			}
			else if(s[i] == '-') 
			{
				ubah(i, n-1);
				res++;
			}
		}
		if(bol) cout << res << "\n";
	}
}
