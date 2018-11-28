#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

priority_queue<int> fila;

int menor()
{
  priority_queue<int> copia = fila;
  int maior = fila.top();
  int tempo = maior;

  for (int i = 2; i <= maior / 2; i++)
  {
    fila.pop();
    fila.push(i);
    fila.push(maior - i);
    tempo = min(tempo, 1 + menor());
    fila = copia;
  }
  return tempo;
}

int main()
{
  int t, d;

  scanf("%d", &t);

  for (int i = 1; i <= t; i++)
  {
    while(!fila.empty())
      fila.pop();

    scanf("%d", &d);

    for (int j = 0; j < d; j++)
    {
      int aux;
      scanf("%d", &aux);
      fila.push(aux);
    }

    printf("Case #%d: %d\n", i, menor());
  }

  return 0;
}
