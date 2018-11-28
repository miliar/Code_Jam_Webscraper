#include <cstdio>

int main()
{
  int t, k, cont, amigos, valor;

    scanf("%d", &t);

   for (int i = 1; i <= t; i++)
   {
     amigos = 0;
     cont = 0;
     scanf("%d", &k);

     for (int j = 0; j <= k; j++)
     {
       scanf("%1d", &valor);
       if (valor > 0 && cont < j)
       {
         amigos += (j - cont);
         cont = j;
       }
       cont += valor;
     }
     printf("Case #%d: %d\n", i, amigos);
   }
   return 0;
}
