#ifndef _FAREANDSQUARE_HPP
#define _FAREANDSQUARE_HPP

#include <cmath>
#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

class FareAndSquare
{
    private :
        char *input;
        char *output;

    public:

        FareAndSquare(char *input,char *output)
        {
            this->input=input;
            this->output=output;
        }

        void Output()
        {
            int a, b, compt=1, max;
            int r;
            FILE *entree;
            FILE *sortie;
            char *nbre;
            nbre = (char *)malloc(sizeof(char)*22);
            sortie = fopen (output,"w");
            entree = fopen (input, "r");
            if(entree && sortie)
            {
                fgets(nbre,22,entree);
                max = atoi(nbre);
                do
                {
                    fgets(nbre,22,entree);
                    convert(nbre,&a,&b);
                    r=work(a,b);
                    printf("Case #%d: %d\n",compt,r);
                    fprintf(sortie,"Case #%d: %d\n",compt,r);
                    compt++;
                }
                while(compt<=max);
                fclose(entree);
                fclose(sortie);
            }
        }

    protected:

        void convert(char *c, int *a,int *b)
        {
            int i=0;
            while(*(c+i)!=' ') i++;
            *b = atoi(c+i+1);
            *(c+i) = '\0';
            *a = atoi(c);
        }

        int is_palindrome(int nb)
        {
            int x =nb,i=0,result=0;
            while(x>9)
            {
                i++;
                x = x/10;
            }
            x=nb;
            do
            {
                result = result + (x%10) * pow(10,i);
                i--;
                x = x/10;
            }
            while(x != 0);
            return (result==nb)? 1:0;
        }

        int is_square(int nb)
        {
            int carre=sqrt(nb);
            return ((carre*carre)==nb) ? 1:0;
        }

        int work(int a, int b)
        {
            int c=0;
            while(a<=b)
            {
                if(is_square(a)&& is_palindrome(a) && is_palindrome(sqrt(a)))
                {
                    c++;
                }
                a++;
            }
            return c;
        }
};


#endif // _FAREANDSQUARE_HPP
