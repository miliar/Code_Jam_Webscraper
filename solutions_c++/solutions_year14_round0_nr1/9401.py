#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

FILE *in = fopen("f.in", "r");
FILE *out = fopen("f.out", "w");

int cnum[20], answer, grid[4][4];

void fill_cnum(){
    for(int q = 0; q < 4; q++){
        int x = grid[answer - 1][q];
        cnum[x] ++;
    }
}

int main(){

    int ntest;
    fscanf(in, "%d", &ntest);
    for(int TEST = 1; TEST <= ntest; TEST++){
        memset(cnum, 0, sizeof cnum);
        for(int q = 0; q < 2; q++){
            fscanf(in, "%d", &answer);
            for(int w = 0; w < 4; w++){
                for(int e = 0; e < 4; e++){
                    fscanf(in, "%d", &grid[w][e]);
                }
            }
            fill_cnum();
        }
        int cnt = 0, ans = -1;
        for(int q = 1; q <= 16; q++){
            if(cnum[q] == 2){
                cnt ++;
                ans = q;
            }
        }
        if(cnt == 0) fprintf(out, "Case #%d: Volunteer cheated!\n", TEST);
        else if(cnt == 1) fprintf(out, "Case #%d: %d\n", TEST, ans);
        else fprintf(out, "Case #%d: Bad magician!\n", TEST);
    }

    return 0;
}
