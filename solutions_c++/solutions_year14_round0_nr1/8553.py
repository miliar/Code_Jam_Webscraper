#include <stdio.h>
int main(void) {
    FILE* in=fopen("A-small-attempt1.in","r");
    FILE* out=fopen("output.txt","w");
    int tests,answer1,answer2,square1[16],square2[16],compare,matches,res[2];
    fscanf(in,"%d",&tests);
    for(int i=0;i<tests;++i) {
        fscanf(in,"%d",&answer1);
        fscanf(in,"%d %d %d %d",square1,square1+1,square1+2,square1+3);
        fscanf(in,"%d %d %d %d",square1+4,square1+5,square1+6,square1+7);
        fscanf(in,"%d %d %d %d",square1+8,square1+9,square1+10,square1+11);
        fscanf(in,"%d %d %d %d",square1+12,square1+13,square1+14,square1+15);
        fscanf(in,"%d",&answer2);
        fscanf(in,"%d %d %d %d",square2,square2+1,square2+2,square2+3);
        fscanf(in,"%d %d %d %d",square2+4,square2+5,square2+6,square2+7);
        fscanf(in,"%d %d %d %d",square2+8,square2+9,square2+10,square2+11);
        fscanf(in,"%d %d %d %d",square2+12,square2+13,square2+14,square2+15);
        matches=0;
        for(int j=0;j<4;++j) {
            compare=square1[4*(answer1-1)+j];
            for(int k=0;k<4;++k) {
                if(square2[4*(answer2-1)+k]==compare) {
                    res[matches]=compare;
                    ++matches;
                    if(matches>1)
                        goto end_loop;
                }
            }
        }
        end_loop: ;
        fprintf(out,"Case #%d: ",i+1);
        switch (matches) {
            case 0: {
                fprintf(out,"Volunteer cheated!\n");
                break;
            }
            case 1: {
                fprintf(out,"%d\n",res[0]);
                break;
            }
            case 2: {
                fprintf(out,"Bad magician!\n");
                break;
            }
        }
    }
fclose(in);
fclose(out);
}
