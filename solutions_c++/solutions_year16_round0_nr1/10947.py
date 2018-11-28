#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
bool ar[10];
bool check()
{
	for (int i = 0; i < 10; i++)
		if (!ar[i])
			return false;
	return true;
}
void setDigit(ll t)
{
	while (t > 0)
	{
		ar[t % 10] = 1;
		t /= 10;
	}
}
int main()
 {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	ll t, p, cur;
	bool fl = false;
	for (int i = 0; i < n; i++)
	{
		fl = false;
		for (int j = 0; j < 10; j++) ar[j] = 0;
		cin >> t;
		p = 1;
		do
		{
			cur = t * p;
			p++;
			if (p > 20000)
			{
				fl = true;
				break;
			}
			setDigit(cur);
		}while (!check());
		if(fl)
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		else
		cout << "Case #" << i + 1 << ": " << cur << endl;
	}
	return 0;
}