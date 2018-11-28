#include<iostream>
using namespace std;

void solve()
{
	int fs,nd, wp, x;
	int tab[4];
	cin >> fs;
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			cin >> nd;
			if(i+1 == fs)tab[j] = nd;
		}
	}
	cin >> nd;
	fs = 0;
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			cin >> x;
			if(i+1 == nd)
				for(int k = 0; k < 4; k++)if(tab[k] == x)fs++, wp = x;
		}
	}

	if(fs == 0)cout << "Volunteer cheated!\n";
	else if(fs == 1)cout << wp << endl;
	else cout << "Bad magician!\n";
}

int main()
{
	int n;
	cin >> n;
	for(int i = 1; i <= n; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}
