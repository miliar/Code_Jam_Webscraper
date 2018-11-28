#include <stdio.h>
#include <stdlib.h>
bool viz[100];
int n; //numarul de noduri
bool mat[100][100]; //matricea de adiacenta
void parcurgere(int radacina)
{
	int i;
	int memo[100]; //memorez nodurile dupa nivelul care urmeaza
	int cnt = 0; //cate noduri sunt pe nivelul urmator
	viz[radacina] = true; //vizitez radacina
	for (i = 1; i <= n; i++)
	{
		if (viz[i] == false && mat[radacina][i] == true)
		{
			memo[cnt] = i;
			cnt++;
		}
	}
	for (i = 0; i < cnt; i++)
	{
		printf("%d ", memo[i]); //afisez nivelul urmator
	}
	for (i = 0; i < cnt; i++)
	{
		parcurgere(memo[i]); //reapelez pentru fiecare copil de pe nivelul urmator
	}
}
int main()
{
	int u, v, radacina;
	printf("Dati numarul de noduri:\n");
	scanf("%d", &n);
	printf("Introduceti muchiile iar cand ati terminat introduceti 0 0\n");
	while (true)
	{
		printf("Dati muchia\n");
		scanf("%d %d", &u, &v);
		mat[u][v] = true;
		if (u == 0 && v == 0)
		{
			break;
		}
	}
	printf("Dati radacina\n");
	scanf("%d", &radacina);
	printf("%d ", radacina); // o afisam inainte
	parcurgere(radacina);
	system("pause");

}