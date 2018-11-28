#include <cstdio>

FILE *file_in;
FILE *file_out;

void test(int index)
{
    char znak = '@', posledni = '@';
    bool prvni = true;
    int vysledek = 0;
    fscanf(file_in, "%c", &znak);
    while(znak != '\n')
    {
        if(prvni == true)
        {
            prvni = false;
        }
        else
        {
            if(znak != posledni)
            {
                vysledek++;
            }
        }
        posledni = znak;
        fscanf(file_in, "%c", &znak);
    }
    if(posledni == '-')
    {
        vysledek++;
    }
    fprintf(file_out, "Case #%d: %d\n", index, vysledek);
}

int main()
{
    file_in = fopen("B-large.in", "r");
    file_out = fopen("out.txt", "w");
    int T;
    fscanf(file_in, "%d\n", &T);
    for(int i=0; i<T; i++)
    {
        test(i+1);
    }
    fclose(file_in);
    fclose(file_out);
    return 0;
}
