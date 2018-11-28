#include <iostream>
#include <queue>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

int tab[20];
int pom[5];

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		for(int j = 1; j <= 16; ++j) tab[j] = 0;
		int a;
		cin >> a;
		for(int j = 1; j <= 4; ++j)
		{
			for(int z = 0; z < 4; ++z) cin >> pom[z];
			if(a == j) for(int z = 0; z < 4; ++z) tab[pom[z]]++;
		}
		cin >> a;
		for(int j = 1; j <= 4; ++j)
		{
			for(int z = 0; z < 4; ++z) cin >> pom[z];
			if(a == j) for(int z = 0; z < 4; ++z) tab[pom[z]]++;
		}

		int w = 0;
		int wyn;
		for(int j = 1; j <= 16; ++j) 
		{
			if(tab[j] == 2) 
			{
				w++;
				wyn = j;
			}
		}

		cout << "Case #" << i + 1 << ": ";
		if(w == 0) cout << "Volunteer cheated!" << endl;
		else if(w > 1) cout << "Bad magician!" << endl;
		else cout << wyn << endl;
	}
	return 0;
}