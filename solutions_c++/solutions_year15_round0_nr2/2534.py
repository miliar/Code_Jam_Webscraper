#include <stdio.h>
#include <queue>
#include <algorithm>
#define INF 1000000000
#include <vector>
using namespace std;

vector <int> fila2;

int v[1005];

int resolve(priority_queue<int> fila)
{
	int a = fila.top();
	if (a <= 3) 
		return a;
	int menor = a;
	priority_queue<int> fila2;
	fila2 = fila;
	for (int i = 2; i <= a/2; i++)
	{
		fila2 = fila;
		fila2.pop();
		fila2.push(i);
		fila2.push(a-i);
		menor = min(menor, 1+resolve(fila2));
	}
	return menor;
}

int main()
{
	priority_queue<int> fila;
	int t;
	scanf("%d",&t);
	int teste = 0;
	while(t--)
	{
		while(!fila.empty())
			fila.pop();
		teste++;
		int d;
		scanf("%d",&d);
		for (int i = 1; i <= d; i++)
		{	
			scanf("%d",&v[i]);
			//printf("%d ",v[i]);
			fila.push(v[i]);
		}
		//printf("\n");
		int tempo = INF;

			tempo = min(tempo,resolve(fila));

		

		printf("Case #%d: ",teste);
		printf("%d\n",tempo);


	}

	return 0;
}