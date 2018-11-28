#include <stdio.h>

FILE *fin, *fout;
int T, ans1, ans2, row1[4], row2[4], a, b, c, d, times_used[16], ans;

void read_solve_write();

int main(){
    read_solve_write();
    return 0;
}

void read_solve_write(){
    fin = fopen("A-small-attempt0.in.txt","r");
    fout = fopen("results.txt","w");
        fscanf(fin,"%d\n",&T);
        for(int i = 0; i < T; i++){
            ans = -1;
            for(int j = 0; j < 16; j++){
                times_used[j] = 0;
            }
            fscanf(fin,"%d\n",&ans1);
            for(int j = 0; j < 4; j++){
                fscanf(fin,"%d %d %d %d\n",&a,&b,&c,&d);
                if(j+1 == ans1){
                    row1[0] = a;
                    row1[1] = b;
                    row1[2] = c;
                    row1[3] = d;
                }
            }
            fscanf(fin,"%d\n",&ans2);
            for(int j = 0; j < 4; j++){
                fscanf(fin,"%d %d %d %d\n",&a,&b,&c,&d);
                if(j+1 == ans2){
                    row2[0] = a;
                    row2[1] = b;
                    row2[2] = c;
                    row2[3] = d;
                }
            }
            for(int j = 0; j < 4; j++){
                //printf("%d ",row1[j]);
                times_used[row2[j]-1]++;
                times_used[row1[j]-1]++;
            }/*printf("\n");
            for(int j = 0; j < 4; j++){
                printf("%d ",row2[j]);
            }printf("\n");*/
            /*for(int j = 0; j < 16; j++){
                printf("%d) %d\n",j+1,times_used[j]);
            }*/
            for(int j = 0; j < 16; j++){
                if(times_used[j] == 2 && ans == -1) ans = j;
                else if(times_used[j] == 2 && ans != -1){ans = -2; break;}
            }
            //printf("Case #%d: \n",i+1);
            if(ans == -2) fprintf(fout,"Case #%d: Bad magician!\n",i+1);
            else if(ans == -1) fprintf(fout,"Case #%d: Volunteer cheated!\n",i+1);
            else fprintf(fout,"Case #%d: %d\n",i+1,ans+1);
        }
    fclose(fout);
    fclose(fin);
}
