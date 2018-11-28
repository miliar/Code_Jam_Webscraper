#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char check_diagonal ();
char check_vertical ();
char check_horizontal ();

char arr[16];

int main ()
{
    int count = 0, value, flag = 0, tests;
    int T; // = rand ();
    char ch;

    printf ("number of test:");
    scanf ("%d", &tests);

    while (tests--)
    {
    memset ( (char *) arr, '.', 16);


    for (count = 0; count <= 15; count++)
    {
        scanf ("%c", &arr[count]);
        if (arr[count] == '\n') --count;

        if (arr[count] == '.')
            flag = 1;
    }

   if ( (ch = check_diagonal ()) != '.')
       printf ("diagonal>>  %c, won\n", ch);

   else if ( (ch = check_vertical ()) != '.')
       printf ("vertical>>> %c, won\n", ch);

   else if ( (ch = check_horizontal ()) != '.')
       printf ("horizontal>>> %c, won\n", ch);

   else if (flag)
       printf (" Game is not over - %d %c\n", count, ch);

   else
       printf ("drawn\n");
   flag = 0;
   }

    return 0;
}

char check_diagonal ()
{



    if ( (arr[0] != 'T') || (arr[3] != 'T') )
    {
        if ( (arr[0] != '.') && ( (arr[0] == arr[5]) || (arr[5] == 'T') ) && ( (arr[0] == arr[10]) || (arr[10] == 'T') )  && ( (arr[0] == arr[15]) || (arr[15] == 'T')
 ) )
             return arr[0];

        else if ( (arr[3] != '.') && ( (arr[3] == arr[6]) || (arr[6] == 'T') ) && ( (arr[3] == arr[9]) || (arr[9] == 'T') ) && ( (arr[3] == arr[12]) || (arr[12] == 'T
') ) )
              return arr[3];
    }

    else
    {
        if ( (arr[5] == arr[15]) && (arr[5] == arr[10]) )
            return arr[5];
        else if ( (arr[6] == arr[9]) && (arr[6] == arr[12]) )
            return arr[6];
   }
   return '.';
}

char check_vertical ()
{
    int i = 0;

     for (; i <= 3; i++)
     {
         if (arr[i] != 'T')
         {

             if ( (arr[i] != '.') && ( (arr[i] == arr[i+4]) || (arr[i+4] == 'T') ) && ( (arr[i] == arr[i+8]) || (arr[i+8] == 'T') )  && ( (arr[i] == arr[i+12]) || (ar
r[i+12] == 'T') ) )
                   return arr[i];
        } else {
             if ( (arr[i+4] == arr[i+8]) && (arr[i+4] == arr[i+12]) )
                 return arr[i+4];
        }

     }
     return '.';
}

char check_horizontal ()
{
    int i = 0;

    for (; i < 16; )
    {
         if (arr[i] != 'T')
         {
              if ( (arr[i] != '.') && ( (arr[i] == arr[i+1]) || (arr[i+1] == 'T') ) && ( (arr[i] == arr[i+2]) || (arr[i+2] == 'T') )  && ( (arr[i] == arr[i+3]) || (ar
r[i+3] == 'T') ) )
                 return arr[i];
         } else {
              if ( (arr[i+1] == arr[i+2]) && (arr[i+1] == arr[i+4]) )
                 return arr[i+1];
        }
         i += 4;
    }
    return '.';
}