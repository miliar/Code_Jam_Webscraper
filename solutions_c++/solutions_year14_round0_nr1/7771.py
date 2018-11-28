#include <stdio.h>

int main(void)
{
        int n,i,j,k,row,col,ans,temp,cnt;
        bool list[16];

        FILE *in = fopen("input.txt","r");
        FILE *out = fopen("output.txt","w");

        fscanf(in,"%d",&n);
        k=1;
        while (k<=n){

                for (i=0; i<16; i++){
                        list[i] = false;
                }

                cnt = 0;
                ans = 0;

                fscanf(in,"%d",&row);
                for (i=0; i<4; i++){
                        for (j=0; j<4; j++){
                                fscanf(in,"%d",&temp);
                                if (i==row-1){
                                        list[temp-1] = true;
                                }
                        }
                }

                fscanf(in,"%d",&row);
                for (i=0; i<4; i++){
                        for (j=0; j<4; j++){
                                fscanf(in,"%d",&temp);
                                if (i==row-1 && list[temp-1]){
                                        cnt++;
                                        ans = temp;
                                }
                        }
                }

                if (cnt==0){
                        fprintf(out,"Case #%d: Volunteer cheated!\n",k);
                }
                else if (cnt==1){
                        fprintf(out,"Case #%d: %d\n",k,ans);
                }
                else if (cnt>1){
                        fprintf(out,"Case #%d: Bad magician!\n",k);
                }

                k++;
        }

        return 0;
}
