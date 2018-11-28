#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int T;
char s[105][105];
int len;

main(){
    FILE *inp = fopen("revpanL.in", "r"), *outp = fopen("revpan.out", "w");
    fscanf(inp, "%d\n", &T);
    int i,j;
    char temp;
    int flips;
    for(i = 0; i < T; i++){
        flips = 0;
        for(j = 0; j <= 101; j++){
            fscanf(inp, "%c", &temp);
            if(temp == '+' || temp == '-') s[i][j] = temp;
            else{
                len = j;
                break;
            }
        }
        for(j = len - 1; j >= 0; j--){
            if(s[i][j] == '+' && flips%2 == 1){
                flips++;
            }
            if (s[i][j] == '-' && flips%2 == 0) flips++;
        }
        fprintf(outp, "Case #%d: %d\n", i+1, flips);
    }
    return 0;
}
