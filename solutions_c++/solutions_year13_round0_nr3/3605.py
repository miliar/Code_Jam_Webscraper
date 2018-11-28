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

    int A, B;

    int less100[5] = {1, 2, 3, 11, 22};

    for (int i=0; i<ncases; ++i) 
    {

        fscanf(fp, "%d %d\n", &A, &B );

        printf("Case #%d: %d %d\n", i+1, A, B);

        int count = 0;
        for (int j=0; j<5; ++j)
        {
            int cur = less100[j];
            cur *= cur;
            printf("%d ", cur);
            if ( (cur>=A) && (cur<=B) )  
                ++count;
        }
        printf("\n");
        printf("Case #%d: %d\n", i+1, count);
        ofs<<"Case #"<<i+1<<": "<<count<<"\n";
    }


    ofs.close();

    fclose(fp);
}

