#include <cstdio>

int main()
{
  int t, l, x, cont = 0;
  char str[10000];
  int positivo = 1;
  char aux;

  scanf("%d", &t);

  for (int i = 1; i <= t; i++)
  {
    aux = '1';
    cont = 0;
    positivo = 1;
    scanf("%d%d", &l, &x);

    scanf("%s", str);

    for (int j = 0; j < x; j++)
    {
      for (int k = 0; k < l; k++)
      {
        switch(aux)
        {
          case '1':
          aux = str[k];
          break;

          case 'i':
          if (str[k] == '1')
            aux = 'i';
          else if (str[k] == 'i')
            aux = '1';
          else if (str[k] == 'j')
            aux = 'k';
          else if (str[k] == 'k')
            aux = 'j';
          if (str[k] == 'i' || str[k] == 'k')
          {
            if(positivo == 0)
              positivo = 1;
          else
            positivo = 0;
          }

          break;

          case 'j':
          if (str[k] == '1')
            aux = 'j';
          else if (str[k] == 'i')
            aux = 'k';
          else if (str[k] == 'j')
            aux = '1';
          else if (str[k] == 'k')
            aux = 'i';
          if (str[k] == 'i' || str[k] == 'j')
          {
            if(positivo == 0)
              positivo = 1;
          else
            positivo = 0;
          }

          break;

          case 'k':
          if (str[k] == '1')
            aux = 'k';
          else if (str[k] == 'i')
            aux = 'j';
          else if (str[k] == 'j')
            aux = 'i';
          else if (str[k] == 'k')
            aux = '1';
          if (str[k] == 'k' || str[k] == 'j')
          {
            if(positivo == 0)
              positivo = 1;
          else
            positivo = 0;
          }

          break;
        }
        if ((cont == 0 && aux == 'i' && positivo == 1)||
            (cont == 1 && aux == 'j' && positivo == 1)||
            (cont == 2 && aux == 'k' && positivo == 1))
        {
          cont++;
          aux = '1';
        }
      }
    }
    printf ("Case #%d: ", i);
    if (cont == 3 && aux == '1' && positivo == 1)
      printf("YES\n");
    else
      printf("NO\n");
  }
}
