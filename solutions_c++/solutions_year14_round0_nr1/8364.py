#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>

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

    int before[16], after[16];

    int result;
    for (int i=0; i<ncases; ++i) 
    {
        memset(before, 0, sizeof(before));
        memset(after, 0, sizeof(after));

        int answer, ival;

        result = fscanf(fp, "%d\n", &answer); 
        if(result==0) printf("read error!\n");
        for (auto k=0; k<4; ++k)
        {
            for (auto j=0; j<4; ++j)
            { 
                result = fscanf(fp, "%d ", &ival);
                if(result==0) printf("read error!\n");
                printf("%d ", ival);
                if (answer == (k+1))
                {
                    before[ival-1]=1;
                }
            }
            printf("\n");
        }

        result=fscanf(fp, "%d\n", &answer); 
        if(result==0) printf("read error!\n");
        for (auto k=0; k<4; ++k)
        {
            for (auto j=0; j<4; ++j)
            { 
                result = fscanf(fp, "%d ", &ival);
                if(result==0) printf("read error!\n");
                printf("%d ", ival);
                if (answer == (k+1))
                {
                    after[ival-1]=1;
                }
            }
            printf("\n");
        }

        result=-1;
        for (auto i=0; i<16; ++i)
        {
            if (before[i]>0 && after[i]>0)
            {
                if (result==-1)
                {
                    result = i;
                }
                else 
                {
                    result = -2;
                }
            }
        }
        
        ofs<<"Case #"<<i+1<<": ";
        if (result==-2)
        {
            ofs<<"Bad magician!"<<std::endl;
        }
        else if (result==-1)
        {
            ofs<<"Volunteer cheated!"<<std::endl;
        }
        else
        {
            ofs<<result+1<<std::endl;
        }

    }


    ofs.close();

    fclose(fp);
}

