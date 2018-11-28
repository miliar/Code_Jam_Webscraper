#include<stdio.h>
#include<string.h>

int main()
{
    FILE *fin,*fout;
    fin = fopen("C:\\Users\\a123\\Desktop\\code jam QR\\input1.txt","r");
    fout = fopen("C:\\Users\\a123\\Desktop\\code jam QR\\output1.txt","w+t");
    int w;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        char pc[1500];
        int fnum;
        fscanf(fin,"%s",pc);
        fscanf(fin,"%d",&fnum);
        int lpc = strlen(pc);
        int last = lpc-fnum;
        int ftime = 0;
        for(int i = 0 ; i <= last ; i++){
            if(pc[i] == '-'){
                for(int j = i ; j <= i+fnum-1 ; j++){
                    if(pc[j] == '-') pc[j] = '+';
                    else pc[j] = '-';
                }
                ftime++;
            }
        }
        int jud = 1;
        for(int i = last+1 ; i <= lpc-1; i++){
            if(pc[i] == '-'){
                jud = 0;
                break;
            }
        }
        if(jud == 0){
            fprintf(fout,"Case #%d: IMPOSSIBLE\n",q);
        }
        else{
            fprintf(fout,"Case #%d: %d\n",q,ftime);
        }
    }
}
