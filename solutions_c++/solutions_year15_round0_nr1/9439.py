#include <iostream>

using namespace std;

typedef struct sCase{
    int s_max;
    int* audience;
    int result;
} Case;

int ctoi(char d)
{
    char str[2];

    str[0] = d;
    str[1] = '\0';
    return atoi(str);
}

int try_case(Case c) {
    int t = c.audience[0];
    int result = 0;

    for (int i = 1; i <= c.s_max; i++)
    {
        if(t < i && c.audience[i] > 0)
        {
            int extra = i - t;
            result += extra;
            t += extra;
        }

        t += c.audience[i];
    }

    return result;

}

int main(int argc, char *argv[]) {
    FILE *fp = fopen(argv[1], "r");
    if(!fp)
    {
        printf("Could not open file!\n");
        return 1;
    }

    int n_cases = 0;
    fscanf(fp, "%d", &n_cases);

    Case *cases = new Case[n_cases];


    int i, j;

    for(i = 0; i < n_cases; i++)
    {
        fscanf(fp, "%d ", &(cases[i].s_max));

        cases[i].audience = new int[cases[i].s_max + 1];
        memset(cases[i].audience, 0, (cases[i].s_max + 1) * sizeof(int));

        unsigned char curr;
        for(j = 0; j <= cases[i].s_max; j++)
        {
            fscanf(fp, "%c", &curr);
            cases[i].audience[j] = ctoi(curr);
        }

        getc(fp);
    }

    fclose(fp);

    for(i = 0; i < n_cases; i++)
        cases[i].result = try_case(cases[i]);


    FILE *out = fopen("output", "w");
    for(i = 0; i < n_cases; i++)
    {
        fprintf(fp, "Case #%d: %d\n", i + 1, cases[i].result);
    }

    fclose(out);


    return 0;
}