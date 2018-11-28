#include <stdio.h>


int main()
{
    FILE *f, *g;
    f = fopen("input", "r");
    g = fopen("output", "w");

    int N, i, j, S;
    int stands, friends;
    char c;
    fscanf(f, "%d ", &N);

    for(i = 1; i <= N; i++){
        friends = 0;
        stands = 0;
        fscanf(f, "%d ", &S);

        for(j = 0; j <= S; j++){
            fscanf(f, "%c", &c);
            if(c == '\n') break;
            c -= 48;


            if(j > stands){
                stands++;
                friends++;
            }
            stands += c;
        }

        fprintf(g, "Case #%d: %d\n", i, friends);
    }

    fclose(f);
    fclose(g);
    return 0;
}
