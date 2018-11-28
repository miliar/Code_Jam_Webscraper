#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>


#include <set>
#include <utility>

#include "helper.h"

using namespace std;


bool is_cons(char c)
{
  if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
    return false;
  return true;
}

unsigned process(char* tab, unsigned length, unsigned n)
{
  // for (unsigned i = 0; i < length; i++)
  //   printf("%c", tab[i]);
  // printf("\n");
  // printf("%d", n);


  set< pair<unsigned, unsigned> > pairs;
  unsigned res = 0;

  for (unsigned i = 0; i < length - n + 1; i++) {
    bool cont = false;
    for (unsigned j = i; j < i + n; j++)
      if (!is_cons(tab[j])) {
        cont = true;
        break;
      }
    if (cont)
      continue;

    for(unsigned j = 0; j <= i; j++) {
      for (unsigned k = i + n - 1; k < length; k++)
        if (pairs.find(make_pair(j,k)) == pairs.end()) {
          pairs.insert(make_pair(j,k));
          res++;
        }
    }


  }


  return res;
}



int main()
{
  unsigned nb_case;
  r1int(&nb_case);
  for (unsigned i = 0; i < nb_case; i++) {

    char tab[1000000];
    char a;
    unsigned length = 0;
    while (1) {
      fscanf(stdin, "%c", &a);
      if (a == ' ')
        break;
      tab[length] = a;
      length++;
    }

    unsigned n;
    fscanf(stdin, "%d", &n);

    unsigned res = process(tab, length, n);


    fscanf(stdin, "%c", &a);
    assert(a == '\n');


    printf("Case #%d: %d", i + 1, res);
    printf("\n");
  }

  return EXIT_SUCCESS;
}
