#include <iostream>
#include <cstdlib>
#include <iomanip> 

using namespace std;

typedef struct no
{
      double valor;
      int flag;
}no;

int war (no *, no *, int);
int procurar (double , no *, int);
int procurar_2 (double , no *, int);
int dec_war (no *, no *, int);

int main ()
{
	no naomi_tora [100];
	no ken_tora [100];
	int t,i, pontos_1;
	int pontos_2;
	int qtdade;
	int testes;

	cin >> testes;
	for (t = 1; t <= testes; t++)
	{
		cin >> qtdade;
		for (i = 0; i < qtdade; i++)
		{
			cin >> naomi_tora[i].valor;
			naomi_tora[i].flag = 0;
		}
		for (i = 0; i < qtdade; i++)
		{
			cin >> ken_tora[i].valor;
			ken_tora[i].flag = 0;
		}
		
		pontos_1 = war (naomi_tora, ken_tora, qtdade);
		for (i = 0; i < qtdade; i++)
		{
			naomi_tora[i].flag = 0;
			ken_tora[i].flag = 0;
		}
		pontos_2 = dec_war (naomi_tora, ken_tora, qtdade);
		cout << "Case #" << t << ": " << pontos_2 << " " << pontos_1;
		cout << '\n';
	}
}

int comparar (const void *a, const void *b)
{
	 struct no *elem1 = (struct no *)a;
	 struct no *elem2 = (struct no *)b;
	 if ( elem1->valor <  elem2->valor ) return -1;
  	 if ( elem1->valor == elem2->valor ) return  0;
  	 if ( elem1->valor >  elem2->valor ) return  1;
}

int war (no *naomi_tora, no *ken_tora, int qtdade)
{
	double carta_naomi;
	int i, pos_carta_ken, ponto;

	ponto = 0;
	qsort (naomi_tora, qtdade, sizeof (struct no), comparar);
	qsort (ken_tora, qtdade, sizeof (struct no), comparar);
	for (i = 0; i < qtdade; i++)
	{
		carta_naomi = naomi_tora[i].valor;
		pos_carta_ken = procurar (naomi_tora[i].valor, ken_tora, qtdade);
		if (carta_naomi > ken_tora[pos_carta_ken].valor)
			ponto++;
	}
	return ponto;
}

int procurar (double carta_naomi, no *ken_tora, int qtdade)
{
	int i;
	for (i = 0; i < qtdade; i++)
	{
		if (ken_tora[i].valor > carta_naomi && ken_tora[i].flag != -1)
		{
			ken_tora[i].flag = -1;
			return i;
		}	
	}
	for (i = 0; i < qtdade; i++)	
	{
		if (ken_tora[i].flag != -1)
		{
			ken_tora[i].flag = -1;
			return i;
		}
	}
}


int dec_war (no *naomi_tora, no *ken_tora, int qtdade)
{
	int i;
	double carta_ken;
	int pos_carta_naomi;
	int ponto = 0;

	qsort (naomi_tora, qtdade, sizeof (struct no), comparar);
	qsort (ken_tora, qtdade, sizeof (struct no), comparar);
	for (i = 0; i < qtdade; i++)
	{
		carta_ken = ken_tora[qtdade - 1 - i].valor;
		pos_carta_naomi = procurar_2 (carta_ken, naomi_tora, qtdade);
		if (carta_ken < naomi_tora[pos_carta_naomi].valor)
			ponto++;
	}
	return ponto;
	
	return 0;
	
}

int procurar_2 (double carta_ken, no *naomi_tora, int qtdade)
{
	int i;

	for (i = 0; i < qtdade; i++)
	{
		if ((naomi_tora[i].valor > carta_ken) && (naomi_tora[i].flag != -1))
		{
			naomi_tora[i].flag = -1;
			return i;
		}
	}
	for (i = 0; i < qtdade; i++)
	{
		if (naomi_tora[i].flag != -1)
		{
			naomi_tora[i].flag = -1;
			return i;
		}
	}
}
