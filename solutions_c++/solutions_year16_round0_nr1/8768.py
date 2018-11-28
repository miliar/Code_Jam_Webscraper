#include <cstdio>

FILE *file_in;
FILE *file_out;

bool digits[10];
int number;

inline void parse(int cislo)
{
    int cislice;
    while(cislo > 0)
    {
        cislice = cislo%10;
        cislo = (cislo-cislo%10)/10;
        if(digits[cislice] == false)
        {
            digits[cislice] = true;
            number++;
        }
    }
}

void test(int index)
{
    int cislo;
    fscanf(file_in, "%d", &cislo);
    int add = cislo;
    for(int i=0; i<10; i++)
        digits[i] = false;
    number = 0;
    parse(cislo);
    bool cykli = false;
    if(cislo == 0)
    {
        cykli = true;
    }
    else
    {
        while(number < 10)
        {
            cislo += add;
            parse(cislo);
        }
    }

    if(cykli)
        fprintf(file_out, "Case #%d: INSOMNIA\n", index);
    else
        fprintf(file_out, "Case #%d: %d\n", index, cislo);
}

int main()
{
    file_in = fopen("A-large.in", "r");
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
