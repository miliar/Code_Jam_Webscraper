#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;
int main()
{
	int Z, n, m ,li, tab[100][100], i, j, kol[100], row[100], wynik;
	scanf("%d", &Z);
	for(li = 1; li <= Z; li++)
	{
		wynik = 0;
		scanf("%d %d", &n, &m);
		for(i = 0; i < max(n, m); i++) kol[i] = row[i] = 0;
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++)
			{
				scanf("%d", &tab[i][j]);
				kol[j] = max(kol[j], tab[i][j]);
				row[i] = max(row[i], tab[i][j]);
			}
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++)
				if(tab[i][j] == min(kol[j], row[i])) wynik++;
		if(wynik == n * m) printf("Case #%d: YES\n", li);
		else printf("Case #%d: NO\n", li);
	}
	return 0;
}
