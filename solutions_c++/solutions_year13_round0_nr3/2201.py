#include <iostream>
#include <string>

using namespace std;

int test; 
int t; 
long long a;
long long b; 
int j; 
long long ans = 0; 


bool check(long long a)
{
	string s ="";
	while (a > 0)
	{
		s = char(a % 10 + 48) + s;
		a /= 10;
	}
	int i1 = 0;
	int j1 = s.size() - 1;
	while (i1 < j1)
		if (s[i1] != s[j1])
			return false;
		else i1++, j1--;
	return true;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> test;
	for(int t = 1; t <= test; t++)
	{
		cout << "Case #" << t << ": ";
		cin >> a >> b;
		ans = 0;
		for (int i = a; i <= b; i++)
		{
			if (   ((int(sqrt(i*1.0)) * int(sqrt(i*1.0))) == i) && check(int(sqrt(i*1.0))) && check(i))
				ans++;
		}
		cout << ans << endl;
	}
}		


