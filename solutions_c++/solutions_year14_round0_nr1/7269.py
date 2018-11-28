#include <iostream>
#include <stdio.h>
FILE *in = fopen("/users/sungpi/documents/A-small-attempt0.in", "r");
FILE *out = fopen("/users/sungpi/documents/output.txt", "w");
void tc()
{
    static int n = 1;
    int t;
    fscanf(in, "%d", &t);
    int toGet;
    int row[4];
    int col[4];
    for(int i=0; i<4; ++i){
        for(int j=0; j<4; ++j){
            if(i+1 == t){
                fscanf(in, "%d", &row[j]);
            }
            else{
                fscanf(in, "%d", &toGet);
            }
        }
    }
    fscanf(in, "%d", &t);
    for(int i=0; i<4; ++i){
        for(int j=0; j<4; ++j){
            if(i+1 == t){
                fscanf(in, "%d", &col[j]);
            }
            else{
                fscanf(in, "%d", &toGet);
            }
        }
    }
    
    int check[4][4];
    int count = 0;
    int save = 0;
    for(int i=0; i<4; ++i){
        for(int j=0; j<4; ++j){
            check[i][j] = -1;
            if(row[i] == col[j])
            {
                count ++;
                save = row[i];
            }
        }
    }
    fprintf(out, "Case #%d: ", n++);
    if(count == 1) fprintf(out, "%d", save);
    else if(count == 0) fprintf(out, "Volunteer cheated!");
    else fprintf(out, "Bad magician!");
    fprintf(out, "\n");
}
int main(void)
{
    int t;
    fscanf(in, "%d", &t);
    
    while(t--) tc();
}