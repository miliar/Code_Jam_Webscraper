#include <iostream>
#include <cstdio>
using namespace std;

FILE *file_in;
FILE *file_out;

int vstup[26];
int cisla[10][26];

void load(int index, string s)
{
    for(int i=0; i<26; i++)
        cisla[index][i] = 0;
    for(int i=0; i<s.length(); i++)
    {
        cisla[index][(int)s[i]-(int)'A']++;
    }
}

void init()
{
    load(0, "ZERO");
    load(1, "ONE");
    load(2, "TWO");
    load(3, "THREE");
    load(4, "FOUR");
    load(5, "FIVE");
    load(6, "SIX");
    load(7, "SEVEN");
    load(8, "EIGHT");
    load(9, "NINE");
}

int aktualni[26];
int pocty[10];

bool nalezeno;

bool PLUS(int cislo)
{
     int ok = true;
     for(int i=0; i<26; i++)
     {
         aktualni[i] += cisla[cislo][i];
         if(aktualni[i] > vstup[i])
            ok = false;
     }
     pocty[cislo]++;
     return ok;
}

bool MINUS(int cislo)
{
    for(int i=0; i<26; i++)
    {
        aktualni[i] -= cisla[cislo][i];
    }
    pocty[cislo]--;
}

bool Shodne()
{
    for(int i=0; i<26; i++)
    {
        if(vstup[i] != aktualni[i])
            return false;
    }
    return true;
}

void Hledej(int index)
{
    if(index > 9)
    {
        printf("ERROR\n");
    }
    //printf("Hledej(%d)\n", index);
    //getchar();
    /*
    printf("Hledej(%d) : ", index);
    for(int i=0; i<10; i++)
    {
        printf("%d ", pocty[i]);
    }
    printf("\n");
    */

    if(nalezeno == false)
    {
        while(PLUS(index) == true)
        {
            ;
        }
        //printf("... index=%d stopped after %d\n", index, pocty[index]);
        MINUS(index);
        if(index == 9)
        {
            if(Shodne() == true)
            {
                nalezeno = true;
            }
            else
            {
                while(pocty[index] == 0)
                {
                    index--; // !!!
                }
                MINUS(index);
                Hledej(index+1);
            }
        }
        else
        {
            Hledej(index+1);
        }
    }
}

int Test(int test)
{
    nalezeno = false;
    for(int i=0; i<26; i++)
        vstup[i] = 0;
    char znak;
    fscanf(file_in, "%c", &znak);
    while(znak != '\n')
    {
        //printf("%c\n", znak);
        //printf("znak: %c ... [%d]\n", znak, (int)znak-(int)'A');
        vstup[(int)znak-(int)'A']++;
        fscanf(file_in, "%c", &znak);
    }

    /*
    printf("vstup: ");
    for(int i=0; i<26; i++)
    {
        printf("%d ", vstup[i]);
    }
    printf("\n");
    */

    for(int i=0; i<26; i++)
        aktualni[i] = 0;
    for(int i=0; i<10; i++)
        pocty[i] = 0;
    while(PLUS(0) == true)
    {
        ;
    }
    MINUS(0);
    Hledej(1);

    /*
    for(int i=0; i<10; i++)
    {
        printf("%d ", pocty[i]);
    }
    printf("\n");
    */

    fprintf(file_out, "Case #%d: ", test);
    for(int i=0; i<10; i++)
    {
        if(pocty[i] > 0)
        {
            for(int j=0; j<pocty[i]; j++)
            {
                fprintf(file_out, "%d", i);
            }
        }
    }
    fprintf(file_out, "\n");
}

// OFNERNIU => FOURNINE

int main()
{
    /*
    init();
    int N;
    scanf("%d\n", &N);
    printf("N = %d\n", N);
    for(int i=0; i<N; i++)
        Test(i+1);
    return 0;
    */
    init();
    file_in = fopen("A-small-attempt2.in", "r");
    //file_in = fopen("in.txt", "r");
    file_out = fopen("out.txt", "w");
    int T;
    fscanf(file_in, "%d\n", &T);
    for(int i=0; i<T; i++)
    {
        //printf("test %d\n", i+1);
        Test(i+1);
        //printf("\n");
    }
    fclose(file_in);
    fclose(file_out);
}
