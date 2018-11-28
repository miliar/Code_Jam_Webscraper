#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>

#include <iomanip>

#define NMAX 40


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

    int result;
    for (int i=0; i<ncases; ++i) 
    {
        double C, F, X;

        result = fscanf(fp, "%lf %lf %lf\n", &C, &F, &X);
        if (result<=0) printf("read error!\n");
        printf("%f %f %f\n", C, F, X);

        double curF=2, accuT=0;
        while( (X/curF)>(X/(curF+F)+C/curF) )
        {
            accuT+=C/curF;
            curF+=F;
        }
        accuT+=X/curF;

        ofs<<"Case #"<<i+1<<": "<<std::setprecision(9)<<accuT<<std::endl;
    }


    ofs.close();

    fclose(fp);
}

