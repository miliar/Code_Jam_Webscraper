#include <iostream>
#include <cstdio>

using namespace std;

int zamien(char a)
{
	return a - (int)'0';
}

int tab[10000];

int main()
{
	int x;
	cin >> x;
	for(int h = 1 ; h <= x ; h++)
	{
		int n;
		string a;
		cin >> n >> a;
		for(int i = 0 ; i <= n ; i++)
		{
			tab[i] = zamien(a[i]);
		}	
		int wynik = 0;
		while(true)
		{
			//cout << "kiczka" ;
			int liczbaStojacych =  0;
			bool czyDziala = true;
			for(int i = 0 ; i <= n ; i++)
			{
				if(i <= liczbaStojacych)
				{
					//cout << tab[i] << " ";
					liczbaStojacych += tab[i];
				}
				else
				{
					//cout << "kiczkaaaaaaaaaaaaaaaaaaaaaaaaa";
					czyDziala = false;
					break;
				}
			}
			if(czyDziala == false)
			{
				tab[0]++;
				wynik++;
			}
			else
			{
				cout << "Case #" << h << ": " << wynik << "\n";
				//return 0;
				break;
			}
		}
	
	}
}
