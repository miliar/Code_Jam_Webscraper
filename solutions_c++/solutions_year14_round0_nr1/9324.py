#include<stdio.h>
int arr[4][4];
int chk[16];

int main() {
    int T, r1, r2;
    int t, i, j, k;
    int num_of_ans, ans;
    FILE *in, *ou;
    in = fopen("input.txt","r");
    ou = fopen("output.txt","w");
    fscanf(in,"%d",&T);
    for(t=0;t<T;t++) {
        num_of_ans = 0;
        fscanf(in,"%d",&r1);
        for(i=0;i<4;i++) 
            for(j=0;j<4;j++)
                fscanf(in,"%d",&arr[i][j]);
        for(i=0;i<16;i++)
            chk[i]=0;
        for(i=0;i<4;i++)
            chk[arr[r1-1][i]-1] ++;
        fscanf(in,"%d",&r2);
        for(i=0;i<4;i++) 
            for(j=0;j<4;j++)
                fscanf(in,"%d",&arr[i][j]);
        for(i=0;i<4;i++)
            chk[arr[r2-1][i]-1] ++;
        for(i=0;i<16;i++) {
            if(chk[i] >= 2) {
                      num_of_ans ++;
                      ans = i + 1;
            }
        }
        if(num_of_ans == 1) {
             fprintf(ou,"Case #%d: %d\n", t+1, ans);
        }
        else if(num_of_ans == 0) {
             fprintf(ou,"Case #%d: Volunteer cheated!\n", t+1);             
        }
        else {
             fprintf(ou,"Case #%d: Bad magician!\n", t+1);
        }
    }
    
    return 1;   
}
