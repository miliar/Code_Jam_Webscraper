#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <algorithm>
#include <fstream>


using namespace std;

int main ()
{
    FILE *in = fopen ("A-small-attempt2.in","r");
    FILE *out = fopen ("a.out","w");
    
    int T, A, B;
    int a,b,c,d;    
    map<int, int> array;    
    
    fscanf(in ,"%d", &T);    
    for (int i =0; i < T; i++ )
    {
        fscanf(in,"%d", &A);

        for(int j =1; j <= 4; j++)
        {
              fscanf(in, "%d %d %d %d", &a, &b, &c, &d);        
              if ( j==A )
              {
                array[a]++;
                array[b]++;
                array[c]++;
                array[d]++;
              }
        }
        
        fscanf(in, "%d", &B);

        for(int j =1; j <= 4; j++)
        {
              fscanf(in,"%d %d %d %d", &a, &b, &c, &d);        
              if ( j==B )
              {
                array[a]++;
                array[b]++;
                array[c]++;
                array[d]++;
              }
        }

        int count2 = 0;
        int value = 0;        


        
        for (int k =0; k < array.size() ; k++)
        {
          if (array[k] == 2)
          {
             count2++;
             value = k;
          }
        }
        
        if (count2 == 1)
        {
          fprintf (out,"Case #%d: %d\n",i+1,value);
        }
        else if ( count2 > 1 )
        {
             fprintf (out,"Case #%d: Bad magician!\n",i+1);
        }
        else 
        {
             fprintf (out,"Case #%d: Volunteer cheated!\n",i+1);
        }        
        array.clear(); 
    }    
}
