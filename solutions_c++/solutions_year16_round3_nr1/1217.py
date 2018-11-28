#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    FILE *f, *g;
    //f = fopen("input", "r");
    //g = fopen("output", "w");
    f = stdin;
    g = stdout;

    int T, N, parties[30];
    char partiesNames[30];
    int i, j, k;
    int tmp1, tmp2, num;

    fscanf(f, "%d ", &T);

    for(j = 0; j < 30; j++){
        parties[j] = 0;
    }

    for(i = 1; i <= T; i++){
        fscanf(f, " %d", &N);

        num = 0;
        for(j = 0; j < N; j++){
            fscanf(f, " %d", parties + j);
            partiesNames[j] = (char)j + 'A';
            num += parties[j];
        }

        //printf("Test %d %c:%d %c:%d %c:%d\n", i, partiesNames[0], parties[0], partiesNames[1], parties[1], partiesNames[2], parties[2]);

        for(j = 0; j < N; j++){
            for(k = 0; k < N-1; k++){
                if(parties[k] < parties[k+1]){
                    tmp1 = parties[k+1];
                    tmp2 = partiesNames[k+1];
                    parties[k+1] = parties[k];
                    partiesNames[k+1] = partiesNames[k];
                    parties[k] = tmp1;
                    partiesNames[k] = tmp2;
                }
            }
        }

        fprintf(g, "Case #%d:", i);

        while(num > 0){
            fprintf(g, " %c", partiesNames[0]);
            parties[0]--;
            num--;
            if(num == 1){
                fprintf(g, "%c", partiesNames[1]);
                parties[1]--;
                num--;
            }
            if(num < 2*parties[1]){
                fprintf(g, "%c", partiesNames[1]);
                parties[1]--;
                num--;
            }

            for(j = 0; j < 3; j++){
                for(k = 0; k < N-1; k++){
                    if(parties[k] < parties[k+1]){
                        tmp1 = parties[k+1];
                        tmp2 = partiesNames[k+1];
                        parties[k+1] = parties[k];
                        partiesNames[k+1] = partiesNames[k];
                        parties[k] = tmp1;
                        partiesNames[k] = tmp2;
                    }
                }
            }
        }

        fprintf(g, "\n");
    }

    fclose(f);
    fclose(g);
    return 0;
}
