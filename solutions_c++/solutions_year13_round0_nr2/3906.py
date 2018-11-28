#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>

#define zduration 1000
#define hitcharge 750
#define mstep 100


int main(int argc, char** argv) {
    if (argc<3) {
        printf("not enough parameters: %d\n", argc);
        return 0;
    }
    FILE *fp;
    printf("%s\n", argv[1]);

    if ( (fp = fopen( (const char*) argv[1], "r" )) == NULL ) {
        printf("Open Input File ERROR!\n"); 
        return 0;
    }

    std::ofstream ofs(argv[2]);

    int ncases;
    fscanf(fp, "%d\n", &ncases);

    printf("#Cases: %d\n", ncases);
    if (ncases<=0) return -1;

    int N, M;

    int garden[100][100];
    int cutheightx[100], cutheighty[100];

    for (int i=0; i<ncases; ++i) 
    {

        fscanf(fp, "%d %d\n", &N, &M );

        printf("Case #%d: %d %d\n", i+1, N, M);

        for (int j=0; j<N; ++j)
        {
            for (int k=0; k<M; ++k)
            {
                fscanf(fp, "%d ", &garden[j][k]); 
            }
            fscanf(fp, "\n"); 
        }
        memset(cutheightx, 0, 100*sizeof(int));
        memset(cutheighty, 0, 100*sizeof(int));
        /*
        for (int j=0; j<N; ++j)
        {
            for (int k=0; k<M; ++k)
            {
                printf("%d ", garden[j][k]);
            }
            printf("\n");
        }
        */

        for (int j=0; j<N; ++j)
        {
            for (int k=0; k<M; ++k)
            {
                cutheighty[j] = std::max(cutheighty[j], garden[j][k]);
                cutheightx[k] = std::max(cutheightx[k], garden[j][k]);
            }
        }

        bool possible = true;
        for (int j=0; j<N; ++j)
        {
            for (int k=0; k<M; ++k)
            {
                int realheight = std::min(cutheighty[j], cutheightx[k]), eheight = garden[j][k];
                possible = possible && (realheight == eheight);
            }
        }

        if (possible)
        {
            printf("Case #%d: YES\n", i+1);
            ofs<<"Case #"<<i+1<<": YES\n";
        }
        else 
        {
            printf("Case #%d: NO\n", i+1);
            ofs<<"Case #"<<i+1<<": NO\n";
        }
    }


    ofs.close();

    fclose(fp);
}

