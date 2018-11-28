#include <stdio.h>
#include <stdlib.h>

#define kMaxSize 101

static const char* YES = "YES";
static const char* NO = "NO";

int findRowMax(int N, int M, int lawn[kMaxSize][kMaxSize], int row, int col)
{
    int max = lawn[row][col];
    for (int i=0; i<M; ++i) {
        if (lawn[row][i] > max) {
            max = lawn[row][i];
        }
    }
    return max;
}

int findColMax(int N, int M, int lawn[kMaxSize][kMaxSize], int row, int col)
{
    int max = lawn[row][col];
    for (int i=0; i<N; ++i) {
        if (lawn[i][col] > max) {
            max = lawn[i][col];
        }
    }
    return max;
}

const char* lawnMower(int N, int M, int lawn[kMaxSize][kMaxSize])
{
    for (int row=0; row<N; ++row) {
        for (int col=0; col<M; ++col) {
            printf("%3d ", lawn[row][col]);
        }
        printf("\n");
    }
    printf("\n");
    
    // for every cell
    for (int row=0; row<N; ++row) {
        for (int col=0; col<M; ++col) {
            // every single other thing in this cells row needs to be <= its height
            // OR
            // every single other thing in this cells column needs to be <= its height
            
            int colMax = findColMax(N, M, lawn, row, col);
            int rowMax = findRowMax(N, M, lawn, row, col);
            int height = lawn[row][col];
            if (colMax > height && rowMax > height) {
                return NO;
            }
        }
    }

    return YES;
}

void codeJam(int numcases, FILE* fin, FILE* fout)
{
    for (int test=0; test<numcases; ++test) {
        int lawn[kMaxSize][kMaxSize] = {0};
        
        int N,M;
        fscanf(fin, "%d %d\n", &N, &M);
        
        for (int row=0; row<N; ++row) {
            for (int col=0; col<M; ++col) {
                int height;
                fscanf(fin, "%d ", &height);
                lawn[row][col] = height;
            }
        }
        fscanf(fin, "\n");
        
        fprintf(fout, "Case #%d: %s\n", test+1, lawnMower(N,M,lawn));
    }
}

int main(int argc, const char * argv[])
{
    if (argc != 3) {
        printf("usage: %s [input.txt] [output.txt]\n", argv[0]);
        exit(1);
    }
    
    FILE* fin = fopen(argv[1], "r");
    if (!fin) {
        printf("unable to open input '%s'\n", argv[1]);
        exit(1);
    }
    
    FILE* fout = fopen(argv[2], "w");
    if (!fout) {
        printf("unable to open output '%s'\n", argv[2]);
        exit(1);
    }

    int numcases = 0;
    fscanf(fin, "%d\n", &numcases);

    printf("code jamming %d cases: '%s' -> '%s'.\n", numcases, argv[1], argv[2]);
    codeJam(numcases, fin, fout);
    
    fclose(fin);
    fclose(fout);
    
    return 0;
}

