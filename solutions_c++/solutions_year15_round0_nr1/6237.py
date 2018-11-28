#include <cstdio>
#include <fstream>
using namespace std;
const int MAXL=1005;
int t,n,wynik,suma,x;
char opis[MAXL];
int main()
{
	fstream plik;
    plik.open( "C:/a.txt", ios::out);
	scanf("%d", &t);
	for(int i=1; i<=t; ++i)
	{
		scanf("%d%s", &n, opis);
		for(int j=0; j<=n; ++j)
		{
			x=opis[j]-'0';
			if(x>0)
			{
				if(suma<j)
				{
					wynik+=j-suma;
					suma=j;
				}
				suma+=x;
			}
		}
		plik<<"Case #"<<i<<": "<<wynik<<endl;
		wynik=0;
		suma=0;	
	}
	plik.close();
}
