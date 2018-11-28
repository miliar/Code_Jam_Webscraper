#include<cstdio>
#include<algorithm>
#include<math.h>
using namespace std;
bool czy_palindrom(int liczba)
{
	int inv = 0;
	int pom = liczba;
	while(liczba > 0)
	{
		inv = inv * 10 + (liczba % 10);
		liczba /= 10;
	}
	if(pom == inv)
		return true;
	else
		return false;

}
int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		int pocz, kon;
		int licznik = 0;
		scanf("%d %d", &pocz, &kon);
		int p_kw = sqrt(double(pocz));
		if(p_kw * p_kw < pocz)
			p_kw += 1;
		int k_kw = sqrt(double(kon));
		if(k_kw * k_kw < kon)
			k_kw += 1;
		for(int j = p_kw; j <= k_kw; j++)
		{
			if(czy_palindrom(j) == true && j <= kon)
			{
				int wynik = j * j;
				if(czy_palindrom(wynik) && wynik <= kon)
				{
					++licznik;
					//printf("TAK %d %d\n", j, j*j);
				}
			}
		}
		printf("Case #%d: %d\n", i + 1, licznik);
	}

	
	return 0;
}
